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



if __name__ == "__main__":
    print(filter_by_state(input_customer_roster=input(), state=input()))
    print(sort_by_date(input_consumer_register=input(), sort_order=input()))
