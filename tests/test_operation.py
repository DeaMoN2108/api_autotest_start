import pytest
from clients.operations_client import OperationClient

@pytest.mark.api
def test_get_operation(operations_client: OperationClient):
    response = operations_client.get_operations()
    response_data = response.json()

    assert len(response_data) > 0
    assert response.status_code == 200

@pytest.mark.api
def test_create_operation(operation_data: dict, operations_client: OperationClient):
    response = operations_client.create_operation(operation_data)
    response_data = response.json()

    assert response.status_code == 201
    assert "id" in response_data
    assert response_data["debit"] == operation_data["debit"]
    assert response_data["credit"] == operation_data["credit"]
    assert response_data["category"] == operation_data["category"]
    assert response_data["description"] == operation_data["description"]
    assert response_data["transactionDate"] == operation_data["transactionDate"]