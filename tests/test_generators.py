from collections.abc import Iterator

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.mark.parametrize(
    "expression, param_money, output_iter",
    [
        (
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                },
                {
                    "id": 142264268,
                    "state": "EXECUTED",
                    "date": "2019-04-04T23:20:05.206878",
                    "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                },
                {
                    "id": 142271268,
                    "state": "EXECUTED",
                    "date": "2019-05-04T21:10:05.206878",
                    "operationAmount": {"amount": "79114.93", "currency": {"name": "RUB", "code": "RUB"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                },
            ],
            "USD",
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                },
                {
                    "id": 142264268,
                    "state": "EXECUTED",
                    "date": "2019-04-04T23:20:05.206878",
                    "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                },
            ],
        )
    ],
)
def test_filter_currency(expression: list[dict], param_money: str, output_iter: Iterator[dict]) -> None:
    result = list(filter_by_currency(expression, param_money))
    assert result == output_iter


def test_not_currency(get_empty_meaning: list[dict], get_currency: str) -> None:
    result = list(filter_by_currency(get_empty_meaning, get_currency))
    assert result == []


@pytest.mark.parametrize(
    "list_transfer, expected",
    [
        (
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                },
                {
                    "id": 142264268,
                    "state": "EXECUTED",
                    "date": "2019-04-04T23:20:05.206878",
                    "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                },
                {
                    "id": 142271268,
                    "state": "EXECUTED",
                    "date": "2019-05-04T21:10:05.206878",
                    "operationAmount": {"amount": "79114.93", "currency": {"name": "RUB", "code": "RUB"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                },
                {
                    "id": 142264268,
                    "state": "EXECUTED",
                    "date": "2019-06-03T23:20:05.206878",
                    "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод с карты на карту",
                    "from": "Счет 19708645235787258542",
                    "to": "Счет 75651667383060284188",
                },
                {
                    "id": 142264268,
                    "state": "EXECUTED",
                    "date": "2020-01-04T23:00:05.206878",
                    "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                },
            ],
            [
                "Перевод организации",
                "Перевод со счета на счет",
                "Перевод со счета на счет",
                "Перевод с карты на карту",
                "Перевод организации",
            ],
        ),
        (
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                },
                {
                    "id": 142264268,
                    "state": "EXECUTED",
                    "date": "2019-04-04T23:20:05.206878",
                    "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                },
                {
                    "id": 142271268,
                    "state": "EXECUTED",
                    "date": "2019-05-04T21:10:05.206878",
                    "operationAmount": {"amount": "79114.93", "currency": {"name": "RUB", "code": "RUB"}},
                    "description": "",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                },
            ],
            [
                "Перевод организации",
                "Перевод со счета на счет",
            ],
        ),
    ],
)
def test_transaction_descriptions(list_transfer: list[dict], expected: Iterator[str | type[KeyError]]) -> None:
    result = list(transaction_descriptions(list_transfer))
    assert result == expected


@pytest.mark.parametrize(
    "number_one, number_two, output_numbers",
    [
        (
            1,
            7,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
                "0000 0000 0000 0006",
                "0000 0000 0000 0007",
            ],
        ),
        (
            2398,
            2400,
            [
                "0000 0000 0000 2398",
                "0000 0000 0000 2399",
                "0000 0000 0000 2400",
            ],
        ),
        (
            11,
            11,
            [
                "0000 0000 0000 0011",
            ],
        ),
    ],
)
def test_number_generator(number_one: int, number_two: int, output_numbers: Iterator[str | type[ValueError]]) -> None:
    result = list(card_number_generator(number_one, number_two))
    assert result == output_numbers


def test_number_generator_zero() -> None:
    with pytest.raises(ValueError) as exc_info:
        list(card_number_generator(0, 10))
    assert str(exc_info.value) == "Значения вне диапазона номеров."


def test_number_generator_outer() -> None:
    with pytest.raises(ValueError) as exc_info:
        list(card_number_generator(9999999999999997, 10000000000000001))
    assert str(exc_info.value) == "Значения вне диапазона номеров."


def test_number_generator_inverse(get_number_extra: int) -> None:
    result = list(card_number_generator(get_number_extra, get_number_extra))
    assert result == ["0000 0058 6453 7245"]
