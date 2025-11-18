import re


def get_mask_card_number(card_number: int | type[ValueError]) -> str:
    """
    Функция маскирует номер банковской карты.
    """

    assert isinstance(card_number, int), "Введено некорректное значение карты."
    if str(card_number).isdigit() and (len(str(card_number)) == 16) and card_number is not type[ValueError]:
        mask_card_number = re.sub(r"^(\d{4})(\d{2})(\d{2})(\d{4})(\d{4})$", r"\1 \2** **** \5", str(card_number))
        return mask_card_number
    else:
        return "Введено некорректное значение карты."


def get_mask_account(account_number: int | type[ValueError]) -> str:
    """
    Функция маскирует номер банковского счета.
    """

    assert isinstance(account_number, int), "Введено некорректное значение счета."
    if str(account_number).isdigit() and (len(str(account_number)) == 20) and account_number is not type[ValueError]:
        mask_account = "**" + str(account_number)[-4:]
        return mask_account
    else:
        return "Введено некорректное значение счета."


if __name__ == "__main__":
    print(get_mask_card_number(card_number=next((int(x) for x in [input()] if x.isdigit()), ValueError)))
    print(get_mask_account(account_number=next((int(x) for x in [input()] if x.isdigit()), ValueError)))
