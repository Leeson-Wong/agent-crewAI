#!/usr/bin/env python
"""
故事创作团队 - 主程序入口

这个程序运行一个由多个 AI Agent 组成的故事创作团队，
包括故事策划、写作和编辑三个角色。

监控功能：
    - 启用后，会自动发送 Agent 事件到监控服务器
    - 设置环境变量：
        export AGENT_MONITOR_ENABLED=true
        export AGENT_MONITOR_URL=http://localhost:8080
"""
import sys
from story_writer_crew.crew import StoryWriterCrew  # 相对导入，因为在同一包内

# ==================== 监控插件导入 ====================
# 尝试从多个可能的路径导入监控插件
MONITOR_AVAILABLE = False
CrewAIPlugin = None

# 方式1: 从已安装的包导入
try:
    from agent_monitor.plugins.crewai_plugin import CrewAIPlugin
    MONITOR_AVAILABLE = True
    print("[INFO] Agent Monitor Plugin 已加载 (pip install)")
except ImportError:
    # 方式2: 从本地相对路径导入
    try:
        import sys
        sys.path.insert(0, '../../agent-monitor-plugin/src')
        from agent_monitor.plugins.crewai_plugin import CrewAIPlugin
        MONITOR_AVAILABLE = True
        print("[INFO] Agent Monitor Plugin 已加载 (local source)")
    except ImportError:
        # 方式3: 从项目根目录导入
        try:
            import sys
            sys.path.insert(0, '../../../agent-monitor-plugin/src')
            from agent_monitor.plugins.crewai_plugin import CrewAIPlugin
            MONITOR_AVAILABLE = True
            print("[INFO] Agent Monitor Plugin 已加载 (project root)")
        except ImportError:
          print("[WARN] Agent Monitor Plugin 未找到")
          print("[INFO] 监控功能将不可用")
          print("[INFO] 安装方法: pip install agent-monitor-plugin")
# ===========================================================


def setup_monitor():
    """
    设置监控插件

    检查环境变量，如果启用了监控，则自动安装插件
    """
    if not MONITOR_AVAILABLE:
        return

    import os

    # 检查是否启用监控
    if not os.getenv("AGENT_MONITOR_ENABLED"):
        print("[INFO] 监控未启用 (设置 AGENT_MONITOR_ENABLED=true 来启用)")
        return

    monitor_url = os.getenv("AGENT_MONITOR_URL")
    if not monitor_url:
        print("[WARN] AGENT_MONITOR_URL 未设置，监控功能无法使用")
        return

    # 安装插件
    try:
        plugin = CrewAIPlugin(monitor_url=monitor_url)
        plugin.install()
        print(f"[INFO] 监控已启用 -> {monitor_url}")
    except Exception as e:
        print(f"[ERROR] 监控插件安装失败: {e}")


def run():
    """
    运行故事创作 Crew

    这个函数创建并执行一个故事创作团队，生成一篇完整的故事。
    """
    # 设置监控（如果启用）
    setup_monitor()

    # 定义输入参数
    inputs = {
        'theme': '时间旅行与遗憾',  # 故事主题
    }

    print("=" * 60)
    print("🎬 启动故事创作团队")
    print("=" * 60)
    print(f"📝 故事主题：{inputs['theme']}")
    print("=" * 60)
    print()

    try:
        # 创建 Crew 实例
        story_crew = StoryWriterCrew()

        # 执行 Crew
        # kickoff() 方法会按顺序执行所有任务
        result = story_crew.crew().kickoff(inputs=inputs)

        print()
        print("=" * 60)
        print("✅ 故事创作完成！")
        print("=" * 60)
        print()
        print("📄 生成的文件：")
        print("  - story_draft.md   (故事草稿)")
        print("  - story_final.md   (最终版本)")
        print()

        # 显示最终输出
        if result:
            print("=" * 60)
            print("📖 最终输出摘要")
            print("=" * 60)
            print(str(result.raw))
            print()

    except Exception as e:
        print()
        print("=" * 60)
        print("❌ 执行过程中出现错误")
        print("=" * 60)
        print(f"错误信息：{str(e)}")
        print()
        import traceback
        traceback.print_exc()
        sys.exit(1)


# 也可以为每个输入独立运行 Crew
def run_for_each(inputs_list: list[dict]):
    """
    为多个输入分别运行 Crew

    Args:
        inputs_list: 输入参数列表
    """
    # 设置监控
    setup_monitor()

    story_crew = StoryWriterCrew()
    results = story_crew.crew().kickoff_for_each(inputs=inputs_list)

    for i, result in enumerate(results):
        print(f"\n{'='*60}")
        print(f"结果 #{i+1}")
        print(f"{'='*60}")
        print(result.raw)


# 用于训练 Crew（可选）
def train():
    """
    训练 Crew

    这个函数可以用来优化 Agent 的性能。
    """
    # 设置监控
    setup_monitor()

    inputs = {
        'theme': '科幻冒险',
    }

    training_data = """
    这是一个优秀故事的示例...
    （这里可以提供训练数据）
    """

    story_crew = StoryWriterCrew()
    story_crew.crew().train(
        n_iterations=1,
        inputs=inputs,
        training_data=training_data,
        filename="training_data.json"
    )


# 用于测试 Crew（可选）
def test():
    """
    测试 Crew

    这个函数用于测试 Crew 的性能和输出质量。
    """
    # 设置监控
    setup_monitor()

    inputs = {
        'theme': '测试主题',
    }

    story_crew = StoryWriterCrew()
    story_crew.crew().test(
        n_iterations=1,
        inputs=inputs,
    )


class StoryWriterCrewCLI:
    """命令行界面"""

    @staticmethod
    def run():
        """运行 Crew"""
        run()

    @staticmethod
    def train():
        """训练 Crew"""
        train()

    @staticmethod
    def test():
        """测试 Crew"""
        test()

    @staticmethod
    def repl():
        """
        REPL 模式 - 与 Crew 进行对话式交互

        这个模式允许你多次输入主题，让 Crew 生成多个故事。
        """
        # 设置监控
        setup_monitor()

        story_crew = StoryWriterCrew()

        print("=" * 60)
        print("🎭 故事创作团队 - REPL 模式")
        print("=" * 60)
        print("输入 'quit' 或 'exit' 退出")
        print()

        while True:
            try:
                theme = input("🎨 请输入故事主题（或 quit 退出）: ").strip()

                if theme.lower() in ['quit', 'exit', 'q']:
                    print("\n👋 再见！")
                    break

                if not theme:
                    print("⚠️  请输入一个主题")
                    continue

                inputs = {'theme': theme}

                print(f"\n📝 正在创作主题：{theme} 的故事...\n")

                result = story_crew.crew().kickoff(inputs=inputs)

                print("\n✅ 创作完成！\n")
                print("=" * 60)
                print(str(result.raw))
                print("=" * 60)
                print()

            except KeyboardInterrupt:
                print("\n\n👋 再见！")
                break
            except Exception as e:
                print(f"\n❌ 错误：{str(e)}\n")


# 主程序入口
if __name__ == "__main__":
    # 检查命令行参数
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()

        if command == "repl":
            StoryWriterCrewCLI.repl()
        elif command == "train":
            StoryWriterCrewCLI.train()
        elif command == "test":
            StoryWriterCrewCLI.test()
        else:
            print("用法:")
            print("  python main.py          # 运行一次")
            print("  python main.py repl     # 交互模式")
            print("  python main.py train    # 训练模式")
            print("  python main.py test     # 测试模式")
    else:
        # 默认运行一次
        run()
