import json
import os

FILE_PATH = "assistant/memory/chat_history.json"


def save_chat(user, assistant):
    os.makedirs(os.path.dirname(FILE_PATH), exist_ok=True)

    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            history = json.load(f)
    else:
        history = []

    history.append({
        "user": user,
        "assistant": assistant
    })

    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=4)


def load_chat():
    if not os.path.exists(FILE_PATH):
        return []

    with open(FILE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)