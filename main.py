import os
import sys

from src.generators import filter_by_currency
from src.utils import get_operations
from src.transactions_import import get_operations_data
from src.widget import mask_account_card, get_date
from src.processing import filter_by_state, sort_by_date
from src.filters import get_process_search, process_bank_operations


def main():
    """Функция предоставляет пользовательский интерфейс и возвращает данные по операциям в соответствии
    с условиями выборки и сортировками указанными пользователем.
    """

    strict_path = os.path.dirname(__file__)
    file_json_path = strict_path + "/data/operations.json"
    file_csv_path = strict_path + "/data/transactions.csv"
    file_xlsx_path = strict_path + "/data/transactions_excel.xlsx"
    greeting = """
        Привет! Добро пожаловать в программу работы 
        с банковскими транзакциями."""
    print(greeting)
    while True:
        print(
            """
        Выберите необходимый пункт меню:
        1. Получить информацию о транзакциях из JSON-файла
        2. Получить информацию о транзакциях из CSV-файла
        3. Получить информацию о транзакциях из XLSX-файла
        """
        )
        user_num = input()
        if not user_num.isdigit():
            print(f"Статус выбора {user_num} недоступен.")
            continue
        elif int(user_num) in [1, 2, 3]:
            break
    if int(user_num) == 1:
        print("Для обработки выбран JSON-файл.")
        transactions_data = get_operations(file_json_path)
    elif int(user_num) == 2:
        print("Для обработки выбран CSV-файл.")
        transactions_data = get_operations_data(file_csv_path)
    else:
        print("Для обработки выбран XLSX-файл.")
        transactions_data = get_operations_data(file_xlsx_path)
    while True:
        print(
            """
        Введите статус, по которому необходимо выполнить фильтрацию. 
        Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"""
        )
        user_tell_state = input()
        state_process = user_tell_state.strip().upper()
        if state_process in ["EXECUTED", "CANCELED", "PENDING"]:
            break
        else:
            print(f'Статус операции "{state_process}" недоступен.')
            continue
    print(f'Операции отфильтрованы по "{state_process}".')
    date_mark_ascending = None
    word_describe_search = None
    while True:
        print("Отсортировать операции по дате? Да/Нет")
        date_mark = input().lower()
        if date_mark == "да":
            break
        elif date_mark == "нет":
            break
        else:
            print(f'Статус выбора "{date_mark}" недоступен')
            continue
    if date_mark == "да":
        while True:
            print("Отсортировать по возрастанию или по убыванию? по возрастанию/по убыванию")
            date_mark_ascending = input().lower()
            if date_mark_ascending == "по возрастанию":
                break
            elif date_mark_ascending == "по убыванию":
                break
            else:
                print(f'Статус выбора "{date_mark_ascending}" недоступен')
                continue
    while True:
        print("Выводить только рублевые транзакции? Да/Нет")
        only_rub_mark = input().lower()
        if only_rub_mark == "да":
            break
        elif only_rub_mark == "нет":
            break
        else:
            print(f'Статус выбора "{only_rub_mark}" недоступен')
            continue
    while True:
        print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
        word_describe = input().lower()
        if word_describe == "да":
            print("Введите искомое в описании слово:\n")
            word_describe_search = input().lower()
            break
        elif word_describe == "нет":
            break
        else:
            print(f'Статус выбора "{word_describe}" недоступен')
            continue
    filtered_state_data = filter_by_state(transactions_data, state_process)
    if date_mark_ascending == "по убыванию":
        date_mark_ascending = True
        filtered_date_data = sort_by_date(filtered_state_data, date_mark_ascending)
    elif date_mark_ascending == "по возрастанию":
        date_mark_ascending = False
        filtered_date_data = sort_by_date(filtered_state_data, date_mark_ascending)
    else:
        filtered_date_data = filtered_state_data
    if only_rub_mark == "да":
        only_rub_mark = "RUB"
        filtered_rub_data = filter_by_currency(filtered_date_data, only_rub_mark)
    else:
        filtered_rub_data = filtered_date_data
    if word_describe_search:
        filtered_search_data = get_process_search(filtered_rub_data, word_describe_search)
    else:
        filtered_search_data = filtered_rub_data
    if (filtered_search_data == []) or (filtered_search_data is None):
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    categories_list = []
    transactions_est = process_bank_operations(filtered_search_data, categories_list)
    print("Распечатываю итоговый список транзакций...")
    print(f"Всего банковских операций в выборке: {sum(transactions_est.values())}")
    for operation in filtered_search_data:
        transfer_date = get_date(operation.get("date"))
        transfer_description = operation.get("description")
        transfer_to = mask_account_card(operation.get("to"))
        amount = operation.get("operationAmount").get("amount") if operation.get("operationAmount") else operation.get("amount")
        currency_code = operation.get("operationAmount", {}).get("currency", {}).get("code") if operation.get("operationAmount") else operation.get("currency_code")
        transfer_from = ("\n" + mask_account_card(operation.get("from")) + " -> ") if isinstance(operation.get("from"), str) and operation.get("from").strip() else "\n"
        print(f"{transfer_date} {transfer_description}{transfer_from}{transfer_to}\nСумма: {amount} {currency_code}")
    sys.exit(0)


if __name__ == "__main__":
    print(main())
