# AutoGen-Agent AI 

这是一个基于多智能体（AutoGen-Agents）的代码示例，，通过 [OpenRouter](https://openrouter.ai/) 、[Google Gemini API](https://aistudio.google.com/)、本地部署的 [Ollama](https://ollama.com/) 模型。你可以使用它快速构建灵活的多智能体协作系统。

## ✨ 特性

- 🤖 多模型协作：支持 OpenRouter、Gemini、本地 Ollama 等模型灵活组合。
- 🔁 多智能体并行：每个 Agent 可单独设定角色、目标、策略。
- 🧱 易于扩展：模块化架构，适配新的模型或 Agent 类型很方便。
- 📦 示例：翻译助手、写作助理、旅行规划助手。

## 🛠 安装

本项目使用 [uv](https://pypi.org/project/uv/) 进行依赖管理。确保你已经安装了 `uv`。你可以通过 pip 安装：

```bash
pip install uv

git clone [https://github.com/yourusername/multi-agent-framework.git](https://github.com/zhaomo08/AutoGen_GraphFlow.git)
cd AutoGen_GraphFlow
uv pip install -r pyproject.toml
```
🚀 示例

1. 翻译助手（Translator Agent）

该示例中，多个 Agent 协作完成高质量翻译任务，包括以下三个阶段：

1. **初稿翻译**：使用本地部署的 **Ollama** 模型快速完成初步翻译。
2. **风格润色**：通过 **Gemini** 进一步优化语言风格，使表达更自然流畅。
3. **术语校对**：调用 **OpenRouter（如 GPT-4）** 复查专业术语，确保翻译准确无误。

```bash
(AutoGen_GraphFlow) ☁  0510_simple_agent  python sequence_flow.py
```
2. 写作助手（Writing Agent）

该示例通过多模型协同，提供写作辅助服务，包含以下步骤：

1. **思路发散**：借助 **Gemini** 激发主题创意，构建初步写作方向。
2. **段落草稿**：由 **Gemini** 生成初稿段落，确保语义连贯。
3. **结构优化与润色**：继续使用 **Gemini** 对文章整体结构进行调整，并提升语言表达质量。
```bash
(AutoGen_GraphFlow) ☁  0510_simple_agent  python parallel_flow.py
```
3. 旅行助手（Travel Assistant Agent）


该示例通过多个智能体协同，完成个性化的旅行规划任务，具体包括：

1. **规划师智能体**：制定整体旅行框架，包括时间安排和大致路线。
2. **当地专家智能体**：根据目的地推荐热门景点、本地活动与餐饮建议。
3. **语言专家智能体**：提供实用语言翻译支持与跨文化沟通技巧，提升旅行体验。

```bash
(AutoGen_GraphFlow) ☁  0510_simple_agent  python travel_agent.py
```


📜 许可证

MIT License

## 🙋‍♂️ 致谢

感谢以下开源项目提供灵感与支持：

- [OpenRouter](https://openrouter.ai/)
- [Ollama](https://ollama.com/)
- [Gemini API](https://aistudio.google.com/)