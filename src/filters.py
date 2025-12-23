import re
from collections import Counter

from src.generators import transaction_descriptions


def get_process_search(bank_data: list[dict], row_search: str) -> list[dict] | None:
    """
    Функция возвращает список словарей, у которых в описании есть заданная строка поиска.
    """

    if row_search.isalpha() and len(row_search) >= 4:
        pattern = re.compile(row_search)
        filtered_bank_data: list[dict] = list(
            filter(lambda transaction: re.search(pattern, transaction.get("description")), bank_data)
        )
        return filtered_bank_data
    else:
        return None


def process_bank_operations(transactions_data: list[dict], categories_names: list) -> dict:
    """
    Функция возвращает словарь, в котором ключи — это названия категорий, а значения —
    это количество операций в каждой категории.
    """

    for operation in transaction_descriptions(transactions_data):
        if operation and operation is not KeyError:
            categories_names.append(operation)
        else:
            pass
    operations_quantity = dict(Counter(categories_names))
    return operations_quantity
