import json

class PrintMixin:
    def __init__(self, *args):
        print(repr(self))

    def __repr__(self):
        object_attributes = ''
        for k, v in self.__dict__.items():
            object_attributes += f'{k}: {v},'
        return f"создан объект со свойствами {object_attributes}"

class LogMixin:
    def __init__(self):
        self.log_messages = []

    def log(self, message):
        self.log_messages.append(message)

    def __str__(self):
        return f"Лог: {', '.join(self.log_messages)}" if self.log_messages else "Лог: (пусто)"

def load_data_from_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data
