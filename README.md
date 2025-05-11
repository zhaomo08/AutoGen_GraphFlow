# AutoGen-Agent AI 

这是一个基于多智能体（AutoGen-Agents）的代码示例，，通过 [OpenRouter](https://openrouter.ai/) 、Google Gemini API、本地部署的 [Ollama](https://ollama.com/) 模型。你可以使用它快速构建灵活的多智能体协作系统。

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


🚀 示例

1. 翻译助手（Translator Agent）

该示例中，多个 Agent 协作完成高质量翻译任务，例如：
	•	初稿翻译（使用 Ollama 本地模型）
	•	风格润色（使用 Gemini）
	•	专业术语复核（使用 OpenRouter GPT-4）

```bash
(AutoGen_GraphFlow) ☁  AutoGen_GraphFlow  cd 0510_simple_agent
(AutoGen_GraphFlow) ☁  0510_simple_agent  python sequence_flow.py

2. 写作助手（Writing Agent）

通过多智能体实现写作辅助(可以修改为多模型)：
	•	思路发散（Gemini）
	•	段落草稿（Gemini）
	•	结构优化和语言润色（Gemini） 
```bash
(AutoGen_GraphFlow) ☁  AutoGen_GraphFlow  cd 0510_simple_agent
(AutoGen_GraphFlow) ☁  0510_simple_agent  python parallel_flow.py

3. 旅行助手（Travel Assistant Agent）

旅行规划智能体包括：
	•	规划师智能体（初步旅行计划制定）
	•	当地专家智能体（当地活动和景点建议）
	•	语言专家智能体（提供语言和沟通技巧）

```bash
(AutoGen_GraphFlow) ☁  AutoGen_GraphFlow  cd 0510_simple_agent
(AutoGen_GraphFlow) ☁  0510_simple_agent  python travel_agent.py




📜 许可证

MIT License

## 🙋‍♂️ 致谢

感谢以下开源项目提供灵感与支持：

- [OpenRouter](https://openrouter.ai/)
- [Ollama](https://ollama.com/)
- [Gemini API](https://ai.google.dev/)