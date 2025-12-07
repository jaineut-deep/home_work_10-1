import os
import requests
from datetime import datetime
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
    def get_swap_response(currency: str, currency_amount: float, swap_date: str) -> dict | str:
        load_dotenv("../.env")
        api_key = os.getenv("API_KEY")
        url = "https://api.apilayer.com/exchangerates_data/convert"
        payload = {"to": "RUB", "from": currency, "amount": currency_amount, "date": swap_date}
        headers = {"apikey": api_key}
        response = requests.get(url, headers=headers, params=payload)
        status_code = response.status_code
        result = response.json()
        if status_code == 200:
            return result.get("result")
        else:
            return f"Запрос не был успешным. Возможная причина: {response.reason}, {api_key}"
    if currency_code == "RUB":
        fact_amount = float(fact_amount)
    elif currency_code == "EUR":
        fact_amount = get_swap_response(currency=currency_code, currency_amount=fact_amount, swap_date=actual_date[:10])
    elif currency_code == "USD":
        fact_amount = get_swap_response(currency=currency_code, currency_amount=fact_amount, swap_date=actual_date[:10])
    return fact_amount
