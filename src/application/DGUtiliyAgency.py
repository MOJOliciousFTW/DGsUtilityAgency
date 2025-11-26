from textual.app import App
from textual.binding import Binding

from ..forms.welcome import WelcomeScreen


class DGUtilityAgency(App):
    CSS_PATH = "dgutility.css"
    purchase_data = {}

    BINDINGS = [
        Binding("q", "quit", "Quit", priority=True),  # Press 'q' to quit
        Binding("ctrl+c", "quit", "Quit", priority=True),  # Ctrl+C also quits
    ]

    def on_mount(self) -> None:
        self.push_screen(WelcomeScreen())


def main():
    app = DGUtilityAgency()
    app.run()


if __name__ == "__main__":
    main()
