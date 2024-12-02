import requests
from requests.auth import HTTPBasicAuth
import urllib3

# disable self-signed ssl warning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

api_key = "5YJKGVEFPCKJJWSFV9VULCUQ8N11XCTC"
base_url = "https://localhost:8080/api/"

headers = {
    "Authorization": f"Basic {api_key}",
    "Content-Type": "application/xml; charset=UTF-8",
}


def get_blank_schema(endpoint: str):
    response = requests.get(
        f"{base_url}{endpoint}?schema=blank",
        headers=headers,
        auth=HTTPBasicAuth(api_key, ""),
        verify=False
    )
    return response.raw


def send_get(endpoint: str):
    return requests.get(
        f"{base_url}{endpoint}",
        headers=headers,
        auth=HTTPBasicAuth(api_key, ""),
        verify=False
    )


def send_post(payload: str, endpoint: str):
    response = requests.post(
        f"{base_url}{endpoint}",
        headers=headers,
        data=payload.encode('utf-8'),
        auth=HTTPBasicAuth(api_key, ""),
        verify=False
    )

    if response.status_code == 201:
        return response
    else:
        print(f"--------- Failed ({response.status_code}). Payload: ---------\n{payload}")


