# CrewAI 动态创建能力分析

## 1. 支持动态创建的组件

| 组件 | 动态创建 | 使用方式 |
|------|---------|---------|
| Agent | ✅ 完全支持 | `Agent(role="...", goal="...")` |
| Task | ✅ 完全支持 | `Task(description="...", agent=agent)` |
| Crew | ✅ 完全支持 | `Crew(agents=[...], tasks=[...])` |
| Flow | ❌ 受限 | 必须用装饰器，不能运行时动态添加 |

## 2. Agent 动态创建

```python
from crewai import Agent

# 方式一：直接实例化
agent = Agent(
    role="Senior Researcher",
    goal="Uncover cutting-edge developments in AI",
    backstory="You're a seasoned researcher...",
    verbose=True,
    allow_delegation=True,
    llm="gpt-4",
    tools=[search_tool, analysis_tool]
)

# 方式二：从字典动态创建
agent_config = {
    "role": "Senior Researcher",
    "goal": "Uncover cutting-edge developments in AI",
    "backstory": "You're a seasoned researcher...",
    "verbose": True,
    "allow_delegation": True
}
agent = Agent(**agent_config)

# 方式三：从 YAML/JSON 配置
import yaml
with open("agents.yaml") as f:
    configs = yaml.safe_load(f)
    agents = [Agent(**cfg) for cfg in configs["agents"]]
```

## 3. Task 动态创建

```python
from crewai import Task

# 直接创建
task = Task(
    description="Research about {topic}",
    expected_output="A detailed report about {topic}",
    agent=agent,
    async_execution=False,
    human_input=False
)

# 批量创建
task_configs = [
    {"description": "Task 1", "agent": agent1},
    {"description": "Task 2", "agent": agent2},
]
tasks = [Task(**cfg) for cfg in task_configs]
```

## 4. Crew 动态创建

```python
from crewai import Crew, Agent, Task

# 完全动态创建
def create_crew_from_config(config):
    # 动态创建 Agents
    agents = []
    for agent_cfg in config["agents"]:
        agent = Agent(**agent_cfg)
        agents.append(agent)

    # 动态创建 Tasks
    tasks = []
    for task_cfg in config["tasks"]:
        agent = next(a for a in agents if a.role == task_cfg["agent"])
        task = Task(
            description=task_cfg["description"],
            expected_output=task_cfg["expected_output"],
            agent=agent
        )
        tasks.append(task)

    # 创建 Crew
    crew = Crew(
        agents=agents,
        tasks=tasks,
        process=config.get("process", "sequential"),
        verbose=True
    )
    return crew
```

## 5. 配置驱动创建

```python
import yaml
from crewai import Crew, Agent, Task

def load_crew_from_yaml(yaml_path):
    with open(yaml_path) as f:
        config = yaml.safe_load(f)

    # 创建 agent 映射
    agents = {}
    for agent_cfg in config["agents"]:
        agent = Agent(**agent_cfg)
        agents[agent.role] = agent

    # 创建 tasks
    tasks = []
    for task_cfg in config["tasks"]:
        agent = agents[task_cfg["agent"]]
        task = Task(
            description=task_cfg["description"],
            expected_output=task_cfg["expected_output"],
            agent=agent
        )
        tasks.append(task)

    # 创建 crew
    return Crew(
        agents=list(agents.values()),
        tasks=tasks,
        process=config.get("process", "sequential")
    )
```

## 6. 运行时动态修改

```python
# 创建 Crew
crew = Crew(agents=[agent1, agent2], tasks=[task1, task2])

# 运行时添加新 Agent
new_agent = Agent(role="Editor", goal="Edit content", backstory="...")
crew.agents.append(new_agent)

# 运行时添加新 Task
new_task = Task(
    description="Edit the article",
    expected_output="Polished article",
    agent=new_agent
)
crew.tasks.append(new_task)

# 运行时修改流程
crew.process = Process.hierarchical
```

## 7. Flow 的限制

**❌ Flow 不支持完全动态创建**

```python
# Flow 必须使用装饰器定义
from crewai.flow import Flow

@Flow
class MyFlow:
    @start()
    def begin(self):
        return "Start"

    @listen(begin)
    def handle_begin(self):
        return "Process"
```

**无法在运行时动态添加监听器或路由**
