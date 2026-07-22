def show_main_menu(menu: dict[str]):
    for key, value in menu.items():
        print(f"{key} : {value}")


def show_menus(menu: dict[str]):
    for key, (value, price) in menu.items():
        print(f"{key} : {value} : {price}")