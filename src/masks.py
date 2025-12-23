import logging
import os
import re

base_dir = os.path.dirname(os.path.dirname(__file__))
path_to_log = base_dir + "/logs/module_masks.log"
masks_logger = logging.getLogger(__name__)
if not masks_logger.handlers:
    file_handler = logging.FileHandler(path_to_log, mode="w")
    file_formatter = logging.Formatter("%(asctime)s - %(module)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(file_formatter)
    masks_logger.addHandler(file_handler)
    masks_logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str | type[ValueError] | int) -> str:
    """
    Функция маскирует номер банковской карты.
    """

    masks_logger.info(f"Начало работы программы маскировки номера карты. Введено значение: {card_number}")
    if str(card_number).isdigit() and (len(str(card_number)) == 16) and (card_number is not type[ValueError]):
        mask_card_number = re.sub(r"^(\d{4})(\d{2})(\d{2})(\d{4})(\d{4})$", r"\1 \2** **** \5", str(card_number))
        masks_logger.info(f"Номер карты успешно замаскирован: {mask_card_number}")
        return mask_card_number
    else:
        masks_logger.error("Введено некорректное значение карты.")
        return "Введено некорректное значение карты."


def get_mask_account(account_number: str | type[ValueError] | int) -> str:
    """
    Функция маскирует номер банковского счета.
    """

    masks_logger.info(f"Начало работы программы маскировки номера счета. Введено значение: {account_number}")
    if str(account_number).isdigit() and (len(str(account_number)) == 20) and account_number is not type[ValueError]:
        mask_account = "**" + str(account_number)[-4:]
        masks_logger.info(f"Номер счета успешно замаскирован: {mask_account}")
        return mask_account
    else:
        masks_logger.error("Введено некорректное значение счета.")
        return "Введено некорректное значение счета."
