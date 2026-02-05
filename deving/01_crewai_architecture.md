# CrewAI 架构分析

## 1. 核心业务概念

CrewAI 的核心概念包括：

- **Agent（智能体）**：具有角色、目标、背景故事的 AI 实体
- **Crew（团队）**：多个 Agent 的集合，定义协作方式
- **Task（任务）**：需要 Agent 执行的具体工作单元
- **Flow（流程）**：事件驱动的 workflow，提供精确执行控制
- **Tools（工具）**：Agent 可以使用的功能集合
- **LLM（语言模型）**：Agent 的大脑
- **Memory（记忆）**：Agent 和 Crew 的记忆系统
- **Process（过程）**：任务执行的流程控制（顺序、层次）
- **Delegation（委派）**：Agent 之间的任务转移和协作

## 2. 代码模块结构

```
src/crewai/
├── __init__.py                 # 主入口
├── agent/
│   ├── core.py                 # Agent 核心实现
│   └── utils.py
├── agents/
│   ├── agent_builder/
│   ├── cache/
│   └── crew_agent_executor.py
├── crew.py                     # Crew 核心实现
├── crews/
│   └── crew_output.py
├── flow/
│   └── flow.py                 # Flow 核心实现（123KB）
├── task.py                     # Task 核心实现
├── tasks/
│   ├── conditional_task.py
│   ├── llm_guardrail.py
│   └── task_output.py
├── tools/
│   ├── base_tool.py
│   └── agent_tools/
├── llms/
│   ├── base_llm.py
│   └── providers/
├── memory/                     # 记忆系统
│   ├── contextual/
│   ├── entity/
│   ├── long_term/
│   └── short_term/
├── knowledge/                  # 知识库系统
└── hooks/                      # Hooks 系统
```

## 3. 核心依赖关系

```
Crew (团队管理)
├── Agent (智能体)
│   ├── LLM (语言模型)
│   ├── Tools (工具)
│   ├── Memory (记忆)
│   └── Knowledge (知识)
├── Task (任务)
│   ├── Agent (执行者)
│   └── Tools (工具使用)
└── Process (执行流程)
    ├── Sequential (顺序执行)
    └── Hierarchical (层次执行)
```

## 4. 需求到工程的映射

| 业务概念 | 对应代码模块 | 文件路径 |
|---------|-------------|---------|
| Agent | `agent/core.py`, `agents/` | `src/crewai/agent/` |
| Crew | `crew.py`, `crews/` | `src/crewai/crew.py` |
| Task | `task.py`, `tasks/` | `src/crewai/task.py` |
| Flow | `flow/flow.py` | `src/crewai/flow/` |
| Tools | `tools/` | `src/crewai/tools/` |
| LLM | `llms/` | `src/crewai/llms/` |
| Memory | `memory/` | `src/crewai/memory/` |
| Knowledge | `knowledge/` | `src/crewai/knowledge/` |
| Process | `process.py` | `src/crewai/process.py` |
| Hooks | `hooks/` | `src/crewai/hooks/` |
