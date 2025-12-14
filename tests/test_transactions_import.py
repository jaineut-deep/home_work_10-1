import os.path
from unittest.mock import Mock, patch

import pytest
from pandas.errors import EmptyDataError

from src.transactions_import import get_operations_data


@pytest.mark.parametrize(
    "input_value, output_value, mock_value",
    [
        (
            "file_name.csv",
            [{"user": "John", "age": 22, "city": "London"}],
            [{"user": "John", "age": 22, "city": "London"}],
        ),
        (
            "file_name.xlsx",
            [{"user": "Victor", "age": 31, "city": "Edinburgh"}],
            [{"user": "Victor", "age": 31, "city": "Edinburgh"}],
        ),
        (
            "file_name.xls",
            [{"user": "Marissa", "age": 25, "city": "Hampshire"}],
            [{"user": "Marissa", "age": 25, "city": "Hampshire"}],
        ),
        ("file_name.ls", [], []),
    ],
)
def test_spreadsheet_operations(input_value: str, output_value: list, mock_value: list) -> None:
    mock_data = Mock()
    mock_data.to_dict.return_value = mock_value
    with (
        patch("src.transactions_import.pd.read_csv") as mock_csv_read,
        patch("src.transactions_import.pd.read_excel") as mock_excel_read,
    ):
        _, file_ext = os.path.splitext(input_value)
        if file_ext == ".csv":
            mock_csv_read.return_value = mock_data
        elif file_ext in [".xlsx", ".xls"]:
            mock_excel_read.return_value = mock_data
        result = get_operations_data(input_value)
        assert result == output_value
        if file_ext == ".csv":
            mock_csv_read.assert_called_once_with(input_value, delimiter=";")
            mock_data.to_dict.assert_called_once_with(orient="records")
        elif file_ext in [".xlsx", ".xls"]:
            mock_excel_read.assert_called_once_with(input_value)
            mock_data.to_dict.assert_called_once_with(orient="records")


@pytest.mark.parametrize("input_data, data_error", [("example.csv", "ValueError"), ("example.xlsx", "StopIteration")])
def test_spreadsheet_errors(input_data: str, data_error: str, capsys: pytest.CaptureFixture) -> None:
    _, file_ext = os.path.splitext(input_data)
    if file_ext == ".csv":
        with patch("src.transactions_import.pd.read_csv", side_effect=ValueError):
            result = get_operations_data(input_data)
            assert result == []

            captured = capsys.readouterr()
            assert captured.out == "Несоответствие числа столбцов строкам или ошибка преобразования\n"
    elif file_ext == ".xlsx":
        with patch("src.transactions_import.pd.read_excel", side_effect=EmptyDataError):
            result = get_operations_data(input_data)
            assert result == []

            captured = capsys.readouterr()
            assert captured.out == "Файл пуст или не содержит заголовков\n"
