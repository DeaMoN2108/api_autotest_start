import pytest
from clients.operations_client import OperationClient

@pytest.fixture
def operation_data():
    return {
        "debit": 100.0,
        "credit": None,
        "category": "food",
        "description": "Обед в кофе",
        "transactionDate": "2024-01-05"
    }

@pytest.fixture
def operations_client():
    return OperationClient()