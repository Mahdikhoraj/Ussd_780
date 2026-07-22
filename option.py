from vallidation import *
from get_value import *
from Internets import *
from show import *
import random
import time
from files import *


def all_option(
    internet_package,
    show_func,
    random,
    choice,
    rand_pass,
):
    internet = internet_package
    show_func(internet)
    choice = get_choice(is_valid_choice, internet)
    phone = get_phone(is_valid_phone)
    card = get_card(is_valid_card)
    with open("password.txt", mode="rt", encoding="UTF-8") as file:
        file_password = file.read().strip()
    password = get_password(is_valldi_pass, file_password)
    (f"{rand_pass}")
    if password is not None:
        random(internet, choice)
        print("Successfully purchased")
        current_time = time.strftime("%Y-%m-%d %H:%M:%S")
        add_choice_user(f"{choice} - {internet[choice]}- {current_time}")
        show_in_file()
    time.sleep(5)


def random_charge_internet(
    menu: dict,
    choice: str,
) -> callable:
    balance = random.randint(50000, 10000000)
    print(f"your balance {balance}")
    value, price = menu[choice]
    if balance >= price:
        balance -= price
        print(f"pacage price: {price}")
        print(f"current balance : {balance}")
        time.sleep(5)


def show_balance():
    number = get_phone(is_valid_phone)
    balance = random.randint(50000, 10000000)
    print(f"your balance {balance}")
    time.sleep(5)


def random_tic(menu: dict, choice):
    balance = random.randint(50000, 10000000)
    choice = str(choice)

    date, hour, price = menu[choice]

    print(f"Your balance: {balance}")

    if balance >= price:
        balance -= price
        print(f"Ticket date: {date}")
        print(f"Ticket time: {hour}")
        print(f"Ticket price: {price}")
        print(f"Current balance: {balance}")
        time.sleep(5)


def ticket_option(internet_package, random, choice, rand_pass):
    card = get_card(is_valid_card)
    with open("password.txt", mode="rt", encoding="UTF-8") as file:
        file_password = file.read().strip()
        password = get_password(is_valldi_pass, file_password)
    (f"{rand_pass}")
    if password is not None:
        random(internet_package, choice)
        print("Successfully purchased")
        current_time = time.strftime("%Y-%m-%d %H:%M:%S")
        add_choice_user(f"{choice} - {internet_package[str(choice)]} - {current_time}")
        show_in_file()
        time.sleep(5)
