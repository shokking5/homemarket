#!/usr/bin/env python3

from sign import sign_message
from sys import path
from time import sleep
import requests

'''
    Данная функция служит для тестирования работы сервера.
    Она имитирует работу yandex money - оповещений и передает
    POST запрос с теми же параметрами. После обращения, сервер
    заносит данные в базу и хранит их до момента, пока бот
    не запросит эти данные функцией check_payment. Для подтверждения
    каждое сообщение должно быть подписано секретом.
    Как подписывается сообщение, можно посмотреть в файле sign.py
    или в документации yandex money:

    https://yandex.ru/dev/money/doc/payment-buttons/reference/notifications-docpage/
'''

path.append("..")
from configloader import config

SERVER_URL = config["Config"]["server_url"]
SECRET = config["Credit Card"]["yandex_money_secret"]

def set_payment(server_url, amount, label, path="/set_payment/"):
    server_url = server_url if server_url else SERVER_URL
    signed_message = sign_message(label, amount)
    resp = requests.post(server_url + path, data = signed_message).text
    return resp


if __name__ == "__main__":
    print(set_payment(input("server_url (may skeep) > ").strip(),
                      input("amount > ").strip(),
                      input("lable > ").strip()))
