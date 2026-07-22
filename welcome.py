import time
from textual.app import App, ComposeResult
from textual.containers import Vertical, Grid
from textual.widgets import Input, Button
from pathlib import Path



def welcome() -> None:
    print("welcome to the *780#")
    print("please select options")
    time.sleep(1)

class DialerApp(App):
    CSS_PATH = "style.tcss"
    # CSS_PATH = Path(__file__).resolve().parents[2] / "style" / "style.tcss"

    def compose(self) -> ComposeResult:
        with Vertical(id="phone"):
            yield Input(id="display", placeholder="*780#")

            with Grid(id="keypad"):
                for key in (
                    "1", "2", "3",
                    "4", "5", "6",
                    "7", "8", "9",
                    "*", "0", "#"
                ):
                    yield Button(key, classes="num")

            yield Button("📞 CALL", id="call")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        display = self.query_one("#display", Input)
        display.value = display.value or ""

        if event.button.id == "call":
            self.exit(display.value)
        else:
            display.value += str(event.button.label)


def main_choice() -> dict[str]:
    user = {
        "1": "Internet",
        "2": "Charge",
        "3": "Balance",
        "4": "Service",
        "5": "User choice",
        "6": "Exit",
    }
    return user
