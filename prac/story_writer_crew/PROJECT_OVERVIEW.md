# 项目创建完成！

## ✅ 已创建的文件

```
prac/story_writer_crew/
│
├── .gitignore                  # Git 忽略配置
├── .env.example                # 环境变量示例
├── pyproject.toml              # 项目配置
├── README.md                   # 项目说明
├── USAGE_GUIDE.md              # 详细使用指南
├── PROJECT_OVERVIEW.md         # 本文件
│
└── src/story_writer_crew/      # 源代码目录
    │
    ├── __init__.py             # 包初始化
    ├── main.py                 # 程序入口（多种运行模式）
    ├── crew.py                 # Crew 定义（装饰器模式）
    │
    ├── config/                 # 配置文件
    │   ├── agents.yaml         # Agent 配置（3个 Agent）
    │   └── tasks.yaml          # Task 配置（3个 Task）
    │
    └── tools/                  # 自定义工具
        ├── __init__.py
        └── custom_tool.py      # 3个自定义工具
```

---

## 🎯 项目功能

这是一个**故事创作团队**，包含：

### 三个 Agent（智能体）
1. **Story Ideator** - 故事策划师：创作大纲
2. **Story Writer** - 小说作家：撰写故事
3. **Story Editor** - 文学编辑：润色优化

### 三个 Task（任务）
1. **outline_task** - 创作故事大纲
2. **writing_task** - 撰写完整故事（依赖 outline）
3. **editing_task** - 编辑润色（依赖 writing）

### 三个自定义工具
1. **WordCountTool** - 字数统计
2. **StyleAnalysisTool** - 写作风格分析
3. **WritingPromptTool** - 写作提示生成

---

## 🚀 快速开始

### 1. 安装依赖

```bash
pip install crewai crewai-tools
```

### 2. 配置环境

```bash
cp .env.example .env
# 编辑 .env 文件，添加你的 OPENAI_API_KEY
```

### 3. 运行项目

```bash
cd src/story_writer_crew
python main.py
```

或使用 REPL 交互模式：

```bash
python main.py repl
```

---

## 📖 核心文件说明

### main.py - 程序入口

提供多种运行方式：

```python
# 单次运行
python main.py

# REPL 交互模式
python main.py repl

# 训练模式
python main.py train

# 测试模式
python main.py test
```

### crew.py - Crew 定义

使用装饰器模式从 YAML 加载配置：

```python
@CrewBase
class StoryWriterCrew:
    @agent
    def story_ideator(self) -> Agent:
        return Agent(
            config=self.agents_config['story_ideator'],
            tools=[WritingPromptTool()],
        )

    @task
    def outline_task(self) -> Task:
        return Task(
            config=self.tasks_config['outline_task'],
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
        )
```

### config/agents.yaml - Agent 配置

```yaml
story_ideator:
  role: 创意故事策划师
  goal: 根据 {theme} 创作故事大纲
  backstory: 你是一位充满想象力的故事策划师...
```

### config/tasks.yaml - Task 配置

```yaml
outline_task:
  description: 基于 {theme} 创作故事大纲
  expected_output: 结构完整的故事大纲
  agent: story_ideator

writing_task:
  description: 根据大纲撰写故事
  agent: story_writer
  context: [outline_task]  # 依赖关系
  output_file: story_draft.md
```

---

## 🎓 学习要点

### 1. YAML + Python 的组合模式

- **配置文件** (YAML)：描述 Agent 和 Task 的"是什么"
- **代码文件** (Python)：定义"怎么做"

### 2. 装饰器的魔法

```python
@agent          # 自动创建 Agent 并添加到 self.agents
def story_ideator(self) -> Agent:
    return Agent(config=self.agents_config['...'])

@task           # 自动创建 Task 并添加到 self.tasks
def outline_task(self) -> Task:
    return Task(config=self.tasks_config['...'])

@crew           # 自动组装 Crew
def crew(self) -> Crew:
    return Crew(
        agents=self.agents,  # 自动收集
        tasks=self.tasks,    # 自动收集
    )
```

### 3. Task 依赖关系

```yaml
writing_task:
  context: [outline_task]  # 可以使用 outline_task 的输出
```

在执行时，`writing_task` 会自动获得 `outline_task` 的结果作为上下文。

### 4. 自定义工具

继承 `BaseTool` 并实现 `_run` 方法：

```python
class MyTool(BaseTool):
    name: str = "工具名称"
    description: str = "工具描述"
    args_schema: Type[BaseModel] = InputSchema

    def _run(self, arg1: str) -> str:
        return f"处理 {arg1}"
```

---

## 🔄 执行流程

```
用户输入: theme = "时间旅行与遗憾"
    ↓
┌─────────────────────────────────────────┐
│  Story Ideator (故事策划师)              │
│  - 使用 WritingPromptTool 生成创意       │
│  - 创作故事大纲                          │
│  - 输出: outline.md                     │
└─────────────────────────────────────────┘
    ↓ (传递上下文)
┌─────────────────────────────────────────┐
│  Story Writer (小说作家)                │
│  - 接收大纲作为上下文                    │
│  - 使用 WordCountTool 统计字数          │
│  - 撰写完整故事                          │
│  - 输出: story_draft.md                 │
└─────────────────────────────────────────┘
    ↓ (传递上下文)
┌─────────────────────────────────────────┐
│  Story Editor (文学编辑)                │
│  - 接收草稿作为上下文                    │
│  - 使用 StyleAnalysisTool 分析风格      │
│  - 编辑润色                              │
│  - 输出: story_final.md                 │
└─────────────────────────────────────────┘
    ↓
返回: CrewOutput (包含所有任务的输出)
```

---

## 💡 扩展建议

### 1. 添加更多 Agent

```yaml
# agents.yaml
cover_designer:
  role: 书籍封面设计师
  goal: 设计封面概念
```

### 2. 添加更多工具

```python
# tools/custom_tool.py
class CharacterNameGenerator(BaseTool):
    name: str = "角色名字生成器"
    description: str = "生成适合的角色名字"
    ...
```

### 3. 改用 Hierarchical 模式

```python
# crew.py
@crew
def crew(self) -> Crew:
    return Crew(
        agents=self.agents,
        tasks=self.tasks,
        process=Process.hierarchical,  # 改为分层
        manager_llm="gpt-4",
    )
```

### 4. 添加记忆功能

```python
# 已在 crew.py 中启用
memory=True  # Agent 会记住之前的内容
```

---

## 📚 下一步学习

1. **修改配置**：尝试修改 `agents.yaml` 和 `tasks.yaml`
2. **添加工具**：创建你自己的工具
3. **改变流程**：尝试 `Process.hierarchical`
4. **集成其他 LLM**：使用本地模型或其他 API
5. **查看官方示例**：[crewAI-examples](https://github.com/crewAIInc/crewAI-examples)

---

## 🎉 恭喜！

你已经创建了一个完整的 CrewAI 项目！这个项目展示了：

✅ CrewAI 的标准项目结构
✅ Agent、Task、Crew 的配置和使用
✅ YAML + Python 的组合模式
✅ 自定义工具的创建方法
✅ 任务依赖关系的设置
✅ 多种运行模式

现在你可以：
1. 运行这个示例项目
2. 修改配置，创建自己的 Crew
3. 探索 CrewAI 的更多功能

祝学习愉快！🚀
