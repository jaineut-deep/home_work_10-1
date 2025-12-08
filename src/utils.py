import json
import os


def get_operations(file_path: str) -> list | str:
    """Функция возвращает список транзакций из файла operations.json"""

    if os.path.isfile(file_path):
        try:
            interim_file = open(file_path)
            interim_file.close()
        except IOError:
            return "Файл занят, попробуйте позже."
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                raw_content = json.load(file)
        except json.JSONDecodeError:
            return []
        if isinstance(raw_content, list):
            return raw_content
        else:
            return []
    else:
        return []
