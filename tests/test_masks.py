import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_mask_number(get_string: int, get_row: int) -> None:
    assert get_mask_card_number(get_string) == "2637 87** **** 2419"
    assert get_mask_card_number(get_row) == "Введено некорректное значение карты."


def test_mask_account(get_string: int, get_row: int) -> None:
    assert get_mask_account(get_string) == "Введено некорректное значение счета."
    assert get_mask_account(get_row) == "**0000"


def test_mask_number_error() -> None:
    with pytest.raises(ValueError) as exc_info:
        int("793946GFTqg462mj")
    assert "invalid literal for int()" in str(exc_info.value)
    with pytest.raises(ValueError) as exc_info:
        int("")
    assert "invalid literal for int()" in str(exc_info.value)


def test_mask_account_error() -> None:
    with pytest.raises(ValueError) as exc_info:
        int("238716dGetru879H73V3")
    assert "invalid literal for int()" in str(exc_info.value)
    with pytest.raises(ValueError) as exc_info:
        int("")
    assert "invalid literal for int()" in str(exc_info.value)
