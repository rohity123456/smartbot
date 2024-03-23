from flask import Flask
from dotenv import load_dotenv
from core.bots import BotManager
from core.query_handler import handle_get_bot, handle_query

load_dotenv()
app = Flask(__name__)
bot_manager = BotManager()


@app.route("/")
def hello_world():
    return "Hello, World! Yo how are you doing?"


@app.route("/chat", methods=["POST"])
def query_route():
    return handle_query()


@app.route("/chat/bot", methods=["GET"])
def get_bot_route():
    return handle_get_bot()


if __name__ == "__main__":
    app.run(debug=True)
