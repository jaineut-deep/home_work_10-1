import re
from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """
    Функция возвращает строку с замаскированным номером карты или счета,
    в зависимости от ввода.
    """

    named_section = re.compile(r"^\b[a-zA-Z]{2,}\s(?!\s)([a-zA-Z]{2,}\b\s)?$")
    named_section_rus = re.compile(r"^\b[а-яА-Я]{4}\b\s$")
    if named_section.match(account_card[:-16]) and (account_card[-16:]).isdigit():
        card_number_int = int(account_card[-16:])
        if get_mask_card_number(card_number_int) == "Введено некорректное значение карты.":
            mask_drafted_number = get_mask_card_number(card_number_int)
        else:
            mask_drafted_number = account_card[:-16] + get_mask_card_number(card_number_int)
        return mask_drafted_number
    elif named_section_rus.match(account_card[:-20]) and (account_card[-20:]).isdigit():
        card_number_int = int(account_card[-20:])
        if get_mask_account(card_number_int) == "Введено некорректное значение счета.":
            mask_drafted_number = get_mask_account(card_number_int)
        else:
            mask_drafted_number = account_card[:-20] + get_mask_account(card_number_int)
        return mask_drafted_number
    else:
        mask_drafted_number = str("Неверное значение учетной записи.")
        return mask_drafted_number


def get_date(unformatted_date: str) -> str:
    """
    Функция возвращает строку с датой в формате 'ДД.ММ.ГГГГ'.
    """

    if re.match(r"^(\d{4})-(\d{2})-(\d{2})", unformatted_date):
        try:
            datetime.strptime(unformatted_date[:10], "%Y-%m-%d").date()
        except (ValueError, TypeError):
            return "Неверный формат даты."
        else:
            formatted_date = re.sub(r"^(\d{4})-(\d{2})-(\d{2})", r"\3.\2.\1", unformatted_date)
        return formatted_date[0:10]
    else:
        return "Неверный формат даты."


if __name__ == "__main__":
    print(mask_account_card(input()))
    print(get_date(input()))
