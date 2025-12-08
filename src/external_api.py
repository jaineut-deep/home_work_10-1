import os
from datetime import datetime

import requests
from dotenv import load_dotenv


def get_conversation(transaction: dict) -> float | str:
    """Функция возвращает сумму заданной транзакции в рублях"""

    actual_date = transaction.get("date", "")
    try:
        datetime.strptime(actual_date[:10], "%Y-%m-%d").date()
    except (ValueError, TypeError) as error_info:
        raise Exception("Задано некорректное время") from error_info
    fact_amount = transaction.get("operationAmount", {}).get("amount")
    currency_code = transaction.get("operationAmount", {}).get("currency", {}).get("code", {})

    def get_swap_response(currency: str, currency_amount: float, swap_date: str) -> float | str:
        load_dotenv("../.env")
        api_key = os.getenv("API_KEY")
        url = "https://api.apilayer.com/exchangerates_data/convert"
        payload: dict[str, str | float] = {"to": "RUB", "from": currency, "amount": currency_amount, "date": swap_date}
        headers = {"apikey": api_key}
        response = requests.get(url, headers=headers, params=payload)
        status_code = response.status_code
        result = response.json()
        if status_code == 200:
            converted_result = result.get("result", "")
            if isinstance(converted_result, float):
                return converted_result
            else:
                return "Значение отсутствует."
        else:
            return f"Запрос не был успешным. Возможная причина: {response.reason}, {api_key}"

    if currency_code == "RUB":
        return float(fact_amount)
    elif currency_code in ("EUR", "USD"):
        fact_amount = get_swap_response(
            currency=currency_code, currency_amount=fact_amount, swap_date=actual_date[:10]
        )
        if isinstance(fact_amount, float):
            return fact_amount
        else:
            return "Значение отсутствует."
    else:
        return f"Неподдерживаемая валюта: {currency_code}"
