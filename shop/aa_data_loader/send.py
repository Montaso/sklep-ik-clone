import os

import requests
from requests.auth import HTTPBasicAuth
import urllib3

# disable self-signed ssl warning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

api_key = "NHVHC529QBYGLR338W652HNF16LNH5ER"
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


def download_image(image_url: str, file_name: str):
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(file_name, 'wb') as file:
            file.write(response.content)
        return True
    else:
        print(f"Failed to download image from {image_url}. Status Code: {response.status_code}")
        return False


def upload_product_image(product_id: int, image_file_path: str):
    image_upload_url = f"{base_url}images/products/{product_id}"

    if not os.path.exists(image_file_path):
        print(f"File does not exist: {image_file_path}")
        return

    with open(image_file_path, 'rb') as image_file:
        files = {"image": (os.path.basename(image_file_path), image_file, 'image/jpeg')}
        response = requests.post(image_upload_url, files=files, headers={
            "Authorization": f"Basic {api_key}"
        }, auth=HTTPBasicAuth(api_key, ""), verify=False)

    if response.status_code == 200:
        print(f"Image uploaded successfully for product {product_id}!")
    else:
        print(f"Failed to upload image for product {product_id}. Status Code: {response.status_code}")


def upload_product_images(product_id: int, img_uris: list):
    for img_url in img_uris:
        img_url = img_url.strip('[]\'\" ')
        file_name = img_url.split("/")[-1]

        if download_image(img_url, file_name):
            upload_product_image(product_id, file_name)
            os.remove(file_name)
            print(f"Uploaded image {img_url} successfully.")
        else:
            print(f"Skipping upload for {img_url} due to download failure.")


def send(payload: str, endpoint: str):
    response = requests.post(
        f"{base_url}{endpoint}",
        headers=headers,
        data=payload.encode('utf-8'),
        auth=HTTPBasicAuth(api_key, ""),
        verify=False
    )

    return response

def send_get(endpoint: str):
    return requests.get(
        f"{base_url}{endpoint}",
        headers=headers,
        auth=HTTPBasicAuth(api_key, ""),
        verify=False,
        params={'display': '[id,name]'}
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
        print(f"--------- error3 ---------\n{payload}")


