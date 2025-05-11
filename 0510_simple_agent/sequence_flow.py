# AI 超元域  https://youtu.be/q_IdxUGZsow?si=1kiksFz4hlH5gpUT

# 导入必要的库
import asyncio
import os

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.teams import DiGraphBuilder, GraphFlow
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_ext.models.ollama import OllamaChatCompletionClient
from autogen_core.models import ModelFamily,ModelInfo




async def main():
    # 创建OpenAI模型客户端
    # model_client = OpenAIChatCompletionClient(model="gpt-4.1-nano")

    model_client = OpenAIChatCompletionClient(
        base_url="https://openrouter.ai/api/v1",
        model="openai/gpt-4.1-nano",
        model_info=ModelInfo(
            vision=False,  # 添加这个必需字段
            function_calling=True,
            json_output=True,
            family=ModelFamily.GPT_4O,  # 使用适当的模型家族
            structured_output=True
        )
    )
    # 创建Gemini模型客户端
    gemini_client = OpenAIChatCompletionClient(
        model="gemini-2.0-flash",
        model_info=ModelInfo(
            vision=True,
            function_calling=True,
            json_output=True,
            family=ModelFamily.GEMINI_2_0_FLASH,
            structured_output=True
        ),
    )
    # 创建ollama模型客户端
    ollama_client = OllamaChatCompletionClient(
        model="qwen3:14b",
        model_info = {
            "vision": False,
            "function_calling": True,
            "json_output": True,
            "family": ModelFamily.UNKNOWN, # ModelFamily 需要从 autogen_core.models 导入
            "structured_output": True,
        },
    )

    # 创建代理
    # 翻译器代理 - 负责将文本从英文翻译为中文
    translator = AssistantAgent(
        "translator",
        model_client=ollama_client,
        system_message="你是一位专业的英文到中文翻译专家。你的任务是将用户提供的英文文本准确翻译成中文，保持原文的语气和风格。"
    )

    # 校对者代理 - 负责检查翻译质量并进行修改
    proofreader = AssistantAgent(
        "proofreader",
        model_client=gemini_client,
        system_message="你是一位中文校对专家。你的任务是检查翻译文本的准确性和流畅度，确保没有错误并提出修改建议。"
    )

    # 格式化代理 - 负责最终输出格式的调整
    formatter = AssistantAgent(
        "formatter",
        model_client=model_client,
        system_message="你是一位文档格式专家。你的任务是根据翻译后的文本进行最终格式调整，确保段落分明，标点符号正确，并保持一致的风格。"
    )

    # 构建执行图
    builder = DiGraphBuilder()

    # 添加节点
    builder.add_node(translator).add_node(proofreader).add_node(formatter)

    # 添加边（定义执行顺序）
    builder.add_edge(translator, proofreader)
    builder.add_edge(proofreader, formatter)

    # 构建和验证图
    graph = builder.build()

    # 创建GraphFlow
    flow = GraphFlow(
        participants=builder.get_participants(),
        graph=graph
    )

    # 运行工作流
    result = await flow.run(
        task="Translate the following text to Chinese: 'Artificial intelligence is transforming the way we work and live. It offers new opportunities and challenges that we must navigate carefully.'")

    # 打印结果
    for message in result.messages:
        print(f"{message.source}: {message.content}")

if __name__ == "__main__":
    asyncio.run(main())
