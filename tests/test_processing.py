import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize(
    "user_input, status, total_output",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        ),
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {},
            ],
            "EXECUTED",
            [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}],
        ),
    ],
)
def test_filter_by_state(user_input: str, status: str, total_output: list) -> None:
    assert filter_by_state(user_input, status) == total_output


@pytest.mark.parametrize(
    "user_input, sorting, total_output",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            True,
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            False,
            [
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            ],
        ),
    ],
)
def test_sort_by_date(user_input: str, sorting: bool, total_output: list[dict]) -> None:
    assert sort_by_date(user_input, sorting) == total_output


def test_filter_incorrect() -> None:
    with pytest.raises(ValueError) as exc_info:
        filter_by_state(
            "[{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},"
            "{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}]",
            "Date",
        )
    assert str(exc_info.value) == "Не задан критерий фильтрации"


def test_filter_wrong_list() -> None:
    with pytest.raises(TypeError) as exc_info:
        filter_by_state("{}", "EXECUTED")
    assert str(exc_info.value) == "Клиентский список не задан"


def test_sort_incorrect() -> None:
    with pytest.raises(TypeError) as exc_info:
        sort_by_date(
            "[{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},"
            "{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}]",
            None,
        )
    assert str(exc_info.value) == "Не задан порядок сортировки"


def test_sort_absence() -> None:
    with pytest.raises(ValueError) as exc_info:
        sort_by_date("[]", True)
    assert str(exc_info.value) == "Клиентская ведомость пуста"


def test_sort_wrong_date() -> None:
    with pytest.raises(ValueError) as exc_info:
        sort_by_date(
            "[{'id': 939719570, ''state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},"
            "{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}]",
            True,
        )
    assert str(exc_info.value) == "Некорректный формат данных: Expecting ':' delimiter: line 1 column 22 (char 21)"
