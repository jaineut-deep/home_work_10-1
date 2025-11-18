import pytest


@pytest.fixture
def get_string() -> int:
    return 2637874100472419


@pytest.fixture
def get_row() -> int:
    return 75378019746380090000


@pytest.fixture
def get_date_empty() -> str:
    return ""


@pytest.fixture
def get_date_line() -> str:
    return "02:26:18.671407"
