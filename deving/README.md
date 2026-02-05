# CrewAI 研究笔记索引

本目录包含对 CrewAI 框架的深入研究笔记。

## 文档列表

1. **[架构分析](./01_crewai_architecture.md)**
   - 核心业务概念
   - 代码模块结构
   - 核心依赖关系
   - 需求到工程的映射

2. **[动态创建能力](./02_dynamic_creation.md)**
   - Agent/Task/Crew 的动态创建
   - 配置驱动创建
   - 运行时动态修改
   - Flow 的限制

3. **[人工审核机制](./03_human_review.md)**
   - Task 级别审核（human_input）
   - 输出护栏（guardrail）
   - Crew 钩子（@before_kickoff/@after_kickoff）
   - 自定义回调函数
   - Flow 级别审核
   - 分级审核策略

4. **[框架对比分析](./04_framework_comparison.md)**
   - 记忆能力对比（Letta vs 其他）
   - 协作能力对比（AutoGen vs CrewAI）
   - OpenClaw 的定位
   - 综合评分与选型建议

5. **[委派机制详解](./05_delegation_mechanism.md)**
   - allow_delegation 参数详解
   - 委派流程
   - 委派规则
   - 最佳实践
   - 应用场景

6. **[Hooks 机制](./06_hooks_system.md)**
   - 4 种 Hook 类型
   - 基本用法
   - 过滤 Hooks（按 Agent/Tool）
   - Hook Context 对象
   - 实际应用示例
   - 与 Claude Hooks 对比

## 核心要点

### CrewAI 的优势

1. **多 Agent 协作能力强**：仅次于 AutoGen，企业级应用首选
2. **记忆系统完善**：支持短期/长期/实体/知识库多种记忆
3. **Hooks 机制强大**：提供 4 种 Hook 类型，支持精细控制
4. **易用性优秀**：装饰器语法 + YAML 配置，学习曲线平缓
5. **动态创建灵活**：Agent/Task/Crew 完全支持动态创建

### 与其他框架对比

| 特性 | CrewAI | AutoGen | LangGraph | Letta |
|------|--------|---------|-----------|-------|
| **记忆能力** | 8/10 | 7/10 | 8.5/10 | 9.5/10 |
| **协作能力** | 9/10 | 10/10 | 8.5/10 | 7/10 |
| **易用性** | 8.5/10 | 7/10 | 6/10 | 9/10 |
| **企业级** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |

### 推荐使用场景

| 场景 | 推荐框架 |
|------|---------|
| 企业工作流 | CrewAI |
| 研发团队协作 | AutoGen |
| 复杂状态机 | LangGraph |
| 长期记忆需求 | Letta |
| 个人助理 | OpenClaw |

## 技术栈总结

### 核心依赖

```python
dependencies = [
    "pydantic~=2.11.9",           # 数据验证
    "openai>=1.83.0,<3",         # LLM 接口
    "instructor>=1.3.3",          # 结构化输出
    "chromadb~=1.1.0",            # 向量数据库
    "opentelemetry-api~=1.34.0",  # 遥测
]
```

### 开发环境

```bash
# 使用 conda
conda activate your_env
pip install -e lib/crewai
pip install -e lib/crewai-tools

# 使用 uv（推荐）
cd lib/crewai
uv sync
```

### 源码使用

```bash
# 直接使用源码
from crewai import Agent, Task, Crew

# 创建 Agent
agent = Agent(role="Assistant", goal="Help")

# 创建 Task
task = Task(description="Say hello", agent=agent)

# 创建 Crew
crew = Crew(agents=[agent], tasks=[task])

# 执行
result = crew.kickoff()
```

## 更新日志

- 2025-02-05: 初始版本，包含 6 个核心主题
