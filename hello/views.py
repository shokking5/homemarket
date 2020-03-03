from binascii import hexlify
from hashlib import sha1
from urllib.parse import unquote

from django.http import HttpResponse
from django.http import HttpResponseNotAllowed, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from sentry_sdk import init
from math import ceil
import re

init("https://89ff6b28bd584a0fb6dff53fe0e40a4a@sentry.io/2895800")
notification_secret = "d1kWLWFFycukgu3mkduX1L0P"
sha1_secret: bytes = hexlify(sha1(notification_secret.encode()).digest())
database = "waiting_list"
backup="backup"

class Order:
    def __init__(self, label, amount):
        self.label = label
        self.amount = amount

    def __eq__(self, other):
        return f"{self.label}:{self.amount}" == f"{other.label}:{other.amount}"

    def __str__(self):
        return f"{self.label}:{self.amount}"


def _backup_request(data):
    with open(backup, "a") as file:
        file.write(data)


def _add_to_waitlist(order: Order):
    if order:
        with open(database, "a") as file:
            file.write(str(order) + "\n")



def _remove_from_waitlist(order: Order):
    if order:
        data = ""
        with open(database, "r") as file:
            data = file.read()
        match = re.search(str(order) + "\n", data)
        if match:
            data = data.replace(match.group(0), "", 1)
            with open(database, "w") as file:
                file.write(data)
                return True
    return False



def verify(body: bytes, get_order=False):
    try:
        body = unquote(body.decode())
        data = [dict({key: value}) for key, value
                in [x.split("=") for x in body.split("&")]]
        vals = dict()
        [vals.update(x) for x in data]

        if get_order:
            amount = vals["amount"]
            label = vals["label"]
            sha1_hash = vals["sha1_hash"]
            message = f"{amount}&{label}&{notification_secret}".encode()

        else:
            notification_type = vals["notification_type"]
            operation_id = vals["operation_id"]
            amount = vals["amount"]
            currency = vals["currency"]
            datetime = vals["datetime"]
            sender = vals["sender"]
            codepro = vals["codepro"]
            label = vals["label"]
            sha1_hash = vals["sha1_hash"]

            message = f"{notification_type}&{operation_id}&{amount}&{currency}&{datetime}&{sender}&{codepro}&{notification_secret}&{label}".encode()

        sign = hexlify(sha1(message).digest()).decode()
        return sign == sha1_hash, label, ceil(float(amount))

    except Exception:
        return None, None, None


@csrf_exempt
def set_payment(request):
    _backup_request(f"{datetime.now().ctime()} {request.body.decode()}\n/set_payment\n\n")

    if request.method == "POST":
        is_verified, label, amount = verify(request.body)
        if is_verified:
            _add_to_waitlist(Order(label, amount))
            return HttpResponse(f"order {label} {amount} added")
        else:
            HttpResponseForbidden()
    return HttpResponseNotAllowed("POST")


@csrf_exempt
def remove_payment(request):
    _backup_request(f"{datetime.now().ctime()} {request.body.decode()}\n/remove_payment\n\n")

    if request.method == "POST":
        is_verified, label, amount = verify(request.body, True)
        if is_verified:
            if _remove_from_waitlist(Order(label, amount)):
                return HttpResponse("True")
    return HttpResponseForbidden()


@csrf_exempt
def get_backup(request):
    _backup_request(f"{datetime.now().ctime()} {request.body.decode()}\n/get_backup\n\n")

    if request.method == "POST":
        if request.body == sha1_secret:
            with open(backup, "r") as file:
                return HttpResponse(file.read())
    return HttpResponseForbidden()


@csrf_exempt
def get_orders(request):
    _backup_request(f"{datetime.now().ctime()} {request.body.decode()}\n/get_orders\n\n")

    if request.method == "POST":
        if request.body == sha1_secret:
            with open(database, "r") as file:
                return HttpResponse(file.read())
    return HttpResponseForbidden()

