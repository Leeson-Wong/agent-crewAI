# CrewAI 人工审核机制详解

## 1. Task 级别的人工审核 (`human_input`)

```python
from crewai import Agent, Task, Crew

agent = Agent(
    role="Writer",
    goal="Write articles",
    backstory="Expert writer"
)

task = Task(
    description="Write an article about AI",
    expected_output="A 500-word article",
    agent=agent,
    human_input=True  # 👈 启用人工审核
)

crew = Crew(agents=[agent], tasks=[task])
result = crew.kickoff()
```

**运行时效果**：
```
[Agent Writer] Working on: Write an article about AI
[Agent Writer] Article: AI is transforming the world...

====
Human Review Required
====
Enter your feedback (or press Enter to accept):
```

## 2. 输出护栏 (`guardrail`) - 自动审核

```python
def content_guardrail(output):
    """审核输出内容"""
    content = output.raw.lower()

    # 检查禁用词
    forbidden_words = ["violence", "illegal"]
    for word in forbidden_words:
        if word in content:
            return (False, f"Content contains forbidden word: {word}")

    # 检查长度
    if len(content) < 100:
        return (False, "Content too short")

    return (True, output.raw)

task = Task(
    description="Write an article",
    expected_output="A well-formatted article",
    agent=agent,
    guardrail=content_guardrail,
    guardrail_max_retries=3
)
```

## 3. Crew 钩子审核 (`@before_kickoff`, `@after_kickoff`)

```python
from crewai.project import CrewBase, agent, task, crew, before_kickoff, after_kickoff

@CrewBase
class ReviewedCrew:
    @agent
    def writer(self) -> Agent:
        return Agent(role="Writer", goal="Write content")

    @task
    def write_task(self) -> Task:
        return Task(description="Write article", agent=self.writer)

    @before_kickoff  # 执行前审核
    def review_inputs(self, inputs):
        print(f"[REVIEW] Reviewing inputs: {inputs}")

        if "topic" not in inputs:
            raise ValueError("Missing required parameter: topic")

        forbidden_topics = ["politics", "religion"]
        if inputs["topic"] in forbidden_topics:
            raise ValueError(f"Topic not allowed: {inputs['topic']}")

        return inputs

    @after_kickoff  # 执行后审核
    def review_outputs(self, result):
        print(f"[REVIEW] Reviewing final output...")

        with open("review_log.txt", "a") as f:
            f.write(f"Output: {result.raw}\n")

        approval = input("Approve this output? (yes/no): ")
        if approval.lower() != "yes":
            raise Exception("Output rejected by reviewer")

        return result
```

## 4. 自定义回调函数 (`callback`)

```python
def review_callback(output):
    print(f"\n{'='*50}")
    print(f"TASK OUTPUT REVIEW")
    print(f"{'='*50}")
    print(f"Output:\n{output.raw}")
    print(f"{'='*50}\n")

    save_to_review_queue(output)
    send_review_notification(output)
    log_audit_trail(output)

    return output

task = Task(
    description="Write an article",
    expected_output="An article",
    agent=agent,
    callback=review_callback
)
```

## 5. Flow 级别审核

```python
from crewai.flow import Flow, listen, start

class ReviewFlow(Flow):
    @start()
    def create_content(self):
        crew = Crew(agents=[self.writer], tasks=[self.write_task])
        return crew.kickoff()

    @listen(create_content)
    def review_content(self, output):
        print("\n" + "="*60)
        print("CONTENT REVIEW REQUIRED")
        print("="*60)
        print(f"\nContent to review:\n{output.raw}")
        print("="*60)

        approval = input("\nDo you approve this content? (yes/no/edit): ")

        if approval.lower() == "yes":
            print("✓ Content approved")
            return {"status": "approved", "content": output.raw}
        elif approval.lower() == "no":
            print("✗ Content rejected")
            return {"status": "rejected", "content": None}
        elif approval.lower() == "edit":
            edited_content = input("Enter edited content: ")
            print("✓ Content edited and approved")
            return {"status": "edited", "content": edited_content}
```

## 6. 多级审核系统

```python
@CrewBase
class MultiLevelReviewCrew:
    @agent
    def writer(self) -> Agent:
        return Agent(role="Content Writer")

    @agent
    def editor(self) -> Agent:
        return Agent(role="Editor")

    @task
    def draft_content(self) -> Task:
        return Task(description="Write initial draft", agent=self.writer)

    @task
    def review_content(self) -> Task:
        return Task(
            description="Review the draft",
            agent=self.editor,
            context=[self.draft_content],
            human_input=True  # 编辑后的人工审核
        )

    @task
    def final_approval(self) -> Task:
        return Task(
            description="Final approval check",
            agent=self.editor,
            context=[self.review_content],
            guardrail=lambda output: (
                True, output.raw
            ) if len(output.raw) > 300 else (
                False, "Content too short"
            )
        )
```

## 7. 审核方式对比

| 方式 | 审核时机 | 阻塞执行 | 自动化 | 适用场景 |
|------|---------|---------|--------|---------|
| `human_input` | Task 完成后 | ✅ 是 | ❌ 否 | 简单人工确认 |
| `guardrail` | Task 完成后 | ✅ 是（失败时） | ✅ 是 | 自动规则验证 |
| `@before_kickoff` | Crew 执行前 | ✅ 是 | ✅/❌ | 输入参数验证 |
| `@after_kickoff` | Crew 执行后 | ✅ 是 | ✅/❌ | 最终输出审核 |
| `callback` | Task 完成后 | ❌ 否 | ✅ 是 | 异步通知/日志 |
| Flow Hooks | 任意阶段 | ✅ 是 | ✅/❌ | 复杂工作流 |

## 8. 分级审核策略

```python
# 低风险：仅自动验证
if risk_level == "low":
    task = Task(guardrail=auto_guardrail)

# 中风险：自动 + 人工
elif risk_level == "medium":
    task = Task(
        guardrail=auto_guardrail,
        human_input=True
    )

# 高风险：多级人工
elif risk_level == "high":
    task = Task(
        guardrail=strict_guardrail,
        human_input=True,
        callback=escalate_to_manager
    )
```
