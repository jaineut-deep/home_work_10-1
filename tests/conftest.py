import pytest


@pytest.fixture
def get_string() -> int:
    return 2637874100472419


@pytest.fixture
def get_row() -> int:
    return 75378019746380090000


@pytest.fixture
def get_date_empty() -> str:
    return ""


@pytest.fixture
def get_date_line() -> str:
    return "02:26:18.671407"


@pytest.fixture
def get_empty_meaning() -> list[dict]:
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        }
    ]


@pytest.fixture
def get_currency() -> str:
    return "USD"


@pytest.fixture
def get_number_extra() -> int:
    return 5864537245
