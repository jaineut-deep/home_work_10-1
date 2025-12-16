from src.utils import get_operations
from src.transactions_import import get_operations_data
from src.widget import mask_account_card, get_date
from src.processing import filter_by_state, sort_by_date


def main():
    """Функция возвращает данные по операциям"""

    file_json_path = "../data/operations.json"
    file_csv_path = "../data/transactions.csv"
    file_xlsx_path = "../data/transactions_excel.xlsx"
    greeting = """
        Привет! Добро пожаловать в программу работы 
        с банковскими транзакциями."""
    print(greeting)
    while True:
        print("""
        Выберите необходимый пункт меню:
        1. Получить информацию о транзакциях из JSON-файла
        2. Получить информацию о транзакциях из CSV-файла
        3. Получить информацию о транзакциях из XLSX-файла
        """)
        user_num = input()
        if not user_num.isdigit():
            print(f"Статус выбора {user_num} недоступен.")
            continue
        elif int(user_num) in [1, 2, 3]:
            break
    menu_point = int(user_num)
    if menu_point == 1:
        print("Для обработки выбран JSON-файл.")
        transactions_data = get_operations(file_json_path)
    elif menu_point == 2:
        print("Для обработки выбран CSV-файл.")
        transactions_data = get_operations_data(file_csv_path)
    else:
        print("Для обработки выбран XLSX-файл.")
        transactions_data = get_operations_data(file_xlsx_path)
    while True:
        print("""
        Введите статус, по которому необходимо выполнить фильтрацию. 
        Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING""")
        user_tell = input()
        state_process = user_tell.strip().upper()
        if state_process in ["EXECUTED", "CANCELED", "PENDING"]:
            break
        else:
            print(f"Статус операции \"{state_process}\" недоступен.")
            continue
    filtered_data = filter_by_state(transactions_data, state_process)
    print(f"Операции отфильтрованы по \"{state_process}\".")
    print("Отсортировать операции по дате? Да/Нет")
    date_mark = input()
    print("Отсортировать по возрастанию или по убыванию даты? по возрастанию/по убыванию")
    ascending_mark = input()
    print("Выводить только рублевые транзакции? Да/Нет")
    only_rub_mark = input()
    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    word_describe = input()
    print("Распечатываю итоговый список транзакций...")
    print(f"Всего банковских операций в выборке: {transactions_num}")

    print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")



# 12.11.2019 Перевод с карты на карту
# MasterCard 7771 27** **** 3727 -> Visa Platinum 1293 38** **** 9203
# Сумма: 130 USD
#
# 18.07.2018 Перевод организации
# Visa Platinum 7492 65** **** 7202 -> Счет **0034
# Сумма: 8390 руб.

print(main())