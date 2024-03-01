import json

def load_data_from_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

class LogMixin:
    def __init__(self):
        self.log_messages = []

    def log(self, message):
        self.log_messages.append(message)

    def __str__(self):
        return f"Лог: {', '.join(self.log_messages)}" if self.log_messages else "Лог: (пусто)"
