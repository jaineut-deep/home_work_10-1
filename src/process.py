import json
import re
from datetime import datetime
from typing import Union


def filter_by_state(input_customer_roster: str, state: str = "EXECUTED") -> Union[str, list]:
    """
    Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению.
    """

    json_input_roster: str = input_customer_roster.replace("'", '"')
    customer_roster = json.loads(json_input_roster)
    filtered_customer_roster: list = [{}]
    if not customer_roster:
        return "Клиентская ведомость пуста"
    for customer in customer_roster:
        if customer not in customer_roster:
            return "Клиентская ведомость пуста"
        elif customer.get("state") not in ["EXECUTED", "CANCELED"]:
            continue
        elif customer.get("state") in ["EXECUTED", "CANCELED"]:
            filtered_customer_roster = list(filter(lambda key: key["state"] == state, customer_roster))
        else:
            return "Ни одна из позиций не удовлетворяет запросу"
    if not filtered_customer_roster:
        return "Ни одна из позиций не удовлетворяет запросу"
    return filtered_customer_roster


def sort_by_date(input_consumer_register: str, sort_order: str = "True") -> Union[str, list]:
    """
    Функция возвращает новый список словарей, отсортированный по дате (date).
    """

    if sort_order == "True":
        sort_order_bool = True
    elif sort_order == "False":
        sort_order_bool = False
    elif sort_order == "":
        sort_order_bool = True
    else:
        return "Не задан порядок сортировки"
    json_input_register: str = input_consumer_register.replace("'", '"')
    consumer_register = json.loads(json_input_register)
    valid_date_register = []
    if not consumer_register:
        return "Клиентская ведомость пуста"
    for consumer in consumer_register:
        if consumer not in consumer_register:
            return "Клиентская ведомость пуста"
        elif consumer.get("date") is None:
            continue
        elif re.match(r"^\d{4}-\d{2}-\d{2}", consumer.get("date")):
            try:
                datetime.strptime(consumer.get("date")[:10], "%Y-%m-%d").date()
            except (ValueError, TypeError):
                continue
            valid_date_register.append(consumer)
    sorted_consumer_register = sorted(
        valid_date_register,
        key=lambda idx: datetime.strptime(idx.get("date")[:10], "%Y-%m-%d").date(),
        reverse=sort_order_bool,
    )
    return sorted_consumer_register


if __name__ == "__main__":
    print(filter_by_state(input_customer_roster=input(), state=input()))
    print(sort_by_date(input_consumer_register=input(), sort_order=input()))
