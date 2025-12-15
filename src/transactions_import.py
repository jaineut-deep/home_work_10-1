import os
from typing import Any

import pandas as pd
from pandas.errors import EmptyDataError


def get_operations_data(file_path: str) -> list[Any]:
    """Функция считывает финансовые операции из CSV-, XLS- и XLSX-файлов: принимает путь
    к файлу и возвращает список словарей с транзакциями. Если считать данные невозможно —
    возвращает пустой список.
    """

    _, file_extension = os.path.splitext(file_path)
    if file_extension == ".csv":
        try:
            data_csv = pd.read_csv(file_path, delimiter=";")
            list_data_csv = data_csv.to_dict(orient="records")
            return list_data_csv
        except StopIteration:
            print("Файл пуст или не содержит заголовков")
            return []
        except ValueError:
            print("Несоответствие числа столбцов строкам или ошибка преобразования")
            return []
    elif file_extension in [".xlsx", ".xls"]:
        try:
            data_excel = pd.read_excel(file_path)
            list_data_excel = data_excel.to_dict(orient="records")
            return list_data_excel
        except EmptyDataError:
            print("Файл пуст или не содержит заголовков")
            return []
        except ValueError:
            print("Несоответствие числа столбцов строкам или ошибка преобразования")
            return []
    else:
        print("Расширение файла не поддерживается программой")
        return []
