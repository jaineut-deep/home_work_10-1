import re

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """
    Функция возвращает строку с замаскированным номером карты или счета,
    в зависимости от ввода.
    """

    named_section = re.compile(r"^\b[a-zA-Zа-яА-Я]{2,}\s(?!\s)([a-zA-Zа-яА-Я]{2,}\b\s)?$")
    if named_section.match(account_card[:-16]) and (account_card[-16:]).isdigit():
        card_number = int(account_card[-16:])
        mask_drafted_number = account_card[:-16] + get_mask_card_number(card_number)
    elif named_section.match(account_card[:-20]) and (account_card[-20:]).isdigit():
        card_number = int(account_card[-20:])
        mask_drafted_number = account_card[:-20] + get_mask_account(card_number)
    else:
        mask_drafted_number = str("Wrong account name!")
    return mask_drafted_number


def get_date(unformatted_date: str) -> str:
    """
    Функция возвращает строку с датой в формате 'ДД.ММ.ГГГГ'.
    """

    mask_date = re.compile(r"^(\d{4})-(\d{2})-(\d{2})")
    if mask_date.match(unformatted_date):
        formatted_date = re.sub(mask_date, r"\3.\2.\1", unformatted_date)
        return formatted_date[0:10]
    else:
        return "Неверный формат даты!"


if __name__ == "__main__":
    print(mask_account_card(input()))
    print(get_date(input()))
