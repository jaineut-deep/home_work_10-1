from functools import wraps
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """
    Функция-декоратор автоматически логирует выполнение функций, и их результаты или возникшие ошибки.
    Декоратор принимает необязательный аргумент filename - файл журнала логов.
    """

    def logging_of_function(function: Callable) -> Callable:
        @wraps(function)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            if filename is None:
                try:
                    result = function(*args, **kwargs)
                    print(f"{function.__name__} ok")
                    return result
                except Exception as error_info:
                    print(f"{function.__name__} error: {error_info}. Inputs: {args}, {kwargs}")
                    raise
            else:
                with open(filename, "a", encoding="utf-8") as output_file:
                    try:
                        result = function(*args, **kwargs)
                        output_file.write(f"{function.__name__} ok\n")
                        return result
                    except Exception as error_info:
                        output_file.write(f"{function.__name__} error: {error_info}. Inputs: {args}, {kwargs}\n")
                        raise

        return wrapper

    return logging_of_function
