#!/usr/bin/env python3

from sign import sign_message
from sys import path
from time import sleep
import requests

'''
    C помощью данной функции можно обратититься на сервер,
    чтобы получить статус заказа необходимого пользователя.
    Если пользователь оплатил заказ в нужном размере, то
    сервер возвращает True и удаляет запись об этом заказе,
    иначе False. Каждое сообщение подписывается секретом,
    который знает каждая сторона.
'''

path.append("..")
from configloader import config

SERVER_URL = config["Config"]["server_url"]
SECRET = config["Credit Card"]["yandex_money_secret"]

def remove(server_url, amount, label, path="/remove_payment/"):
    server_url = server_url if server_url else SERVER_URL
    signed_message = sign_message(label=label, amount=amount,
            only_label_amount = True)

    resp = requests.post(server_url + path, data = signed_message).text
    return resp

if __name__ == "__main__":
        print(remove(input("server url (may skeep) > ").strip(),
                            input("amount > ").strip(),
                            input("lable > ").strip()))
