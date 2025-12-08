import pytest
from pytest import CaptureFixture

from src.decorators import log


def test_log_multi_func(capsys: CaptureFixture[str]) -> None:
    @log(filename=None)
    def process_data(data: list | tuple | set) -> list:
        return [x * 2 for x in data]

    result = process_data(data=(1, 2, 3))
    captured = capsys.readouterr()
    assert captured.out == "process_data ok\n"
    assert result == [2, 4, 6]


def test_log_zero_div(capsys: CaptureFixture[str]) -> None:
    @log(filename=None)
    def get_divide(num_one: int | float, num_two: int | float) -> float:
        if num_two == 0:
            raise ZeroDivisionError("Деление на ноль невозможно!")
        return num_one / num_two

    with pytest.raises(Exception) as error_info:
        get_divide(num_one=5, num_two=0)
    captured_one = capsys.readouterr()
    assert captured_one.out == f"get_divide error: {error_info.value}. Inputs: (), {{'num_one': 5, 'num_two': 0}}\n"
    result = get_divide(num_one=48, num_two=3)
    captured_two = capsys.readouterr()
    assert captured_two.out == "get_divide ok\n"
    assert result == 16


def test_log_with_logging(capsys: CaptureFixture[str]) -> None:
    @log(filename="log.txt")
    def process_data(data: list | tuple | set) -> list:
        return [x * 2 for x in data]

    result = process_data(data=(1, 2, 3))
    logged_file = open("log.txt", "r")
    line_log = logged_file.readline()
    assert line_log == "process_data ok\n"
    assert result == [2, 4, 6]
