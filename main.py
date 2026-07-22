from Internets import *
from welcome import *
from show import *
from vallidation import *
from get_value import *
from option import *
from files import *
import time
from charges import *
from show_secend_pass import *
from timer import *


def main() -> None:
    while True:
        create_file("users.txt")
        password_file("password.txt")
        welcome()
        choice = "*780#"
        while True:
            app_keyboard = DialerApp().run()
            if is_valid_app_choice(choice, app_keyboard):
                break
            time.sleep(1)

        show_main_menu(main_choice())

        user_choice = get_choice(is_valid_choice, main_choice())

        match user_choice:
            case "1":
                internet_menu = internet()
                show_main_menu(internet())
                current_time = time.strftime("%Y-%m-%d %H:%M:%S")
                internet_choice = get_choice(is_valid_choice, internet())
                add_choice_user(
                    f"{choice} - {internet_menu[internet_choice]}- {current_time}\n"
                )
                if internet_choice == "1":
                    all_option(
                        internet_daily(),
                        show_menus,
                        random_charge_internet,
                        internet_choice,
                        show_pass(secend_pass),
                        
                    )

                elif internet_choice == "2":
                    all_option(
                        internet_weekly(),
                        show_menus,
                        random_charge_internet,
                        internet_choice,
                        show_pass(secend_pass),
                    )

                elif internet_choice == "3":
                    all_option(
                        internet_monthly(),
                        show_menus,
                        random_charge_internet,
                        internet_choice,
                        show_pass(secend_pass),
                        
                    )

                elif internet_choice == "4":
                    all_option(
                        internet_yearly(),
                        show_menus,
                        random_charge_internet,
                        internet_choice,
                        show_pass(secend_pass),
                    )
                
                seperator()
            case "2":
                charge_menu = charge()
                show_main_menu(charge())
                current_time = time.strftime("%Y-%m-%d %H:%M:%S")
                charge_choice = get_choice(is_valid_choice, charge())
                add_choice_user(
                    f"{choice} - {charge_menu[charge_choice]}- {current_time}\n"
                )

                if charge_choice == "1":
                    all_option(
                        charge_hourly(),
                        show_menus,
                        random_charge_internet,
                        charge_choice,
                        show_pass(secend_pass),
                    )

                elif charge_choice == "2":
                    all_option(
                        charge_daily(),
                        show_menus,
                        random_charge_internet,
                        charge_choice,
                        show_pass(secend_pass),
                    )

                elif charge_choice == "3":
                    all_option(
                        charge_monthly(),
                        show_menus,
                        random_charge_internet,
                        charge_choice,
                        show_pass(secend_pass),
                    )

                seperator()
            case "3" :
                show_balance()
                
            case "4":
                service_t = service()
                show_main_menu(service())
                current_time = time.strftime("%Y-%m-%d %H:%M:%S")
                t_date = get_choice(is_valid_choice, service())
                add_choice_user(
                    f"{choice} - {service_t[t_date]}- {current_time}\n"
                )
                ticket = show_ticket_date()
                choice_calender = get_calender()
                ticket_option(
                    ticket,
                    random_tic,
                    t_date,
                    show_pass(secend_pass),
                )
                seperator()
                
            case "5" :
                with open("users.txt" , mode="rt"  , encoding="UTF-8") as file:
                    user_show = file.read()
                    print(user_show)

            case "6" :
                print("Thanks for chossing 780")
                break

if __name__ == "__main__":
    main()
