from clients.base_client import BaseClient

class OperationClient(BaseClient):
    def __init__(self):
        super().__init__(base_url="https://api.sampleapis.com")
    def get_operations(self):
        return self.get("/fakebank/accounts")
    def create_operation(self, operation: dict):
        return self.post("/fakebank/accounts", json=operation)