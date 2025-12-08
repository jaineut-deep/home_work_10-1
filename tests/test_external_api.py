from unittest.mock import Mock, patch

from src.external_api import get_conversation


@patch("src.external_api.requests.get")
@patch("src.external_api.load_dotenv")
def test_get_conversation(mock_requests: Mock, mock_load_dotenv: Mock) -> None:
    mock_load_dotenv.return_value = None
    transaction = {
        "id": 587085106,
        "state": "EXECUTED",
        "date": "2018-03-23T10:45:06.972075",
        "operationAmount": {"amount": 48223.05, "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Открытие вклада",
        "to": "Счет 41421565395219882431",
    }
    result = get_conversation(transaction)
    assert result == 48223.05
    mock_requests.assert_not_called()


@patch("requests.get")
def test_get_conversation_usd(mock_requests_get: Mock) -> None:
    transaction = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": 8221.37, "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    }
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"result": 520543.416119}
    mock_response.reason = "OK"
    mock_requests_get.return_value = mock_response

    result = get_conversation(transaction)

    assert result == 520543.416119
    mock_requests_get.assert_called_once()


@patch("requests.get")
def test_get_conversation_eur(mock_requests_get: Mock) -> None:
    transaction = {
        "id": 41471229,
        "state": "EXECUTED",
        "date": "2020-05-03T18:35:29.512364",
        "operationAmount": {"amount": 1243.17, "currency": {"name": "EUR", "code": "EUR"}},
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726628",
        "to": "Счет 35383033475547895560",
    }
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"result": 102811.27288}
    mock_response.reason = "OK"
    mock_requests_get.return_value = mock_response

    result = get_conversation(transaction)

    assert result == 102811.27288
    mock_requests_get.assert_called_once()
