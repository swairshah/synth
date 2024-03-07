from textual.app import App, ComposeResult
from textual.events import Key
from textual.widgets import Button, Header, Label, Select


class MyApp(App[str]):
    CSS_PATH="dialog.tcss"
    TITLE = "Evaluate"
    SUB_TITLE = "is the selected answer correct?"

    def __init__(self, text: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.text = text
 
    def compose(self) -> ComposeResult:
        yield Header()
        yield Label(self.text, id="question")
        yield Button("Yes", id=True, variant="default")
        yield Button("No", id=False, variant="default")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.exit(event.button.id)

    #def on_key(self, event: Key):
    #    self.title = event.key
    #    #self.sub_title = f"You just pressed {event.key}!"

def ask_question(text):
    app = MyApp(text)
    reply = app.run()
    return reply


if __name__ == "__main__":
    ret = ask_question("Test Question\nTest Answer")
