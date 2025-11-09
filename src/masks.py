import re


def get_mask_card_number(card_number: int) -> str:
    """
    Функция маскирует номер банковской карты.
    """

    mask_card_number = re.sub(r"^(\d{4})(\d{2})(\d{2})(\d{4})(\d{4})$", r"\1 \2** **** \5", str(card_number))
    return mask_card_number


def get_mask_account(account_number: int) -> str:
    """
    Функция маскирует номер банковского счета.
    """

    mask_account = "**" + str(account_number % 10000)
    return mask_account


if __name__ == "__main__":
    print(get_mask_card_number(int(input())))
    print(get_mask_account(int(input())))
