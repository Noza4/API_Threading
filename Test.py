import requests
import json
import threading


def store_info(link):
    response = requests.get(link)
    response = response.json()
    with open("data.json", "a") as file:
        json.dump(response, file)
        file.write('\n')


ls_threads = []
ls_products = []
for i in range(1, 101):
    product = f"https://dummyjson.com/products/{i}"
    ls_products.append(product)

for product in ls_products:
    thread = threading.Thread(target=store_info, daemon=True, args=(product, ))
    thread.start()
    ls_threads.append(thread)

for thread in ls_threads:
    thread.join()
