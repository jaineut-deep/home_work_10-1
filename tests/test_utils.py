import json
import pytest
from unittest.mock import mock_open, patch

from src.utils import get_operations


@pytest.mark.parametrize(
    "input_value, output_value",
    [
        (
            json.dumps([
                    {
                        "id": 863064926,
                        "state": "EXECUTED",
                        "date": "2019-12-08T22:46:21.935582",
                        "operationAmount": {"amount": "41096.24", "currency": {"name": "USD", "code": "USD"}},
                        "description": "Открытие вклада",
                        "to": "Счет 90424923579946435907",
                    },
                    {
                        "id": 594226727,
                        "state": "CANCELED",
                        "date": "2018-09-12T21:27:25.241689",
                        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
                        "description": "Перевод организации",
                        "from": "Visa Platinum 1246377376343588",
                        "to": "Счет 14211924144426031657",
                    },
            ])
                ,
            [
                {
                    "id": 863064926,
                    "state": "EXECUTED",
                    "date": "2019-12-08T22:46:21.935582",
                    "operationAmount": {"amount": "41096.24", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Открытие вклада",
                    "to": "Счет 90424923579946435907",
                },
                {
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                    "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод организации",
                    "from": "Visa Platinum 1246377376343588",
                    "to": "Счет 14211924144426031657",
                }
            ]
        ), (json.dumps([]), []), (None, [])])


def test_file_operations(input_value: str, output_value: list) -> None:
    file_path = "dummy_file.json"
    mock_file_content = mock_open(read_data=input_value)
    with patch("builtins.open", mock_file_content):
        with patch("os.path.isfile", return_value=True, encoding="utf-8"):
            result = get_operations(file_path)
    assert result == output_value
