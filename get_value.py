from inputimeout import inputimeout, TimeoutOccurred
from timer import *
import sys


def get_choice(is_valid: callable, menu, prompt: str = "Enter your choice:") -> str:
    try:
        choice = input(prompt)
        while not is_valid(menu, choice):
            print("Its not correct, please try again..")
            choice = input(prompt)
        return choice
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt:Error, please start again")
        sys.exit(0)


def get_phone(
    is_valid_ph: callable[int], prompt: str = "Enter your phone number:"
) -> str:
    try:
        phone = input(prompt)
        while not is_valid_ph(phone):
            print("Its not correct, please try again!")
            phone = input(prompt)
        return phone
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt:Error, please start again")
        sys.exit(0)


def get_password(
    is_valid_pass: callable,
    files,
    prompt: str = "Enter the secend_pass in file:",
    delay=120,
) -> str:
    try:
        password = inputimeout(prompt, timeout=delay)
        while not is_valid_pass(password, files):
            print("Its not correct, please try again!")
            password = inputimeout(prompt, timeout=delay)
        return password
    except TimeoutOccurred:
        print("Time is over")
        return None
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt:Error, please start again")
        sys.exit(0)


def get_card(
    is_valid_card_id: callable, prompt: str = "Enter your card number:"
) -> str:
    try:
        card = inputimeout(prompt)
        while not is_valid_card_id(card):
            print("Its not correct, please try again!")
            card = inputimeout(prompt)
        return card
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt:Error, please start again")
        sys.exit(0)


def get_calender(prompt: str = "select your date:"):
    try:
        while True:
            choice = input(prompt)
            choice = int(choice)
            if not choice in range(1, 19):
                print("Its not correct, please try again!")
                choice = input(prompt)
            return choice
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt:Error, please start again")
        sys.exit(0)
