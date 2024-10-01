import requests

from orrnob_drops_automation import base
from core.headers import headers


def get_token(data, proxies=None):
    url = "https://www.binance.com/bapi/growth/v1/friendly/growth-paas/third-party/access/accessToken"
    payload = {"queryString": data, "socialType": "telegram"}

    try:
        response = requests.post(
            url=url, headers=headers(), json=payload, proxies=proxies, timeout=20
        )
        data = response.json()
        token = data["data"]["accessToken"]
        return token
    except:
        return None
