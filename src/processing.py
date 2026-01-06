import json
import re
from datetime import datetime
from typing import List, Union


def filter_by_state(input_customer_list: Union[list, str], state: str = "EXECUTED") -> List:
    """
    Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению.
    """

    if state not in ["EXECUTED", "CANCELED", "PENDING"]:
        raise ValueError("Не задан критерий фильтрации")
    if state == "":
        state = "EXECUTED"
    if isinstance(input_customer_list, str):
        try:
            input_customer_list = json.loads(input_customer_list)
        except json.JSONDecodeError:
            try:
                json_input_list: str = input_customer_list.replace("'", '"')
                input_customer_list = json.loads(json_input_list)
            except json.JSONDecodeError as error_info:
                raise ValueError(f"Некорректный формат данных: {error_info}")
        if isinstance(input_customer_list, list):
            filtered_customer_list = list(filter(lambda customer: customer.get("state") == state, input_customer_list))
        else:
            raise TypeError("Клиентский список не задан")
    elif isinstance(input_customer_list, list):
        filtered_customer_list = list(filter(lambda customer: customer.get("state") == state, input_customer_list))
    else:
        raise TypeError("Клиентский список не задан")
    return filtered_customer_list


def sort_by_date(input_consumer_statement: str | list, sort_order: bool | None = True) -> List:
    """
    Функция возвращает новый список словарей, отсортированный по дате (date).
    """

    if not isinstance(sort_order, bool):
        raise TypeError("Не задан порядок сортировки")
    if isinstance(input_consumer_statement, list):
        pass
    elif isinstance(input_consumer_statement, str):
        try:
            input_consumer_statement = json.loads(input_consumer_statement)
        except json.JSONDecodeError:
            try:
                json_input_statement: str = input_consumer_statement.replace("'", '"')
                input_consumer_statement = json.loads(json_input_statement)
            except json.JSONDecodeError as error_mess:
                raise ValueError(f"Некорректный формат данных: {error_mess}")
        if not isinstance(input_consumer_statement, list):
            raise TypeError("Клиентская ведомость не задана")
    if not input_consumer_statement:
        raise ValueError("Клиентская ведомость пуста")
    valid_date_statement = []
    for consumer in input_consumer_statement:
        if consumer not in input_consumer_statement:
            raise ValueError("Клиентская ведомость пуста")
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
