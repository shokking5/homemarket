#!/usr/bin/env python3

from sign import hash_secret
from sys import path
from time import sleep
import requests

'''
    Данная функция позволяет получить список всех ожидающих
    подтверждения заказов. Возвращает информацию в следующем
    виде: {uid}:{order_id}:{amount}.
    Сервер проверяет только секрет, хешированный алгоритмом
    sha1 и переданный POST запросом в виде голой строки.
'''


path.append("..")
from configloader import config

SERVER_URL = config["Config"]["server_url"]
SECRET = config["Credit Card"]["yandex_money_secret"]

def get_orders(path="/get_orders/", attempts=10):
    hashed_secret = hash_secret(SECRET)
    for i in range(attempts):
        resp = requests.post(SERVER_URL + path, data = hashed_secret).text
        if resp:
            return resp
        sleep(1)
    return "Empty"


if __name__ == "__main__":
    print(get_orders())
