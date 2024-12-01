from xml_payloads import *
from send import send, get_blank_schema

payload = add_category_payload(11, 1, "druty", "podpięcie elektryczne pod nie", "druty-shop")
send(payload, "categories")

# payload = add_product_payload(10, 14.99, True, "test-prod-name",
#                              "https://localhost:8080/test", "test-dscrb", "test-short-dscrb")
# send(payload, "products")

