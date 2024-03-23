from random import Random
from core.smartbot import SmartBot


class BotManager:
    def __init__(self):
        self.bots = {
            "Mike": {
                "id": "Mike",
                "occupied": False,
                "manager": SmartBot("Mike"),
            },
            "Hazel": {
                "id": "Hazel",
                "occupied": False,
                "manager": SmartBot("Hazel"),
            },
            "Alice": {
                "id": "Alice",
                "occupied": False,
                "manager": SmartBot("Alice"),
            },
            "Steve": {
                "id": "Steve",
                "occupied": False,
                "manager": SmartBot("Steve"),
            },
        }

    def get_bot(self, bot_id):
        if bot_id in self.bots:
            self.bots[bot_id]["occupied"] = True
            return self.bots[bot_id]
        return None

    def release_bot(self, bot_id):
        if bot_id in self.bots:
            self.bots[bot_id]["occupied"] = False
            return True
        return False

    def get_free_bot(self):
        free_bots = [bot for bot in self.bots.values() if not bot["occupied"]]
        if free_bots:
            return Random().choice(free_bots)
        return None
