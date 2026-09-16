import requests

from config.settings import API_KEY


BASE_URL = "https://finnhub.io/api/v1"

class FinnhubAPI:
    def get_company_profile(self, symbol):

        url = f"{BASE_URL}/stock/profile2"

        params = {
            "symbol": symbol,
            "token": API_KEY
        }

        response = requests.get(
            url,
            params=params,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        return data
    
    
    def get_quote(self, symbol):

        url = f"{BASE_URL}/quote"

        params = {
            "symbol": symbol,
            "token": API_KEY
        }

        response = requests.get(
            url,
            params=params,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        return data