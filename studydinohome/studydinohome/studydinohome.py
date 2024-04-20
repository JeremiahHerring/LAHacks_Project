from rxconfig import config

import reflex as rx

docs_url = "https://reflex.dev/docs/getting-started/introduction/"
filename = f"{config.app_name}/{config.app_name}.py"

class State(rx.State):
    """The app state."""

def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("Welcome to studydino", size="9"),
            rx.text("where academics meet AI and mental health"),
            rx.button(
                "Form my custom study plan",
		color_scheme="grass",
                on_click=lambda: rx.redirect(docs_url),
                size="4",
            ),
            align="center",
            spacing="7",
            font_size="2em",
        ),
        height="50vh",
    )


app = rx.App()
app.add_page(index)
