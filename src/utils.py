import json
import logging
import os

origin_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")
path_logfile = os.path.join(origin_dir, "module_utils.log")
utils_logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(path_logfile, mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(module)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
utils_logger.addHandler(file_handler)
utils_logger.setLevel(logging.DEBUG)


def get_operations(file_path: str) -> list | str:
    """Функция возвращает список транзакций из файла operations.json"""

    utils_logger.info("Начало работы программы чтения данных из файла.")
    if os.path.isfile(file_path):
        try:
            interim_file = open(file_path)
            interim_file.close()
            utils_logger.info("Файл не занят.")
        except IOError:
            utils_logger.error("Файл занят, попробуйте позже.")
            return "Файл занят, попробуйте позже."
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                raw_content = json.load(file)
            utils_logger.info("Десериализация прошла успешно.")
        except json.JSONDecodeError:
            utils_logger.error("Невозможно десериализовать данные.")
            return []
        if isinstance(raw_content, list):
            utils_logger.info("Успешное прочтение списка.")
            return raw_content
        else:
            utils_logger.error("Десериализованные данные - не список.")
            return []
    else:
        utils_logger.error("Запрашиваемый файл не существует.")
        return []
