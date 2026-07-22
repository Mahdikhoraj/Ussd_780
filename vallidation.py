import re


def is_valid_app_choice(choice, app_keyboard) -> bool:
    if choice == app_keyboard:
        return True

    print("Its not true")
    return False


def is_valid_choice(menu: dict[str], choice: str) -> bool:
    if choice in menu:
        return True
    return False


def is_valid_phone(phone: str) -> bool:
    pattern = r"^(?:09|\+989|989|00989)\d{9}$"
    if re.fullmatch(pattern, phone):
        return True
    return False


def is_valldi_pass(file_pass: str, password) -> bool:
    if password == file_pass:
        return True
    return False


def is_valid_card(card: str) ->bool:
    pattern = r"^\d{16}$"
    if re.fullmatch(pattern, card):
        return True
    return False


# def is_valid_marzie(choice: str) -> bool:
#     if choice in range(1,19):
#         return True
#     return False
