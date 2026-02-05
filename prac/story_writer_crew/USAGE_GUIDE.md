# 故事创作团队 - 使用指南

## 目录
1. [快速入门](#快速入门)
2. [核心概念](#核心概念)
3. [详细配置](#详细配置)
4. [运行方式](#运行方式)
5. [扩展示例](#扩展示例)
6. [常见问题](#常见问题)

---

## 快速入门

### 步骤 1: 环境准备

确保你已安装 Python 3.10+ 和必要的依赖：

```bash
pip install crewai crewai-tools
```

### 步骤 2: 配置 API 密钥

创建 `.env` 文件：

```bash
OPENAI_API_KEY=sk-your-actual-api-key
OPENAI_MODEL_NAME=gpt-4o-mini
```

### 步骤 3: 运行示例

```bash
cd src/story_writer_crew
python main.py
```

---

## 核心概念

### Agent (智能体)

Agent 是具有特定角色和目标的 AI 实体。本项目包含三个 Agent：

```python
# 1. 故事策划师
story_ideator = Agent(
    role="创意故事策划师",
    goal="创作引人入胜的故事大纲",
    backstory="充满想象力的策划师..."
)

# 2. 小说作家
story_writer = Agent(
    role="专业小说作家",
    goal="撰写完整的故事",
    backstory="经验丰富的畅销作家..."
)

# 3. 文学编辑
story_editor = Agent(
    role="资深文学编辑",
    goal="润色和优化故事",
    backstory="20年经验的编辑..."
)
```

### Task (任务)

Task 是具体的工作单元，分配给特定的 Agent：

```python
outline_task = Task(
    description="基于 {theme} 创作故事大纲",
    expected_output="结构完整的大纲...",
    agent=story_ideator
)

writing_task = Task(
    description="根据大纲撰写故事",
    expected_output="完整的故事...",
    agent=story_writer,
    context=[outline_task]  # 依赖前面的任务
)
```

### Crew (团队)

Crew 编排多个 Agent 协作完成多个 Task：

```python
story_crew = Crew(
    agents=[story_ideator, story_writer, story_editor],
    tasks=[outline_task, writing_task, editing_task],
    process=Process.sequential,  # 顺序执行
    memory=True  # 启用记忆
)
```

---

## 详细配置

### agents.yaml 配置说明

```yaml
# Agent 的唯一标识符（键名）
story_ideator:
  # 角色定位
  role: >
    创意故事策划师
    可以使用多行文本

  # 目标（要达成什么）
  goal: >
    根据 {theme} 主题创作一个引人入胜的故事大纲

  # 背景故事（塑造 Agent 的"人格"）
  backstory: >
    你是一位充满想象力的故事策划师，
    擅长从简单的主题中挖掘深度...
```

**配置要点：**
- `{theme}` 是变量，运行时会替换
- 使用 `>` 表示多行文本
- backstory 越详细，Agent 的"性格"越鲜明

### tasks.yaml 配置说明

```yaml
outline_task:
  # 任务描述（告诉 Agent 要做什么）
  description: >
    基于 {theme} 创作故事大纲。
    大纲应包含：
    1. 故事背景和设定
    2. 主要人物介绍
    3. 完整的故事情节

  # 期望输出（明确要求）
  expected_output: >
    一个结构完整的故事大纲，
    包含故事背景、人物小传、情节大纲

  # 执行此任务的 Agent
  agent: story_ideator

  # 可选：输出到文件
  # output_file: outline.md

writing_task:
  description: "撰写故事"
  agent: story_writer

  # 上下文：依赖前面的任务结果
  context: [outline_task]

  # 输出文件
  output_file: story_draft.md
```

**关键配置：**
- `context`: 定义任务依赖关系，Task 会获取前面 Task 的输出
- `output_file`: 将结果保存到文件
- `agent`: 指定执行者

---

## 运行方式

### 1. 标准运行

```bash
python main.py
```

会执行一次完整的故事创作流程。

### 2. REPL 交互模式

```bash
python main.py repl
```

可以多次输入不同主题，持续创作：

```
🎨 请输入故事主题: 科幻冒险
[创作过程...]
✅ 完成！

🎨 请输入故事主题: 爱情故事
[创作过程...]
✅ 完成！

🎨 请输入故事主题: quit
👋 再见！
```

### 3. 作为模块导入

```python
from story_writer_crew.crew import StoryWriterCrew

# 创建实例
crew = StoryWriterCrew()

# 自定义输入
inputs = {'theme': '赛博朋克'}

# 执行
result = crew.crew().kickoff(inputs=inputs)

# 访问结果
print(result.raw)
print(result.tasks_output)
```

### 4. 批量处理

```python
from story_writer_crew.main import run_for_each

# 多个主题
themes = [
    {'theme': '科幻冒险'},
    {'theme': '奇幻世界'},
    {'theme': '悬疑推理'},
]

# 批量执行
results = run_for_each(themes)
```

---

## 扩展示例

### 示例 1: 添加新的 Agent

**步骤 1**: 在 `config/agents.yaml` 中添加

```yaml
cover_designer:
  role: 书籍封面设计师
  goal: 为故事创作吸引人的封面描述
  backstory: 你是一位专业的设计师...
```

**步骤 2**: 在 `crew.py` 中添加

```python
@agent
def cover_designer(self) -> Agent:
    return Agent(
        config=self.agents_config['cover_designer'],
        verbose=True
    )
```

### 示例 2: 添加新的 Task

**步骤 1**: 在 `config/tasks.yaml` 中添加

```yaml
cover_task:
  description: 为故事设计封面概念
  expected_output: 详细的封面设计描述
  agent: cover_designer
  context: [editing_task]
```

**步骤 2**: 在 `crew.py` 中添加

```python
@task
def cover_task(self) -> Task:
    return Task(
        config=self.tasks_config['cover_task']
    )
```

### 示例 3: 使用 Hierarchical 模式

修改 `crew.py`:

```python
@crew
def crew(self) -> Crew:
    return Crew(
        agents=self.agents,
        tasks=self.tasks,
        process=Process.hierarchical,  # 改为分层模式
        manager_llm="gpt-4",  # 指定管理者的 LLM
        verbose=True,
    )
```

在分层模式下，会创建一个 Manager Agent 来协调其他 Agent。

### 示例 4: 添加新工具

**步骤 1**: 在 `tools/custom_tool.py` 中创建

```python
class StoryThemeAnalyzer(BaseTool):
    name: str = "主题分析器"
    description: str = "分析故事的核心主题"
    args_schema: Type[BaseModel] = TextInput

    def _run(self, text: str) -> str:
        # 实现分析逻辑
        return f"主题分析结果..."
```

**步骤 2**: 导出工具

在 `tools/__init__.py`:

```python
from .custom_tool import StoryThemeAnalyzer

__all__ = ["StoryThemeAnalyzer"]
```

**步骤 3**: 在 Agent 中使用

在 `crew.py`:

```python
from story_writer_crew.tools import StoryThemeAnalyzer

@agent
def story_editor(self) -> Agent:
    return Agent(
        config=self.agents_config['story_editor'],
        tools=[StoryThemeAnalyzer()],
    )
```

---

## 常见问题

### Q1: 如何调整生成内容的长度？

**方法 1**: 在 `tasks.yaml` 中明确指定

```yaml
writing_task:
  description: >
    撰写一篇 2000-3000 字的故事...
  expected_output: >
    一篇完整的故事，长度约 2000-3000 字...
```

**方法 2**: 在 Agent 的 backstory 中强调

```yaml
story_writer:
  backstory: >
    你擅长创作简洁有力的短篇故事，
    通常在 2000 字左右完成叙述...
```

### Q2: 如何让输出更符合特定风格？

在 Agent 配置中使用具体的风格描述：

```yaml
story_writer:
  role: 海明威风格的作家
  goal: 用简洁、硬朗的风格撰写故事
  backstory: >
    你模仿海明威的写作风格：
    - 短句为主
    - 避免形容词堆砌
    - 对话简洁有力
    - 注重动作和细节
```

### Q3: 任务失败了怎么办？

启用详细日志查看问题：

```python
result = crew.kickoff(
    inputs=inputs,
    verbose=True  # 显示详细过程
)
```

常见原因：
- API 密钥未配置或无效
- 网络连接问题
- Task 描述不够清晰
- Agent 配置冲突

### Q4: 如何控制成本？

```python
# 使用更便宜的模型
@agent
def story_writer(self) -> Agent:
    return Agent(
        config=self.agents_config['story_writer'],
        llm="gpt-4o-mini",  # 使用便宜的模型
        max_iter=10,  # 限制最大迭代次数
        max_execution_time=120,  # 限制执行时间（秒）
    )
```

### Q5: 能否使用本地模型？

可以！配置 Ollama 或其他本地模型：

```python
@agent
def story_writer(self) -> Agent:
    return Agent(
        config=self.agents_config['story_writer'],
        llm="ollama/llama3",  # 使用本地 Ollama
    )
```

---

## 进阶技巧

### 1. 使用 Human Input

在 `tasks.yaml` 中添加人工审核：

```yaml
editing_task:
  description: "审核并编辑故事"
  human_input: true  # 需要人工确认后继续
```

### 2. 条件任务

创建条件任务，根据条件执行：

```python
from crewai.tasks import ConditionalTask

quality_check = ConditionalTask(
    condition=lambda output: "优秀" in output,
    tasks=[publish_task],  # 条件满足时执行
    else_tasks=[revise_task]  # 不满足时执行
)
```

### 3. 异步执行

```python
result = await crew.kickoff_async(inputs=inputs)
```

---

希望这份指南帮助你更好地使用故事创作团队！如有问题，请参考 [CrewAI 官方文档](https://docs.crewai.com)。
