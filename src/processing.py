import json
import re
from datetime import datetime
from typing import Any


def filter_by_state(input_customer_list: str, state: str = "EXECUTED") -> Any:
    """
    Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению.
    """

    json_input_list: str = input_customer_list.replace("'", '"')
    customer_list = json.loads(json_input_list)
    filtered_customer_list: list = [{}]
    if not customer_list:
        return "Клиентская ведомость пуста"
    for customer in customer_list:
        if customer not in customer_list:
            return "Клиентская ведомость пуста"
        elif customer.get("state") not in ["EXECUTED", "CANCELED"]:
            continue
        elif customer.get("state") in ["EXECUTED", "CANCELED"]:
            filtered_customer_list = list(filter(lambda key: key["state"] == state, customer_list))
        else:
            return "Ни одна из позиций не удовлетворяет запросу"
    if not filtered_customer_list:
        return "Ни одна из позиций не удовлетворяет запросу"
    return filtered_customer_list


def sort_by_date(input_consumer_statement: str, sort_order: bool | None = True) -> Any:
    """
    Функция возвращает новый список словарей, отсортированный по дате (date).
    """

    if not isinstance(sort_order, bool):
        return "Не задан порядок сортировки"
    json_input_statement: str = input_consumer_statement.replace("'", '"')
    consumer_statement = json.loads(json_input_statement)
    valid_date_statement = []
    if not consumer_statement:
        return "Клиентская ведомость пуста"
    for consumer in consumer_statement:
        if consumer not in consumer_statement:
            return "Клиентская ведомость пуста"
        elif consumer.get("date") is None:
            continue
        elif re.match(r"^\d{4}-\d{2}-\d{2}", consumer.get("date")):
            try:
                datetime.strptime(consumer.get("date")[:10], "%Y-%m-%d").date()
            except (ValueError, TypeError):
                continue
            valid_date_statement.append(consumer)
    sorted_consumer_statement = sorted(
        valid_date_statement,
        key=lambda idx: datetime.strptime(idx.get("date")[:10], "%Y-%m-%d").date(),
        reverse=sort_order,
    )
    return sorted_consumer_statement


if __name__ == "__main__":
    print(filter_by_state(input_customer_list=input(), state=input()))
    print(
        sort_by_date(
            input_consumer_statement=input(),
            sort_order=(
                True if (user_input := input().strip()) in ["True", ""] else (False if user_input == "False" else None)
            ),
        )
    )
