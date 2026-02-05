# CrewAI Hooks 机制详解

## 1. Hooks 类型

| Hook 类型 | 触发时机 | 功能 |
|-----------|---------|------|
| **`@before_llm_call`** | LLM 调用前 | 修改消息、阻止执行 |
| **`@after_llm_call`** | LLM 调用后 | 修改响应、记录日志 |
| **`@before_tool_call`** | 工具调用前 | 修改输入、阻止执行 |
| **`@after_tool_call`** | 工具调用后 | 修改输出、记录结果 |

## 2. 基本用法

### LLM Hooks

```python
from crewai import Agent, Task, Crew
from crewai.hooks import before_llm_call, after_llm_call

@before_llm_call
def log_llm_calls(context):
    """记录所有 LLM 调用"""
    print(f"LLM call by {context.agent.role}")
    print(f"Iterations: {context.iterations}")
    return None

@after_llm_call
def sanitize_response(context):
    """清理敏感信息"""
    if context.response and "SECRET" in context.response:
        return context.response.replace("SECRET", "[REDACTED]")
    return None

agent = Agent(role="Assistant", goal="Help users")
task = Task(description="Say hello", agent=agent)
crew = Crew(agents=[agent], tasks=[task])
result = crew.kickoff()
```

### Tool Hooks

```python
from crewai.hooks import before_tool_call, after_tool_call

@before_tool_call
def log_tool_usage(context):
    print(f"Tool: {context.tool_name}")
    return None

@after_tool_call
def log_results(context):
    print(f"Result: {context.tool_result[:100]}")
    return None
```

## 3. 过滤 Hooks（高级功能）

### 按 Agent 过滤

```python
@before_llm_call(agents=["Researcher", "Analyst"])
def log_specific_agents(context):
    """只记录特定 Agent"""
    print(f"Filtered LLM call: {context.agent.role}")
    return None
```

### 按 Tool 过滤

```python
@before_tool_call(tools=["delete_file", "execute_code"])
def approve_dangerous(context):
    """危险工具需要人工确认"""
    response = context.request_human_input(
        prompt=f"⚠️  Allow {context.tool_name}?",
        default_message="Type 'yes' to approve:"
    )
    if response.lower() != "yes":
        return False  # 阻止执行
    return None
```

### 组合过滤

```python
@before_tool_call(tools=["write_file"], agents=["Developer"])
def approve_dev_writes(context):
    """只有 Developer 写文件时需要审批"""
    return None
```

## 4. Hook Context 对象

### LLMCallHookContext

```python
class LLMCallHookContext:
    executor: CrewAgentExecutor | LiteAgent | None
    messages: list[LLMMessage]      # 可变列表，可就地修改
    agent: Agent                     # 当前 Agent
    task: Task                       # 当前 Task
    crew: Crew                       # 当前 Crew
    llm: BaseLLM                     # LLM 实例
    iterations: int                  # 当前迭代次数
    response: str | None             # LLM 响应（仅 after hooks）

    def request_human_input(self, prompt, default_message):
        """请求人工输入"""
```

### ToolCallHookContext

```python
class ToolCallHookContext:
    tool_name: str
    tool_input: dict[str, Any]      # 可变字典，可就地修改
    tool: CrewStructuredTool         # 工具实例
    agent: Agent                     # 执行工具的 Agent
    task: Task                       # 当前 Task
    crew: Crew                       # 当前 Crew
    tool_result: str | None          # 工具结果（仅 after hooks）

    def request_human_input(self, prompt, default_message):
        """请求人工输入"""
```

## 5. 实际应用示例

### 安全审计

```python
@before_llm_call
def audit_log(context):
    """记录所有 LLM 调用"""
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "agent": context.agent.role,
        "iterations": context.iterations
    }
    with open("audit_log.jsonl", "a") as f:
        f.write(json.dumps(log_entry) + "\n")
    return None

@before_tool_call(tools=["delete_file", "execute_code"])
def security_gate(context):
    """危险工具需要二次确认"""
    approval = context.request_human_input(
        prompt="Approve this tool call?",
        default_message="Type 'approve' to continue:"
    )
    return approval.lower() == "approve"
```

### 成本控制

```python
@before_llm_call
def limit_iterations(context):
    """限制最大迭代次数"""
    if context.iterations >= 10:
        print("⚠️  Max iterations reached!")
        return False  # 阻止执行
    return None

@after_llm_call
def track_tokens(context):
    """统计 token 使用"""
    input_tokens = sum(len(str(msg.content)) for msg in context.messages) // 4
    output_tokens = len(context.response) // 4 if context.response else 0
    print(f"💰 Tokens: {input_tokens} + {output_tokens} = {input_tokens + output_tokens}")
    return None
```

### 内容过滤

```python
@after_llm_call
def filter_sensitive_content(context):
    """过滤敏感内容"""
    if not context.response:
        return None

    sensitive_words = ["API_KEY", "SECRET", "PASSWORD"]
    filtered_response = context.response

    for word in sensitive_words:
        if word in filtered_response:
            filtered_response = filtered_response.replace(word, f"[REDACTED]")

    return filtered_response
```

### 动态修改消息

```python
@before_llm_call
def inject_system_prompt(context):
    """动态注入系统提示"""
    from crewai.utilities.types import LLMMessage

    system_message = LLMMessage(
        role="system",
        content="IMPORTANT: Always respond in JSON format."
    )

    context.messages.insert(0, system_message)
    return None

@before_llm_call(agents=["Researcher"])
def enhance_researcher_context(context):
    """为特定 Agent 添加额外上下文"""
    from crewai.utilities.types import LLMMessage

    enhancement = LLMMessage(
        role="user",
        content="\n\nRemember to cite your sources!"
    )

    context.messages.append(enhancement)
    return None
```

## 6. 与 Claude Hooks 对比

| 特性 | CrewAI | Claude |
|------|--------|-------|
| LLM 调用前 Hook | ✅ `@before_llm_call` | ✅ `on_before_llm_call` |
| LLM 调用后 Hook | ✅ `@after_llm_call` | ✅ `on_after_llm_call` |
| 工具调用前 Hook | ✅ `@before_tool_call` | ✅ `on_before_tool_use` |
| 工具调用后 Hook | ✅ `@after_tool_call` | ✅ `on_after_tool_use` |
| Agent 过滤 | ✅ `agents=["..."]` | ⚠️ 手动判断 |
| Tool 过滤 | ✅ `tools=["..."]` | ⚠️ 手动判断 |
| 人工输入 | ✅ `request_human_input()` | ⚠️ 需要自己实现 |
| 修改消息 | ✅ 就地修改 `messages` | ✅ 就地修改 |
| 修改响应 | ✅ 返回新字符串 | ✅ 返回新字符串 |
| 阻止执行 | ✅ 返回 `False` | ✅ 抛出异常 |

## 7. 动态注册 Hooks

```python
from crewai.hooks import (
    register_before_llm_call_hook,
    unregister_before_llm_call_hook,
    clear_all_global_hooks
)

# 定义 hook
def my_llm_hook(context):
    print("Custom LLM hook")
    return None

# 注册
register_before_llm_call_hook(my_llm_hook)

# 使用
crew.kickoff()

# 注销
unregister_before_llm_call_hook(my_llm_hook)

# 清除所有
clear_all_global_hooks()
```

## 8. 推荐使用场景

- ✅ **安全审计**：记录所有 LLM 和工具调用
- ✅ **成本控制**：限制迭代次数、统计 token
- ✅ **内容过滤**：过滤敏感信息
- ✅ **人工审核**：危险操作需要人工确认
- ✅ **动态提示**：运行时修改系统提示
- ✅ **调试日志**：记录详细的执行过程
