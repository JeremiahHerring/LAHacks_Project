from rxconfig import config

import reflex as rx

docs_url = "https://reflex.dev/docs/getting-started/introduction/"
filename = f"{config.app_name}/{config.app_name}.py"

class State(rx.State):
    """The app state."""

header1_style = {
    "font_family": "Arial Rounded MT Bold",
}

def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("Welcome to studydino", size="9", style=header1_style),
            rx.text("where academics meet AI and mental health",
                size="7",
                font_family="Arial Rounded MT Bold",
            ),
            rx.button(
                "Form my custom study plan",
                on_click=lambda: rx.redirect(docs_url),
                size="4",
            ),
            align="center",
            spacing="7",
            font_size="2em",
        ),
        height="100vh",
        background="radial-gradient(circle at 22% 11%,rgba(229, 255, 231,0.8),hsla(0,0%,100%,0) 30%),radial-gradient(circle at 82% 40%,rgba(253, 251, 230,0.8),hsla(0,0%,100%,0) 45%),radial-gradient(circle at 25% 85%,rgba(255, 234, 242, 0.8),hsla(0,0%,100%,0) 40%)",
    )

style1 = {
    "font_family": "Arial",
    rx.button: {
        "background_color": "#C3E3C3", #default CSS color: DarkSeaGreen
        "color": "black",
    },
}

app = rx.App(style=style1,
             theme=rx.theme(
                appearance="light", has_background=True, radius="full"
            )
            )
app.add_page(index, title="studydino | home")
