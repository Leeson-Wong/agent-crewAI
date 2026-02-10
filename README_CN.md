<p align="center">
  <a href="https://github.com/crewAIInc/crewAI">
    <img src="docs/images/crewai_logo.png" width="600px" alt="开源多智能体编排框架">
  </a>
</p>
<p align="center" style="display: flex; justify-content: center; gap: 20px; align-items: center;">
  <a href="https://trendshift.io/repositories/11239" target="_blank">
    <img src="https://trendshift.io/api/badge/repositories/11239" alt="crewAIInc%2FcrewAI | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/>
  </a>
</p>

<p align="center">
  <a href="https://crewai.com">官网</a>
  ·
  <a href="https://docs.crewai.com">文档</a>
  ·
  <a href="https://app.crewai.com">开始云试用</a>
  ·
  <a href="https://blog.crewai.com">博客</a>
  ·
  <a href="https://community.crewai.com">论坛</a>
</p>

<p align="center">
  <a href="https://github.com/crewAIInc/crewAI">
    <img src="https://img.shields.io/github/stars/crewAIInc/crewAI" alt="GitHub 仓库星标">
  </a>
  <a href="https://github.com/crewAIInc/crewAI/network/members">
    <img src="https://img.shields.io/github/forks/crewAIInc/crewAI" alt="GitHub 派生">
  </a>
  <a href="https://github.com/crewAIInc/crewAI/issues">
    <img src="https://img.shields.io/github/issues/crewAIInc/crewAI" alt="GitHub 问题">
  </a>
  <a href="https://github.com/crewAIInc/crewAI/pulls">
    <img src="https://img.shields.io/github/issues-pr/crewAIInc/crewAI" alt="GitHub 拉取请求">
  </a>
  <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="许可证: MIT">
  </a>
</p>

<p align="center">
  <a href="https://pypi.org/project/crewai/">
    <img src="https://img.shields.io/pypi/v/crewai" alt="PyPI 版本">
  </a>
  <a href="https://pypi.org/project/crewai/">
    <img src="https://img.shields.io/pypi/dm/crewai" alt="PyPI 下载量">
  </a>
  <a href="https://twitter.com/crewAIInc">
    <img src="https://img.shields.io/twitter/follow/crewAIInc?style=social" alt="Twitter 关注">
  </a>
</p>

### 快速灵活的多智能体自动化框架

> CrewAI 是一个精简、极速的 Python 框架，完全从零开始构建——**完全独立于 LangChain 或其他智能体框架**。
> 它为开发者提供高层简洁性和精确的低层控制，非常适合为任何场景创建自主 AI 智能体。

- **CrewAI Crews（智能体组）**：优化自主性和协作智能。
- **CrewAI Flows（流程）**：构建和部署多智能体系统的**企业级生产架构**。支持细粒度的事件驱动控制、单次 LLM 调用实现精确任务编排，并原生支持 Crews。

已有超过 100,000 名开发者通过 [learn.crewai.com](https://learn.crewai.com) 的社区课程获得认证，CrewAI 正迅速成为企业级 AI 自动化的标准。

# CrewAI AMP 套件

CrewAI AMP 套件是一个专为需要安全、可扩展且易于管理的智能体驱动自动化的组织定制的综合解决方案。

您可以免费试用套件的一部分 [Crew 控制平面](https://app.crewai.com)

## Crew 控制平面主要功能：

- **追踪与可观测性**：实时监控和跟踪您的 AI 智能体和工作流，包括指标、日志和追踪。
- **统一控制平面**：用于管理、监控和扩展 AI 智能体和工作流的集中平台。
- **无缝集成**：轻松连接现有企业系统、数据源和云基础设施。
- **高级安全**：内置强大的安全性和合规措施，确保安全部署和管理。
- **可操作的洞察**：实时分析和报告，以优化性能和决策。
- **24/7 支持**：专属企业支持，确保不间断运营和快速问题解决。
- **本地和云端部署选项**：根据安全性和合规要求，选择在本地或云端部署 CrewAI AMP。

CrewAI AMP 专为寻求强大、可靠解决方案的企业设计，可将复杂的业务流程转化为高效、智能的自动化。

## 目录

- [为什么选择 CrewAI？](#为什么选择-crewai)
- [快速入门](#快速入门)
- [核心功能](#核心功能)
- [理解 Flows 和 Crews](#理解-flows-和-crews)
- [CrewAI vs LangGraph](#crewai-与其他框架对比)
- [示例](#示例)
  - [快速教程](#快速教程)
  - [撰写职位描述](#撰写职位描述)
  - [旅行规划](#旅行规划)
  - [股票分析](#股票分析)
  - [结合使用 Crews 和 Flows](#结合使用-crews-和-flows)
- [连接模型](#连接您的-crew-到模型)
- [框架对比](#crewai-与其他框架对比)
- [常见问题 (FAQ)](#常见问题-faq)
- [贡献](#贡献)
- [遥测](#遥测)
- [许可证](#许可证)

## 为什么选择 CrewAI？

<div align="center" style="margin-bottom: 30px;">
  <img src="docs/images/asset.png" alt="CrewAI Logo" width="100%">
</div>

CrewAI 释放了多智能体自动化的真正潜力，通过 AI 智能体组或事件流程提供最佳的极速、灵活性和控制组合：

- **独立框架**：从零构建，独立于 LangChain 或任何其他智能体框架。
- **高性能**：针对速度和最小资源使用进行优化，实现更快的执行。
- **灵活的低层定制**：完全自由的高层和低层定制——从整体工作流和系统架构到细粒度的智能体行为、内部提示和执行逻辑。
- **适用于所有场景**：在简单任务和高度复杂的现实世界企业级场景中都 proven 有效。
- **强大的社区**：拥有超过 **100,000 名认证**开发者的快速增长社区支持，提供全面的支持和资源。

CrewAI 赋能开发者和企业自信地构建智能自动化，架起简洁性、灵活性和性能之间的桥梁。

## 快速入门

按照此教程设置并运行您的第一个 CrewAI 智能体。

[![CrewAI 快速入门教程](https://img.youtube.com/vi/-kSOTtYzgEw/hqdefault.jpg)](https://www.youtube.com/watch?v=-kSOTtYzgEw "CrewAI 快速入门教程")

###

学习资源

通过我们的综合课程学习 CrewAI：

- [Multi AI Agent Systems with CrewAI](https://www.deeplearning.ai/short-courses/multi-ai-agent-systems-with-crewai/) - 掌握多智能体系统的基础知识
- [Practical Multi AI Agents and Advanced Use Cases](https://www.deeplearning.ai/short-courses/practical-multi-ai-agents-and-advanced-use-cases-with-crewai/) - 深入高级实现

### 理解 Flows 和 Crews

CrewAI 提供两种强大的、互补的方法，可以无缝协作构建复杂的 AI 应用程序：

1. **Crews（智能体组）**：具有真正自主性和代理能力的 AI 智能体团队，通过基于角色的协作共同完成复杂任务。Crews 实现：

   - 智能体之间自然的、自主的决策
   - 动态任务委派和协作
   - 具有明确目标和专业知识的专业角色
   - 灵活的问题解决方法

2. **Flows（流程）**：生产就绪的、事件驱动的工作流，为复杂自动化提供精确控制。Flows 提供：

   - 对现实场景执行路径的细粒度控制
   - 任务之间安全、一致的状态管理
   - AI 智能体与生产 Python 代码的清晰集成
   - 复杂业务逻辑的条件分支

当结合 Crews 和 Flows 时，CrewAI 的真正力量就显现出来了。这种协同效应允许您：

- 构建复杂的生产级应用程序
- 平衡自主性与精确控制
- 处理复杂的现实场景
- 保持清晰、可维护的代码结构

### 安装入门

要开始使用 CrewAI，请按照以下简单步骤操作：

### 1. 安装

确保您的系统上安装了 Python >=3.10 <3.14。CrewAI 使用 [UV](https://docs.astral.sh/uv/) 进行依赖管理和包处理，提供无缝的设置和执行体验。

首先，安装 CrewAI：

```shell
uv pip install crewai
```

如果您想安装 'crewai' 包及其包含智能体额外工具的可选功能，可以使用以下命令：

```shell
uv pip install 'crewai[tools]'
```

上述命令安装基本包，还添加了需要更多依赖才能运行的额外组件。

### 依赖问题排查

如果在安装或使用过程中遇到问题，以下是一些常见解决方案：

#### 常见问题

1. **ModuleNotFoundError: No module named 'tiktoken'**

   - 显式安装 tiktoken：`uv pip install 'crewai[embeddings]'`
   - 如果使用 embedchain 或其他工具：`uv pip install 'crewai[tools]'`

2. **Failed building wheel for tiktoken**

   - 确保安装了 Rust 编译器（参见上面的安装步骤）
   - 对于 Windows：验证是否安装了 Visual C++ 构建工具
   - 尝试升级 pip：`uv pip install --upgrade pip`
   - 如果问题仍然存在，使用预构建的 wheel：`uv pip install tiktoken --prefer-binary`

### 2. 使用 YAML 配置设置您的 Crew

要创建新的 CrewAI 项目，请运行以下 CLI（命令行界面）命令：

```shell
crewai create crew <project_name>
```

此命令创建一个具有以下结构的新项目文件夹：

```
my_project/
├── .gitignore
├── pyproject.toml
├── README.md
├── .env
└── src/
    └── my_project/
        ├── __init__.py
        ├── main.py
        ├── crew.py
        ├── tools/
        │   ├── custom_tool.py
        │   └── __init__.py
        └── config/
            ├── agents.yaml
            └── tasks.yaml
```

现在您可以通过编辑 `src/my_project` 文件夹中的文件开始开发您的 crew。`main.py` 文件是项目的入口点，`crew.py` 文件是定义 crew 的地方，`agents.yaml` 文件是定义智能体的地方，`tasks.yaml` 文件是定义任务的地方。

#### 要自定义您的项目，您可以：

- 修改 `src/my_project/config/agents.yaml` 来定义您的智能体。
- 修改 `src/my_project/config/tasks.yaml` 来定义您的任务。
- 修改 `src/my_project/crew.py` 来添加您自己的逻辑、工具和特定参数。
- 修改 `src/my_project/main.py` 来为智能体和任务添加自定义输入。
- 将环境变量添加到 `.env` 文件中。

#### 具有顺序流程的简单 crew 示例：

实例化您的 crew：

```shell
crewai create crew latest-ai-development
```

根据需要修改文件以适应您的用例：

**agents.yaml**

```yaml
# src/my_project/config/agents.yaml
researcher:
  role: >
    {topic} 高级数据研究员
  goal: >
    揭示 {topic} 的前沿发展
  backstory: >
    您是一名经验丰富的研究员，擅长发现 {topic} 的最新
    发展。您以能够找到最相关的信息并以清晰简洁的方式呈现而闻名。

reporting_analyst:
  role: >
    {topic} 报告分析师
  goal: >
    根据 {topic} 数据分析和研究结果创建详细报告
  backstory: >
    您是一名一丝不苟的分析师，对细节有敏锐的眼光。您以
    将复杂数据转化为清晰简洁的报告而闻名，使其他人容易理解
    并根据您提供的信息采取行动。
```

**tasks.yaml**

````yaml
# src/my_project/config/tasks.yaml
research_task:
  description: >
    对 {topic} 进行彻底研究
    确保找到任何有趣和相关的信息，考虑到当前年份是 2025 年。
  expected_output: >
    包含关于 {topic} 最相关信息的 10 个要点的列表
  agent: researcher

reporting_task:
  description: >
    审查您获得的上下文，并将每个主题扩展为报告的完整章节。
    确保报告详细并包含任何和所有相关信息。
  expected_output: >
    一份完整的报告，包含主要主题，每个主题都有完整的信息章节。
    格式为 markdown，不使用 '```'
  agent: reporting_analyst
  output_file: report.md
````

**crew.py**

```python
# src/my_project/crew.py
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

@CrewBase
class LatestAiDevelopmentCrew():
	"""LatestAiDevelopment crew"""
	agents: List[BaseAgent]
	tasks: List[Task]

	@agent
	def researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['researcher'],
			verbose=True,
			tools=[SerperDevTool()]
		)

	@agent
	def reporting_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['reporting_analyst'],
			verbose=True
		)

	@task
	def research_task(self) -> Task:
		return Task(
			config=self.tasks_config['research_task'],
		)

	@task
	def reporting_task(self) -> Task:
		return Task(
			config=self.tasks_config['reporting_task'],
			output_file='report.md'
		)

	@crew
	def crew(self) -> Crew:
		"""创建 LatestAiDevelopment crew"""
		return Crew(
			agents=self.agents, # 由 @agent 装饰器自动创建
			tasks=self.tasks, # 由 @task 装饰器自动创建
			process=Process.sequential,
			verbose=True,
		)
```

**main.py**

```python
#!/usr/bin/env python
# src/my_project/main.py
import sys
from latest_ai_development.crew import LatestAiDevelopmentCrew

def run():
    """
    运行 crew。
    """
    inputs = {
        'topic': 'AI 智能体'
    }
    LatestAiDevelopmentCrew().crew().kickoff(inputs=inputs)
```

### 3. 运行您的 Crew

在运行 crew 之前，请确保在 `.env` 文件中将以下密钥设置为环境变量：

- [OpenAI API 密钥](https://platform.openai.com/account/api-keys)（或其他 LLM API 密钥）：`OPENAI_API_KEY=sk-...`
- [Serper.dev](https://serper.dev/) API 密钥：`SERPER_API_KEY=YOUR_KEY_HERE`

使用 CLI 命令锁定依赖并安装它们，但首先导航到您的项目目录：

```shell
cd my_project
crewai install (可选)
```

要运行您的 crew，请在项目根目录执行以下命令：

```bash
crewai run
```

或

```bash
python src/my_project/main.py
```

如果由于使用 poetry 而发生错误，请运行以下命令来更新您的 crewai 包：

```bash
crewai update
```

您应该会在控制台中看到输出，并且应该在项目根目录中创建 `report.md` 文件，其中包含完整的最终报告。

除了顺序流程外，您还可以使用分层流程，它会自动为定义的 crew 分配一个管理员，通过委派和验证结果来正确协调任务的规划和执行。[在此处查看有关流程的更多信息](https://docs.crewai.com/core-concepts/Processes/)。

## 核心功能

CrewAI 作为一个精简、独立、高性能的多 AI 智能体框架脱颖而出，提供简洁性、灵活性和精确控制——摆脱了其他智能体框架中发现的复杂性和限制。

- **独立且精简**：完全独立于 LangChain 等其他框架，提供更快的执行速度和更轻的资源需求。
- **灵活且精确**：通过直观的 [Crews](https://docs.crewai.com/concepts/crews) 或精确的 [Flows](https://docs.crewai.com/concepts/flows) 轻松编排自主智能体，实现完美平衡以满足您的需求。
- **无缝集成**：轻松结合 Crews（自主性）和 Flows（精确性）以创建复杂的现实世界自动化。
- **深度定制**：定制每个方面——从高层工作流到低层内部提示和智能体行为。
- **可靠性能**：在简单任务和复杂的企业级自动化中提供一致的结果。
- **繁荣的社区**：拥有强大的文档和超过 100,000 名认证开发者，提供非凡的支持和指导。

选择 CrewAI 轻松构建强大、灵活且生产就绪的 AI 自动化。

## 示例

您可以在 [CrewAI-examples 仓库](https://github.com/crewAIInc/crewAI-examples?tab=readme-ov-file)中测试不同的 AI crews 现实示例：

- [落地页生成器](https://github.com/crewAIInc/crewAI-examples/tree/main/crews/landing_page_generator)
- [在执行过程中进行人工输入](https://docs.crewai.com/how-to/Human-Input-on-Execution)
- [旅行规划](https://github.com/crewAIInc/crewAI-examples/tree/main/crews/trip_planner)
- [股票分析](https://github.com/crewAIInc/crewAI-examples/tree/main/crews/stock_analysis)

### 快速教程

[![CrewAI 教程](https://img.youtube.com/vi/tnejrr-0a94/maxresdefault.jpg)](https://www.youtube.com/watch?v=tnejrr-0a94 "CrewAI 教程")

### 撰写职位描述

[查看此示例的代码](https://github.com/crewAIInc/crewAI-examples/tree/main/crews/job-posting)或观看下面的视频：

[![职位发布](https://img.youtube.com/vi/u98wEMz-9to/maxresdefault.jpg)](https://www.youtube.com/watch?v=u98wEMz-9to "职位发布")

### 旅行规划

[查看此示例的代码](https://github.com/crewAIInc/crewAI-examples/tree/main/crews/trip_planner)或观看下面的视频：

[![旅行规划](https://img.youtube.com/vi/xis7rWp-hjs/maxresdefault.jpg)](https://www.youtube.com/watch?v=xis7rWp-hjs "旅行规划")

### 股票分析

[查看此示例的代码](https://github.com/crewAIInc/crewAI-examples/tree/main/crews/stock_analysis)或观看下面的视频：

[![股票分析](https://img.youtube.com/vi/e0Uj4yWdaAg/maxresdefault.jpg)](https://www.youtube.com/watch?v=e0Uj4yWdaAg "股票分析")

### 结合使用 Crews 和 Flows

当结合 Crews 和 Flows 创建复杂的自动化管道时，CrewAI 的真正力量就显现出来了。CrewAI flows 支持逻辑运算符，如 `or_` 和 `and_` 来组合多个条件。这可以与 `@start`、`@listen` 或 `@router` 装饰器一起使用，以创建复杂的触发条件。

- `or_`：当满足任何指定条件时触发。
- `and_`：当满足所有指定条件时触发。

以下是如何在 Flow 中编排多个 Crews：

```python
from crewai.flow.flow import Flow, listen, start, router, or_
from crewai import Crew, Agent, Task, Process
from pydantic import BaseModel

# 定义结构化状态以实现精确控制
class MarketState(BaseModel):
    sentiment: str = "neutral"
    confidence: float = 0.0
    recommendations: list = []

class AdvancedAnalysisFlow(Flow[MarketState]):
    @start()
    def fetch_market_data(self):
        # 通过结构化状态展示低层控制
        self.state.sentiment = "analyzing"
        return {"sector": "tech", "timeframe": "1W"}  # 这些参数与任务描述模板匹配

    @listen(fetch_market_data)
    def analyze_with_crew(self, market_data):
        # 通过专业角色展示 crew 代理能力
        analyst = Agent(
            role="高级市场分析师",
            goal="进行具有专业见解的深入市场分析",
            backstory="您是一名资深分析师，以识别微妙的市场模式而闻名"
        )
        researcher = Agent(
            role="数据研究员",
            goal="收集和验证支持性市场数据",
            backstory="您擅长查找和关联多个数据源"
        )

        analysis_task = Task(
            description="分析过去 {timeframe} 的 {sector} 行业数据",
            expected_output="具有置信度分数的详细市场分析",
            agent=analyst
        )
        research_task = Task(
            description="查找支持性数据以验证分析",
            expected_output="佐证证据和潜在矛盾",
            agent=researcher
        )

        # 展示 crew 自主性
        analysis_crew = Crew(
            agents=[analyst, researcher],
            tasks=[analysis_task, research_task],
            process=Process.sequential,
            verbose=True
        )
        return analysis_crew.kickoff(inputs=market_data)  # 将 market_data 作为命名输入传递

    @router(analyze_with_crew)
    def determine_next_steps(self):
        # 通过条件路由展示流程控制
        if self.state.confidence > 0.8:
            return "high_confidence"
        elif self.state.confidence > 0.5:
            return "medium_confidence"
        return "low_confidence"

    @listen("high_confidence")
    def execute_strategy(self):
        # 展示复杂决策
        strategy_crew = Crew(
            agents=[
                Agent(role="策略专家",
                      goal="制定最优市场策略")
            ],
            tasks=[
                Task(description="基于分析创建详细策略",
                     expected_output="分步行动计划")
            ]
        )
        return strategy_crew.kickoff()

    @listen(or_("medium_confidence", "low_confidence"))
    def request_additional_analysis(self):
        self.state.recommendations.append("收集更多数据")
        return "需要额外分析"
```

此示例演示了如何：

1. 使用 Python 代码进行基本数据操作
2. 创建和执行 Crews 作为工作流中的步骤
3. 使用 Flow 装饰器管理操作序列
4. 基于 Crew 结果实现条件分支

## 连接您的 Crew 到模型

CrewAI 支持通过各种连接选项使用各种 LLM。默认情况下，您的智能体在查询模型时将使用 OpenAI API。但是，还有其他几种方式允许您的智能体连接到模型。例如，您可以配置智能体通过 Ollama 工具使用本地模型。

请参阅 [Connect CrewAI to LLMs](https://docs.crewai.com/how-to/LLM-Connections/) 页面，了解有关配置智能体与模型连接的详细信息。

## CrewAI 与其他框架对比

**CrewAI 的优势**：CrewAI 通过其独特的 Crews 和 Flows 架构，将自主智能体智能与精确的工作流控制相结合。该框架在高层编排和低层定制方面都表现出色，能够实现具有细粒度控制的复杂、生产级系统。

- **LangGraph**：虽然 LangGraph 为构建智能体工作流提供了基础，但其方法需要大量样板代码和复杂的状态管理模式。该框架与 LangChain 的紧密耦合可能在实现自定义智能体行为或与外部系统集成时限制灵活性。

_P.S. CrewAI 在某些情况下（如此 QA 任务示例）展示了比 LangGraph 显著的性能优势，执行速度快 5.76 倍（[查看比较](https://github.com/crewAIInc/crewAI-examples/tree/main/Notebooks/CrewAI%20Flows%20%26%20Langgraph/QA%20Agent)），同时在某些编码任务中实现更高的评估分数和更快的完成时间，如此示例所示（[详细分析](https://github.com/crewAIInc/crewAI-examples/blob/main/Notebooks/CrewAI%20Flows%20%26%20Langgraph/Coding%20Assistant/coding_assistant_eval.ipynb)）。_

- **Autogen**：虽然 Autogen 擅长创建能够协同工作的对话式智能体，但它缺乏固有的流程概念。在 Autogen 中，编排智能体的交互需要额外的编程，随着任务规模的扩大，这可能会变得复杂和繁琐。
- **ChatDev**：ChatDev 将流程的概念引入了 AI 智能体领域，但其实现相当僵化。ChatDev 中的定制是有限的，不是面向生产环境的，这可能会阻碍现实应用程序中的可扩展性和灵活性。

## 贡献

CrewAI 是开源的，我们欢迎贡献。如果您想做出贡献，请：

- 派生仓库。
- 为您的功能创建一个新分支。
- 添加您的功能或改进。
- 发送拉取请求。
- 我们感谢您的输入！

### 安装依赖

```bash
uv lock
uv sync
```

### 虚拟环境

```bash
uv venv
```

### 预提交钩子

```bash
pre-commit install
```

### 运行测试

```bash
uv run pytest .
```

### 运行静态类型检查

```bash
uvx mypy src
```

### 打包

```bash
uv build
```

### 本地安装

```bash
uv pip install dist/*.tar.gz
```

## 遥测

CrewAI 使用匿名遥测来收集使用数据，主要目的是通过将精力集中在最常用的功能、集成和工具上来帮助我们改进库。

至关重要的是要理解，**不会收集**关于提示、任务描述、智能体背景故事或目标、工具使用、API 调用、响应、智能体处理的任何数据或秘密和环境变量的数据，所述情况除外。当启用 `share_crew` 功能时，会收集详细数据，包括任务描述、智能体背景故事或目标以及其他特定属性，以在尊重用户隐私的同时提供更深入的见解。用户可以通过将环境变量 OTEL_SDK_DISABLED 设置为 true 来禁用遥测。

收集的数据包括：

- CrewAI 版本
  - 以便我们可以了解有多少用户使用最新版本
- Python 版本
  - 以便我们可以决定更好地支持哪些版本
- 通用操作系统（例如 CPU 数量、macOS/Windows/Linux）
  - 以便我们知道应该关注哪些操作系统，以及是否可以构建特定的操作系统相关功能
- crew 中的智能体和任务数量
  - 以便我们确保在内部使用类似的用例进行测试，并就最佳实践教育人们
- 正在使用的 Crew 流程
  - 了解我们应该在哪里集中精力
- 智能体是否使用内存或允许委派
  - 了解我们是否改进了功能，甚至可能放弃它们
- 任务是并行还是顺序执行
  - 了解我们应该更多地关注并行执行
- 正在使用的语言模型
  - 改进对最常用语言的支持
- crew 中智能体的角色
  - 了解高层用例，以便我们可以围绕它构建更好的工具、集成和示例
- 可用的工具名称
  - 了解在公开可用的工具中，哪些工具使用最多，以便我们可以改进它们

用户可以选择加入进一步的遥测，通过将他们的 Crews 上的 `share_crew` 属性设置为 `True` 来共享完整的遥测数据。启用 `share_crew` 后，将收集详细的 crew 和任务执行数据，包括任务的 `goal`、`backstory`、`context` 和 `output`。这可以在尊重用户选择共享的情况下更深入地了解使用模式。

## 许可证

CrewAI 在 [MIT 许可证](https://github.com/crewAIInc/crewAI/blob/main/LICENSE)下发布。

## 常见问题 (FAQ)

### 通用

- [CrewAI 到底是什么？](#q-crewai-到底是什么)
- [如何安装 CrewAI？](#q-如何安装-crewai)
- [CrewAI 依赖 LangChain 吗？](#q-crewai-依赖-langchain-吗)
- [CrewAI 是开源的吗？](#q-crewai-是开源的吗)
- [CrewAI 会从用户那里收集数据吗？](#q-crewai-会从用户那里收集数据吗)

### 功能和能力

- [CrewAI 能处理复杂的用例吗？](#q-crewai-能处理复杂的用例吗)
- [我可以将 CrewAI 与本地 AI 模型一起使用吗？](#q-我可以将-crewai-与本地-ai-模型一起使用吗)
- [Crews 和 Flows 有什么不同？](#q-crews-和-flows-有什么不同)
- [CrewAI 比 LangChain 好在哪里？](#q-crewai-比-langchain-好在哪里)
- [CrewAI 支持微调或训练自定义模型吗？](#q-crewai-支持微调或训练自定义模型吗)

### 资源和社区

- [在哪里可以找到现实世界的 CrewAI 示例？](#q-在哪里可以找到现实世界的-crewai-示例)
- [如何为 CrewAI 做出贡献？](#q-如何为-crewai-做出贡献)

### 企业功能

- [CrewAI AMP 提供哪些额外功能？](#q-crewai-amp-提供哪些额外功能)
- [CrewAI AMP 可用于云端和本地部署吗？](#q-crewai-amp-可用于云端和本地部署吗)
- [我可以免费试用 CrewAI AMP 吗？](#q-我可以免费试用-crewai-amp-吗)

### Q: CrewAI 到底是什么？

A: CrewAI 是一个独立的、精简的、快速的 Python 框架，专门用于编排自主 AI 智能体。与 LangChain 等框架不同，CrewAI 不依赖外部依赖，使其更精简、更快、更简单。

### Q: 如何安装 CrewAI？

A: 使用 pip 安装 CrewAI：

```shell
uv pip install crewai
```

对于额外工具，使用：

```shell
uv pip install 'crewai[tools]'
```

### Q: CrewAI 依赖 LangChain 吗？

A: 不。CrewAI 完全从零开始构建，不依赖 LangChain 或其他智能体框架。这确保了精简、快速和灵活的体验。

### Q: CrewAI 能处理复杂的用例吗？

A: 是的。CrewAI 在简单和高度复杂的现实场景中都表现出色，提供高层和低层的深度定制选项，从内部提示到复杂的工作流编排。

### Q: 我可以将 CrewAI 与本地 AI 模型一起使用吗？

A: 当然可以！CrewAI 支持各种语言模型，包括本地模型。Ollama 和 LM Studio 等工具允许无缝集成。查看 [LLM 连接文档](https://docs.crewai.com/how-to/LLM-Connections/)了解更多详情。

### Q: Crews 和 Flows 有什么不同？

A: Crews 提供自主智能体协作，适合需要灵活决策和动态交互的任务。Flows 提供精确的、事件驱动的控制，适合管理详细的执行路径和安全状态管理。您可以无缝结合两者以获得最大效果。

### Q: CrewAI 比 LangChain 好在哪里？

A: CrewAI 提供更简单、更直观的 API、更快的执行速度、更可靠和一致的结果、强大的文档和活跃的社区——解决了与 LangChain 相关的常见批评和限制。

### Q: CrewAI 是开源的吗？

A: 是的，CrewAI 是开源的，积极鼓励社区贡献和协作。

### Q: CrewAI 会从用户那里收集数据吗？

A: CrewAI 严格收集匿名遥测数据以用于改进目的。除非用户明确启用，否则永远不会收集提示、任务或 API 响应等敏感数据。

### Q: 在哪里可以找到现实世界的 CrewAI 示例？

A: 在 [CrewAI-examples 仓库](https://github.com/crewAIInc/crewAI-examples)中查看实际示例，涵盖旅行规划、股票分析和职位发布等用例。

### Q: 如何为 CrewAI 做出贡献？

A: 热烈欢迎贡献！派生仓库，创建您的分支，实施您的更改，然后提交拉取请求。有关详细指南，请参阅 README 的贡献部分。

### Q: CrewAI AMP 提供哪些额外功能？

A: CrewAI AMP 提供高级功能，如统一控制平面、实时可观测性、安全集成、高级安全、可操作的洞察和专属 24/7 企业支持。

### Q: CrewAI AMP 可用于云端和本地部署吗？

A: 是的，CrewAI AMP 支持基于云和本地的部署选项，允许企业满足其特定的安全和合规要求。

### Q: 我可以免费试用 CrewAI AMP 吗？

A: 是的，您可以通过免费访问 [Crew 控制平面](https://app.crewai.com)来探索 CrewAI AMP 套件的一部分。

### Q: CrewAI 支持微调或训练自定义模型吗？

A: 是的，CrewAI 可以与自定义训练或微调的模型集成，允许您使用领域特定的知识和准确性增强智能体。

### Q: CrewAI 智能体可以与外部工具和 API 交互吗？

A: 当然可以！CrewAI 智能体可以轻松与外部工具、API 和数据库集成，使它们能够利用现实世界的数据和资源。

### Q: CrewAI 适合生产环境吗？

A: 是的，CrewAI 专为生产级标准设计，确保企业部署的可靠性、稳定性和可扩展性。

### Q: CrewAI 的可扩展性如何？

A: CrewAI 高度可扩展，支持简单自动化和大规模企业工作流，同时涉及多个智能体和复杂任务。

### Q: CrewAI 提供调试和监控工具吗？

A: 是的，CrewAI AMP 包括高级调试、跟踪和实时可观测性功能，简化了自动化的管理和故障排除。

### Q: CrewAI 支持哪些编程语言？

A: CrewAI 主要基于 Python，但可以通过其灵活的 API 集成功能轻松与用任何编程语言编写的服务和 API 集成。

### Q: CrewAI 为初学者提供教育资源吗？

A: 是的，CrewAI 通过 learn.crewai.com 提供广泛的初学者友好教程、课程和文档，支持各级技能的开发者。

### Q: CrewAI 可以自动化人在环中的工作流吗？

A: 是的，CrewAI 完全支持人在环中的工作流，允许人类专家和 AI 智能体之间无缝协作，以增强决策。
