#!/usr/bin/env python
"""
测试 story_writer_crew + Vibecraft 集成
"""
import os
import sys

# 设置环境变量
os.environ["AGENT_MONITOR_ENABLED"] = "true"
os.environ["AGENT_MONITOR_URL"] = "http://localhost:4003"
os.environ["AGENT_SERVER_ID"] = "story-writer-crew"

# 导入插件
try:
    from agent_monitor import CrewAIPlugin
    print("✓ 监控插件已加载")
except ImportError as e:
    print(f"✗ 监控插件未找到: {e}")
    sys.exit(1)

# 初始化插件
plugin = CrewAIPlugin()
print(f"✓ 插件已初始化 (server_id: {plugin.server_id})")

# 安装插件（注册监听器）
plugin.install()
print("✓ 监控监听器已安装")

# 测试发送事件
print("\n测试发送事件到 Vibecraft...")
test_event = {
    "protocol": "agent-monitor",
    "version": "1.0",
    "source": {
        "server_id": plugin.server_id,
        "agent_id": "test-agent",
        "framework": "crewai",
        "language": "python",
        "process_id": os.getpid()
    },
    "event": {
        "type": "agent_online",
        "data": {
            "role": "Story Writer",
            "goal": "Write amazing stories"
        }
    },
    "metadata": {
        "hostname": "test-host",
        "ip_address": "127.0.0.1"
    }
}

# 直接发送到 Vibecraft 的 /event 端点
import requests
response = requests.post("http://localhost:4003/event", json=test_event, timeout=2)
if response.status_code == 200:
    print("✓ 测试事件发送成功！")
else:
    print(f"✗ 事件发送失败: {response.status_code}")

print("\n现在可以运行 main.py 了！")
print("提示：插件会自动发送事件到 Vibecraft")
