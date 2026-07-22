from typing import Callable
import csv
import os
from show_secend_pass import *


def create_file(file: callable):
    try:
        file = open("users.txt", mode="rt", encoding="UTF-8")
    except:
        file = open("users.txt", mode="a", encoding="UTF-8")


def password_file(file: callable):
    try:
        file = open("password.txt", mode="rt", encoding="UTF-8")
    except:
        file = open("password.txt", mode="a", encoding="UTF-8")


def show_pass(secend_pass: str):
    with open("password.txt", mode="w", encoding="UTF-8") as file:
        file.write(f"{secend_pass()}")


def add_choice_user(choice: dict[str]) -> None:
    with open("users.txt", mode="a", encoding="UTF-8") as file:
        file.write(f"Your choice:{choice}")


def show_in_file():
    with open("users.txt", mode="a", encoding="UTF-8") as file:
        file.write("\n")
        file.write("This package Successfully purchased\n")
        file.write("\n")


def seperator():
    with open("users.txt", mode="a", encoding="UTF-8") as file:
        seperator = f"{"-" * 100}\n"
        file.write(seperator)
