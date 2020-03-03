#!/usr/bin/env python3

from sign import hash_secret
from sys import path
from time import sleep
import requests

'''
    Данная функция позволяет получить список всех запросов
    на сервер. Возвращает информацию в следующем
    виде: {datetime}:{label}:{amount}\n{method}.
    Сервер проверяет только секрет, хешированный алгоритмом
    sha1 и переданный POST запросом в виде голой строки.
'''


path.append("..")
from configloader import config

SERVER_URL = config["Config"]["server_url"]
SECRET = config["Credit Card"]["yandex_money_secret"]

def get_orders(server_url, path="/get_backup/", attempts=10):
    hashed_secret = hash_secret(SECRET)
    server_url = server_url if server_url else SERVER_URL
    resp = requests.post(server_url + path, data = hashed_secret).text
    return resp

if __name__ == "__main__":
    print(get_orders(input("server url (may skeep) > ").strip()))
