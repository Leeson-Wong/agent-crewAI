"""
故事创作 Crew 定义

这个模块定义了故事创作团队的 Crew、Agent 和 Task。
使用装饰器模式从 YAML 配置文件加载配置。
"""
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# 导入自定义工具（可选）
from story_writer_crew.tools import WordCountTool, StyleAnalysisTool, WritingPromptTool

from typing import List
from crewai.agents.agent_builder.base_agent import BaseAgent


@CrewBase
class StoryWriterCrew:
    """故事创作团队 Crew"""

    # 这些属性会被装饰器自动填充
    agents: List[BaseAgent]
    tasks: List[Task]

    # === 定义 Agents ===
    @agent
    def story_ideator(self) -> Agent:
        """故事构思者 Agent"""
        return Agent(
            config=self.agents_config['story_ideator'],
            verbose=True,
            # 可以添加工具
            tools=[WritingPromptTool()],
            # 允许委派任务给其他 Agent
            allow_delegation=False,
        )

    @agent
    def story_writer(self) -> Agent:
        """故事作家 Agent"""
        return Agent(
            config=self.agents_config['story_writer'],
            verbose=True,
            # 作家可以使用字数统计和风格分析工具
            tools=[WordCountTool(), StyleAnalysisTool()],
            allow_delegation=False,
        )

    @agent
    def story_editor(self) -> Agent:
        """故事编辑 Agent"""
        return Agent(
            config=self.agents_config['story_editor'],
            verbose=True,
            # 编辑使用所有工具
            tools=[WordCountTool(), StyleAnalysisTool()],
            allow_delegation=False,
        )

    # === 定义 Tasks ===
    @task
    def outline_task(self) -> Task:
        """故事大纲创作任务"""
        return Task(
            config=self.tasks_config['outline_task'],
        )

    @task
    def writing_task(self) -> Task:
        """故事撰写任务"""
        return Task(
            config=self.tasks_config['writing_task'],
            output_file='story_draft.md',
        )

    @task
    def editing_task(self) -> Task:
        """编辑润色任务"""
        return Task(
            config=self.tasks_config['editing_task'],
            output_file='story_final.md',
        )

    # === 定义 Crew ===
    @crew
    def crew(self) -> Crew:
        """创建故事创作团队 Crew"""
        return Crew(
            agents=self.agents,  # 由 @agent 装饰器自动创建
            tasks=self.tasks,    # 由 @task 装饰器自动创建
            process=Process.sequential,  # 顺序执行
            verbose=True,
            memory=False,  # 暂时禁用记忆功能（ChromaDB 默认使用 OpenAI 嵌入 API）
            # 可以添加更多配置
            max_rpm=None,  # 不限制每分钟请求数
            share_crew=False,  # 不与 CrewAI 分享数据
        )
