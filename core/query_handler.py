import os
from flask import request

from core.utils import clear_dir, response


def handle_query():
    from app import bot_manager

    response_obj = {}
    bot_id = request.form.get("bot_id")
    bot = bot_manager.get_bot(bot_id)
    if not bot:
        return response("Invalid bot id", success=0)
    query = None
    image_path = None
    if "query" in request.form:
        query = request.form["query"]
    if not query:
        return response("Invalid query", success=0)

    print("Files: ", request.files)
    if "image" in request.files:
        image = request.files.getlist("image")[0]
        image_name = image.filename
        if image_name:
            image.save("images/" + image_name)
            image_path = os.path.abspath("images/" + image_name)
            clear_dir("images")

    message = {"query": query, "image": image_path}
    response_obj["response"] = bot["manager"].send_message(message)
    response_obj["query"] = query
    if not response_obj:
        return "Invalid query", 400

    return response(response_obj)


def handle_get_bot():
    from app import bot_manager

    response = {}

    bot = bot_manager.get_free_bot()
    if bot:
        response["bot_id"] = bot["id"]
    else:
        response["error"] = "No bots available"

    return response
