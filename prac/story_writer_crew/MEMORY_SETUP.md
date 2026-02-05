# CrewAI 记忆功能配置说明

## 问题说明

当启用 `memory=True` 时，CrewAI 使用 ChromaDB 进行向量存储，而 ChromaDB 默认调用 OpenAI 嵌入 API，在中国大陆无法访问。

## 解决方案

### 方案 1：禁用记忆功能（当前配置）

**已应用**：`src/story_writer_crew/crew.py` 中 `memory=False`

这是最简单的方案，适合不需要记忆功能的场景。

### 方案 2：使用本地嵌入模型（推荐）

#### 2.1 安装依赖

```bash
pip install sentence-transformers
```

#### 2.2 配置环境变量

在 `.env` 文件中添加：

```bash
# 使用本地嵌入模型
EMBEDDING_MODEL=sentence-transformers
SENTENCE_TRANSFORMERS_MODEL=paraphrase-multilingual-MiniLM-L12-v2
```

#### 2.3 修改 crew.py

```python
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.memory.embeddings import OpenAIEmbedding
from chromadb.utils import embedding_functions

@CrewBase
class StoryWriterCrew:
    # ... agents 和 tasks 定义 ...

    @crew
    def crew(self) -> Crew:
        # 创建本地嵌入函数
        local_embedder = embedding_functions.SentenceTransformerEmbeddingFunction(
            model_name="paraphrase-multilingual-MiniLM-L12-v2"  # 支持中文
        )

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
            memory=True,  # 启用记忆
            # 注意：CrewAI 可能需要额外配置来使用本地嵌入
            max_rpm=None,
            share_crew=False,
        )
```

### 方案 3：使用国内 API 嵌入模型

使用智谱 AI、通义千问等厂商的嵌入 API：

```python
# 需要实现自定义嵌入类
from typing import List
import requests

class ZhipuEmbedding:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://open.bigmodel.cn/api/paas/v4/embeddings"

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        # 调用智谱嵌入 API
        headers = {"Authorization": f"Bearer {self.api_key}"}
        response = requests.post(
            self.base_url,
            json={"input": texts, "model": "embedding-2"},
            headers=headers
        )
        return [item["embedding"] for item in response.json()["data"]]
```

## 推荐模型

### 本地嵌入模型（Sentence Transformers）

| 模型 | 语言 | 大小 | 速度 |
|------|------|------|------|
| `paraphrase-multilingual-MiniLM-L12-v2` | 多语言（含中文） | 420MB | 快 |
| `shibing624/text2vec-base-chinese` | 中文 | 400MB | 快 |
| `moka-ai/m3e-base` | 中文 | 400MB | 快 |

### 国内 API 嵌入服务

| 厂商 | 模型 | API 文档 |
|------|------|----------|
| 智谱 AI | embedding-2 | https://open.bigmodel.cn/dev/api |
| 通义千问 | text-embedding-v2 | https://help.aliyun.com/zh/dashscope/ |
| 百川智能 | baichuan-text-embedding | https://platform.baichuan-ai.com/docs |

## 验证配置

运行测试：

```bash
python run.py
```

如果不再出现 OpenAI API 连接错误，说明配置成功。
