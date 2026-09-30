import httpx

class BaseClient:
    def __init__(self, base_url: str):
        self.client = httpx.Client(base_url=base_url)
    def get(self, url: str):
        return self.client.get(url)
    def post(self, url: str, json: dict):
        return self.client.post(url, json=json)