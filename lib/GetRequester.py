import requests
import json

class GetRequester:
    def __init__(self, url):
        self.url = url
        if not isinstance(url, str):
            raise ValueError("URL must be a string")

    def get_response_body(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return None

    def load_json(self):
        response_body = self.get_response_body()
        if response_body is None:
            return None
        return json.loads(response_body)
