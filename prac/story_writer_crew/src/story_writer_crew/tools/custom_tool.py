"""
自定义工具示例

这里展示如何创建自定义工具供 Agent 使用。
"""
from crewai.tools import BaseTool
from typing import Optional, Type
from pydantic import BaseModel, Field


# === 工具1: 字数统计工具 ===
class WordCountInput(BaseModel):
    """字数统计工具的输入schema"""
    text: str = Field(..., description="要统计字数的文本")


class WordCountTool(BaseTool):
    name: str = "word_count_tool"
    description: str = "统计文本的字数、段落数和行数"
    args_schema: Type[BaseModel] = WordCountInput

    def _run(self, text: str) -> str:
        """执行字数统计"""
        word_count = len(text)
        char_count = len(text.replace(" ", ""))
        paragraph_count = len([p for p in text.split('\n\n') if p.strip()])
        line_count = len([l for l in text.split('\n') if l.strip()])

        result = f"""
📊 文本统计结果：
- 字符数：{char_count}
- 词数：{word_count}
- 段落数：{paragraph_count}
- 行数：{line_count}
"""
        return result


# === 工具2: 写作风格分析工具 ===
class StyleAnalysisInput(BaseModel):
    """写作风格分析的输入schema"""
    text: str = Field(..., description="要分析的文本")
    focus: str = Field(
        default="overall",
        description="分析重点：overall(整体), tone(语调), structure(结构), vocabulary(词汇)"
    )


class StyleAnalysisTool(BaseTool):
    name: str = "style_analysis_tool"
    description: str = "分析文本的写作风格，包括语调、结构、词汇使用等"
    args_schema: Type[BaseModel] = StyleAnalysisInput

    def _run(self, text: str, focus: str = "overall") -> str:
        """执行写作风格分析"""
        # 简单示例分析（实际应用中可以使用 NLP 模型）
        avg_sentence_length = len(text.split('.')) / max(len(text.split('\n')), 1)

        analysis = {
            "overall": f"""
✍️ 整体风格分析：
- 平均句长：{avg_sentence_length:.1f} 句/段落
- 文本密度：{'高' if len(text) > 500 else '中等' if len(text) > 200 else '低'}
- 风格特点：{'描写细腻' if len(text) > 500 else '简洁明快'}
""",
            "tone": "🎭 语调分析：待开发（需要更复杂的NLP模型）",
            "structure": "📐 结构分析：待开发",
            "vocabulary": "📚 词汇分析：待开发"
        }

        return analysis.get(focus, analysis["overall"])


# === 工具3: 写作提示生成器 ===
class WritingPromptInput(BaseModel):
    """写作提示生成的输入schema"""
    genre: str = Field(..., description="故事类型：科幻、奇幻、悬疑、爱情等")
    difficulty: str = Field(
        default="medium",
        description="难度级别：easy, medium, hard"
    )


class WritingPromptTool(BaseTool):
    name: str = "writing_prompt_tool"
    description: str = "根据指定的类型和难度生成创意写作提示"
    args_schema: Type[BaseModel] = WritingPromptInput

    def _run(self, genre: str, difficulty: str = "medium") -> str:
        """生成写作提示"""
        prompts = {
            "科幻": [
                "2050年，人类首次发现外星文明，但它们以数字形式存在...",
                "时间机器被发明了，但只能回到过去5分钟...",
                "一个AI突然产生了自我意识，它决定...",
            ],
            "奇幻": [
                "在一个魔法即将消失的世界，最后一位魔法师...",
                "普通人突然觉醒了超能力，但每次使用都会...",
                "通往异世界的门被打开了，但只有孩子能通过...",
            ],
            "悬疑": [
                "侦探发现所有线索都指向自己...",
                "一名女子醒来，发现自己在一个完全陌生的房间...",
                "连续10天，每天中午都有人消失...",
            ],
            "爱情": [
                "两个从未见面的陌生人发现他们做着相同的梦...",
                "一封50年前的信件寄到了，发信日期是明天...",
                "在一个只能用文字交流的世界，两人相爱了...",
            ]
        }

        import random
        genre_prompts = prompts.get(genre, ["创作一个独特的故事..."])
        prompt = random.choice(genre_prompts)

        return f"""
🎨 写作提示（{genre} - {difficulty}难度）：

{prompt}

💡 创作建议：
- {'这个提示适合初学者' if difficulty == 'easy' else '这个提示需要一些创意' if difficulty == 'medium' else '这个提示挑战性较大'}
- 考虑加入意外转折增加趣味性
- 注重人物情感和内心描写
"""
