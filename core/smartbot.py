import os
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain_community.tools.youtube.search import YouTubeSearchTool
from core.tools import ImageCaptionTool, ObjectDetectionTool


class SmartBot:
    def __init__(self, bot_name, config=None):
        if not config:
            config = {}
        if "model" not in config:
            config["model"] = "gpt-3.5-turbo-0125"
        if "temperature" not in config:
            config["temperature"] = 0.7
        self.bot_name = bot_name
        self.llm = ChatOpenAI(
            openai_api_key=os.environ.get("OPENAI_API_KEY"),
            model=config["model"],
            temperature=config["temperature"],
        )
        self.history = []
        self.tools = [ImageCaptionTool(), ObjectDetectionTool(), YouTubeSearchTool()]
        self.conversational_memory = ConversationBufferWindowMemory(
            memory_key="chat_history", k=50, return_messages=True
        )

    def send_message(self, message):
        query = message["query"]
        image = message.get("image") or ""
        prompt = None
        agent = initialize_agent(
            agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
            tools=self.tools,
            llm=self.llm,
            max_iterations=5,
            verbose=True,
            early_stopping_method="generate",
            handle_parsing_errors=True,
            memory=self.conversational_memory,
        )
        if image:
            prompt = "input = {}, this is the image path: {}".format(
                query, image or "no_image"
            )
        else:
            prompt = "input = {}".format(query)

        response = agent.run(prompt)
        return response


# test code
# smartbot = SmartBot("Smartbot")
# try:
#     image_path = (
#         "/Users/rohityadav/private/code/challanges/smartbot/images/Indra-Baruna.jpeg"
#     )
#     message = {"query": "Describe the person in the image ?", "image": None}
#     response = smartbot.send_message(message)
#     print(response)
# except Exception as e:
#     print(e)
