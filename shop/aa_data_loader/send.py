import requests
from requests.auth import HTTPBasicAuth
import urllib3

# disable self-signed ssl warning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

api_key = "5YJKGVEFPCKJJWSFV9VULCUQ8N11XCTC"
base_url = "https://localhost:8080/api/"

headers = {
    "Content-Type": "application/xml"
}


def get_blank_schema(endpoint: str):
    response = requests.get(
        f"{base_url}{endpoint}?schema=blank",
        headers=headers,
        auth=HTTPBasicAuth(api_key, ""),
        verify=False
    )
    return response.raw


def send(payload: str, endpoint: str):
    response = requests.post(
        f"{base_url}{endpoint}",
        data=payload,
        headers=headers,
        auth=HTTPBasicAuth(api_key, ""),
        verify=False
    )

    if response.status_code // 100 == 2:
        print(f"Operation worked ({response.status_code})")
    else:
        print(f"Operation terminated with code {response.status_code}")
