import re
from collections.abc import Iterator
from typing import List


def filter_by_currency(transactions: list[dict], currency: str) -> Iterator[dict]:
    """Функция возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной.
    """

    if isinstance(transactions[0].get("currency_code"), str):
        filtered_generator = (position for position in transactions if (position.get("currency_code") == currency))
    elif isinstance(transactions[0].get("operationAmount", {}).get("currency").get("code"), str):
        filtered_generator = (
            position
            for position in transactions
            if (position.get("operationAmount", {}).get("currency", {}).get("code") == currency)
        )
    else:
        items: List[dict] = []
        filtered_generator = (x for x in items)
    for position in filtered_generator:
        try:
            yield position
        except (KeyError, TypeError):
            continue


def transaction_descriptions(transactions_list: list[dict]) -> Iterator[str | type[KeyError]]:
    """
    Функция возвращает описание каждой операции по очереди из списка словарей транзакций.
    """

    operation_generator = (transfer.get("description", KeyError) for transfer in transactions_list)
    for transfer in operation_generator:
        if transfer == "":
            continue
        try:
            yield transfer
        except KeyError:
            continue


def card_number_generator(start: int, stop: int) -> Iterator[str | type[ValueError]]:
    """
    Функция генерирует номера карт формата XXXX XXXX XXXX XXXX в заданном диапазоне.
    """

    if start <= 0 or stop < start:
        raise ValueError("Значения вне диапазона номеров.")
    elif (stop + 1) >= 10**16:
        raise ValueError("Значения вне диапазона номеров.")
    for line in range(start, stop + 1):
        unbroken_line = ((16 - len(str(line))) * "0") + str(line)
        card_number = re.sub(r"^(\d{4})(\d{4})(\d{4})(\d{4})$", r"\1 \2 \3 \4", unbroken_line)
        yield card_number
