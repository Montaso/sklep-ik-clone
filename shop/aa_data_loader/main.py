from xml_payloads import *
from send import send, get_blank_schema

#payload = add_category_payload(2, 1, "test_name", "test_desc", "test_link")
#send(payload, "categories")

#payload = add_product_payload(10, 14.99, True, "test-prod-name",
#                              "https://localhost:8080/test", "test-dscrb", "test-short-dscrb")
#send(payload, "products")

schema = get_blank_schema("products")
print(schema)

