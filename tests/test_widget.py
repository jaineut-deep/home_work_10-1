import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "user_input, overall_output",
    [
        ("MasterCard 79394642378564100096", "Неверное значение учетной записи."),
        ("MasterCard 1751287645321345", "MasterCard 1751 28** **** 1345"),
        ("Счет 79394642378564100096", "Счет **0096"),
        ("Счет 1751287645321345", "Неверное значение учетной записи."),
    ],
)
def test_mask_card(user_input: str, overall_output: str) -> None:
    assert mask_account_card(user_input) == overall_output


def test_get_date(get_date_empty: str, get_date_line: str) -> None:
    assert get_date(get_date_empty) == "Неверный формат даты."
    assert get_date(get_date_line) == "Неверный формат даты."


@pytest.mark.parametrize(
    "user_entry, total_output",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2020-01-30T13:01:34.215039", "30.01.2020"),
        ("2001-02-29T02:26:18.675607", "Неверный формат даты."),
        ("2013/03/28T10:01:34.264039", "Неверный формат даты."),
    ],
)
def test_date_param(user_entry: str, total_output: str) -> None:
    assert get_date(user_entry) == total_output
