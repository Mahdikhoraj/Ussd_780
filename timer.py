from datetime import datetime, timedelta
import random


def service() -> dict[str, str]:
    print("Tickets")
    user = {"1": "Train", "2": "Bus", "3": "Airplane"}
    return user


def show_ticket_date() -> dict:
    tickets = {}
    today = datetime.today()
    index = 1

    for day in range(6):
        date = today + timedelta(days=day)

        print(date.strftime("%A - %Y-%m-%d"))

        for _ in range(3):
            hour = random.randint(0, 23)
            minute = random.randint(0, 59)
            price = random.randint(1_000_000, 10_000_000)

            tickets[str(index)] = (
                date.strftime("%Y-%m-%d"),
                f"{hour:02}:{minute:02}",
                price,
            )

            print(f"{index}: {hour:02}:{minute:02} - {price}")

            index += 1

    return tickets
