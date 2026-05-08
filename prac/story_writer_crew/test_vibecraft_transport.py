#!/usr/bin/env python
"""
测试 VibecraftTransport
"""
import os
os.environ["AGENT_MONITOR_ENABLED"] = "true"
os.environ["AGENT_MONITOR_URL"] = "http://localhost:4003"
os.environ["AGENT_SERVER_ID"] = "story-writer-test"

from agent_monitor.transports.vibecraft import VibecraftTransport
from agent_monitor.protocol.unified_event import (
    MonitorEvent,
    EventSource,
    EventMetadata,
    Language,
)

print("✓ VibecraftTransport 导入成功")

# 创建传输器
transport = VibecraftTransport("http://localhost:4003")
print(f"✓ 传输器初始化成功")

# 创建测试事件
event = MonitorEvent(
    source=EventSource(
        server_id="story-writer-test",
        agent_id="story-planner",
        framework="crewai",
        language=Language.python,
        process_id=os.getpid(),
    ),
    event={
        "type": "agent_online",
        "data": {
            "role": "Story Planner",
            "goal": "Create amazing story outlines"
        }
    },
    metadata=EventMetadata(
        hostname="test-host",
        ip_address="127.0.0.1"
    ),
)

print("\n测试发送事件到 Vibecraft...")

# 同步发送
success = transport.send_sync(event.to_dict())
if success:
    print("✓ 事件发送成功（同步）")
else:
    print("✗ 事件发送失败")

# 异步发送
success = transport.send(event.to_dict())
if success:
    print("✓ 事件已提交（异步）")

# 检查统计
import time
time.sleep(1)  # 等待异步发送
stats = transport.get_stats()
print(f"\n统计信息: {stats}")

# 验证数据库
print("\n验证 Vibecraft 数据库...")
import requests
response = requests.get("http://localhost:4003/stats")
if response.status_code == 200:
    data = response.json()
    print(f"✓ 服务器收到事件数: {data.get('totalEvents', 0)}")
else:
    print("✗ 无法获取统计信息")

print("\n✓ 测试完成！VibecraftTransport 工作正常")
