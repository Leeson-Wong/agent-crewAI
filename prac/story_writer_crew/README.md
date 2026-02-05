# 故事创作团队 (Story Writer Crew)

一个基于 CrewAI 的多智能体故事创作系统，通过协作完成从构思到编辑的完整故事创作流程。

## 🎭 功能特点

- **多 Agent 协作**：三个专业角色（策划师、作家、编辑）协同工作
- **完整创作流程**：从故事大纲 → 正文撰写 → 编辑润色
- **自定义工具**：包含字数统计、风格分析等实用工具
- **配置驱动**：使用 YAML 文件轻松配置 Agent 和 Task
- **多种运行模式**：单次运行、REPL 交互模式等

## 📁 项目结构

```
story_writer_crew/
├── .gitignore              # Git 忽略文件
├── .env.example            # 环境变量示例
├── pyproject.toml          # 项目配置
├── README.md               # 项目说明
│
└── src/story_writer_crew/
    ├── __init__.py         # 包初始化
    ├── main.py             # 程序入口
    ├── crew.py             # Crew 定义
    │
    ├── config/             # 配置文件
    │   ├── agents.yaml     # Agent 配置
    │   └── tasks.yaml      # Task 配置
    │
    └── tools/              # 自定义工具
        ├── __init__.py
        └── custom_tool.py  # 工具实现
```

## 🚀 快速开始

### 1. 安装依赖

```bash
# 确保已安装 CrewAI
pip install crewai crewai-tools

# 或使用 uv
uv pip install crewai crewai-tools
```

### 2. 配置环境变量

```bash
# 复制环境变量示例文件
cp .env.example .env

# 编辑 .env 文件，填入你的 API 密钥
# OPENAI_API_KEY=sk-your-key-here
```

### 3. 运行示例

```bash
# 方式1：使用 Python 直接运行
cd src/story_writer_crew
python main.py

# 方式2：使用 crewai CLI（需要先安装）
crewai run

# 方式3：REPL 交互模式
python main.py repl
```

## 📝 使用示例

### 单次运行

```python
from story_writer_crew.crew import StoryWriterCrew

# 创建 Crew 实例
story_crew = StoryWriterCrew()

# 定义输入
inputs = {
    'theme': '时间旅行与遗憾'
}

# 执行
result = story_crew.crew().kickoff(inputs=inputs)
print(result.raw)
```

### REPL 交互模式

```bash
python main.py repl
```

然后你可以：
```
🎨 请输入故事主题（或 quit 退出）: 科幻冒险
📝 正在创作主题：科幻冒险 的故事...
[创作过程...]
✅ 创作完成！

🎨 请输入故事主题（或 quit 退出）: 奇幻世界
...
```

## 🔧 配置说明

### agents.yaml - Agent 配置

```yaml
story_ideator:
  role: 创意故事策划师
  goal: 根据 {theme} 主题创作故事大纲
  backstory: 你是一位充满想象力的故事策划师...
```

### tasks.yaml - Task 配置

```yaml
outline_task:
  description: 基于 {theme} 创作故事大纲...
  expected_output: 一个结构完整的故事大纲...
  agent: story_ideator
```

## 🛠️ 自定义工具

项目包含三个自定义工具：

1. **WordCountTool** - 字数统计
2. **StyleAnalysisTool** - 写作风格分析
3. **WritingPromptTool** - 写作提示生成器

在 `crew.py` 中使用：

```python
from story_writer_crew.tools import WordCountTool

@agent
def story_writer(self) -> Agent:
    return Agent(
        config=self.agents_config['story_writer'],
        tools=[WordCountTool()],
    )
```

## 🎯 执行流程

```
1. Story Ideator (故事策划师)
   └─> 创建故事大纲

2. Story Writer (小说作家)
   └─> 撰写完整故事
       └─> 使用 WordCountTool 检查字数
       └─> 使用 StyleAnalysisTool 分析风格

3. Story Editor (文学编辑)
   └─> 编辑润色
       └─> 使用 StyleAnalysisTool 优化表达
       └─> 生成最终版本
```

## 📊 输出文件

执行后会生成以下文件：

- `story_draft.md` - 故事草稿
- `story_final.md` - 最终版本

## 🔍 高级用法

### 修改 Agent 配置

编辑 `config/agents.yaml`：

```yaml
story_writer:
  role: 专业小说作家
  goal: 撰写引人入胜的故事
  backstory: 你是一位获得过文学奖的作家...
```

### 添加新工具

1. 在 `tools/custom_tool.py` 中定义：

```python
class MyCustomTool(BaseTool):
    name: str = "我的工具"
    description: str = "工具描述"
    args_schema: Type[BaseModel] = MyInput

    def _run(self, arg1: str) -> str:
        return f"处理结果：{arg1}"
```

2. 在 `tools/__init__.py` 中导出

3. 在 `crew.py` 中使用

### 修改任务流程

编辑 `config/tasks.yaml`，调整 `context` 参数改变任务依赖关系：

```yaml
writing_task:
  context: [outline_task]  # 依赖 outline_task
```

## 🐛 调试技巧

启用详细输出：

```python
result = story_crew.crew().kickoff(
    inputs=inputs,
    verbose=True  # 显示详细执行过程
)
```

## 📚 相关资源

- [CrewAI 官方文档](https://docs.crewai.com)
- [CrewAI GitHub](https://github.com/crewAIInc/crewAI)
- [CrewAI 示例项目](https://github.com/crewAIInc/crewAI-examples)

## 📄 许可证

MIT License

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

---

**提示**：首次运行前，请确保已正确配置 `.env` 文件中的 API 密钥。
