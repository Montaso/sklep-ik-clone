from xml_payloads import *
from send import send, get_blank_schema

# payload = add_category_payload(2, 1, "test_name", "test_desc", "test_link")
# send(payload, "categories")

payload = add_product_payload(4, 20.01, True, "ultra-test",
                              "https://localhost:8080/test", "test-dscrb",
                              "test-short-dscrb", 4, 1)
send(payload, "products")



