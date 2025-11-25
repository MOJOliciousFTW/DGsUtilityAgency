from textual.containers import Container, Horizontal, Vertical
from textual.screen import Screen
from textual.widgets import (
    Button,
    Checkbox,
    Footer,
    Header,
    RadioButton,
    RadioSet,
    Static,
)

from src.forms.time_and_category import TimeAndCategoryScreen


class LifeAreasScreen(Screen):

    def compose(self):
        yield Header()

        with Vertical(id="content"):
            with Container(classes="panel"):
                yield Static(
                    "[bold cyan]╔═══════════════════════════════════════════════════╗[/bold cyan]\n"
                    "[bold cyan]║[/bold cyan]  Step 2: Life Areas & Necessity                  [bold cyan]║[/bold cyan]\n"
                    "[bold cyan]╚═══════════════════════════════════════════════════╝[/bold cyan]",
                    classes="panel-title",
                )

                yield Static(
                    "Tell us more about this purchase and its impact.",
                    classes="hint",
                )

                with Vertical(classes="section"):
                    yield Static("[bold]Life Areas[/bold]", classes="section-header")
                    yield Static(
                        "What areas of life does this affect? (Select all that apply)",
                        classes="hint",
                    )

                    with Vertical(id="life-areas-checkboxes"):
                        yield Checkbox("Career & Professional", id="career")
                        yield Checkbox("Personal & Social", id="personal")
                        yield Checkbox("Health & Wellness", id="health")

                with Vertical(classes="section"):
                    yield Static("[bold]Necessity Level[/bold]", classes="section-header")
                    yield Static("How necessary is this item?", classes="hint")

                    with RadioSet(id="necessity"):
                        yield RadioButton("Essential - Must have", id="essential", value=True)
                        yield RadioButton(
                            "Nice to have - Want but not critical", id="nice_to_have"
                        )

                with Horizontal(id="button-group"):
                    yield Button("← Back", variant="default", id="back")
                    yield Button("Continue →", variant="primary", id="continue")

        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "continue":

            life_areas = []
            career_checkbox = self.query_one("#career", Checkbox)
            personal_checkbox = self.query_one("#personal", Checkbox)
            health_checkbox = self.query_one("#health", Checkbox)

            if career_checkbox.value:
                life_areas.append("career")
            if personal_checkbox.value:
                life_areas.append("personal")
            if health_checkbox.value:
                life_areas.append("health")

            necessity_radio = self.query_one("#necessity", RadioSet)
            necessity = necessity_radio.pressed_button.id

            self.app.purchase_data["life_areas"] = life_areas
            self.app.purchase_data["necessity"] = necessity

            self.app.push_screen(TimeAndCategoryScreen())

        elif event.button.id == "back":
            self.app.pop_screen()
