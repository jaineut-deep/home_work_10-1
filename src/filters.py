import re
from collections import Counter


def get_process_search(bank_data: list[dict], row_search: str) -> list[dict] | None:
    """
    Функция возвращает список словарей, у которых в описании есть заданная строка поиска.
    """

    if row_search.isalpha() and len(row_search) >= 4:
        pattern = re.compile(row_search, flags=re.IGNORECASE)
        filtered_bank_data: list[dict] = list(
            filter(lambda transaction: re.search(pattern, transaction.get("description", "")), bank_data)
        )
        return filtered_bank_data
    else:
        return None


def process_bank_operations(transactions_data: list[dict], categories_names: list) -> dict:
    """
    Функция возвращает словарь, в котором ключи — это названия категорий, а значения —
    это количество операций в каждой категории.
    """

    categories_names = [x.get("description", "") for x in transactions_data if x.get("description") is not None]
    operations_quantity = dict(Counter(categories_names))
    return operations_quantity
