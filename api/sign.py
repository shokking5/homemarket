from binascii import hexlify
from hashlib import sha1
from datetime import datetime
from sys import path

path.append("..")
from configloader import config

SECRET = config["Credit Card"]["yandex_money_secret"]

def hash_secret(secret=SECRET) -> str:
    if type(secret) == str:
        secret = secret.encode("utf-8")
    return hexlify(sha1(secret).digest()).decode()


def sign_message(label: str,
                amount: str,
                notification_secret: str = SECRET,
                date: str = datetime.now().ctime(),
                notification_type: str = "type",
                codepro: str = "None",
                operation_id: str = "None",
                currency: str = "None",
                sender: str = "None",
                only_label_amount = False) -> str:

    if only_label_amount:
        message = f"{amount}&{label}&{notification_secret}".encode()

    else:
        message = f"{notification_type}&{operation_id}&" \
                  f"{amount}&{currency}&{date}&{sender}&" \
                  f"{codepro}&{notification_secret}&{label}".encode()


    sha1_hash = hexlify(sha1(message).digest()).decode()
    signed_message = f"notification_type={notification_type}&" \
               f"operation_id={operation_id}&" \
               f"amount={amount}&" \
               f"currency={currency}&" \
               f"datetime={date}&" \
               f"sender={sender}&" \
               f"codepro={codepro}&" \
               f"sha1_hash={sha1_hash}&" \
               f"label={label}"

    return signed_message

