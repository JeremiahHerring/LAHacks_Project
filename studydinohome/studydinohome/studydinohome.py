from rxconfig import config

import reflex as rx

docs_url = "https://reflex.dev/docs/getting-started/introduction/"
filename = f"{config.app_name}/{config.app_name}.py"
pg_size = "150"

class State(rx.State):
    """The app state."""

header1_style = { #sets font for header
    "font_family": "Arial Rounded MT Bold",
}
def navigation():
    return rx.box(
        rx.hstack(
            rx.link(
                rx.hstack(
                    rx.heading("studydino | merging AI and mental health", size = "6",
                               style=header1_style),
                    align="center",
                ),
                href="/",
            ),
            rx.spacer(width="100%"),
            #menu here
            align="center",
            justify="center",
            border_bottom="0.2em solid #F0F0F0",
            padding_x="10em",
            padding="2em",
            bg="rgba(255, 255, 255, 0.97)",
        ),
        position="fixed",
        width="100%",
        topy="0px",
        z_index="500",
        height=pg_size + "%",
    )


def index() -> rx.Component:
    return rx.center(
        navigation(),
        rx.vstack(
            rx.vstack(
                rx.heading("Welcome to studydino", size="9", style=header1_style),
                rx.text("where academics meet AI and mental health",
                    size="6",
                    font_family="Arial Rounded MT Bold",
                ),
                align="center",
                spacing="2",
            ),
            rx.button(
                "Form my custom study plan",
                on_click=lambda: rx.redirect(docs_url),
                size="4",
            ),
            align="center",
            spacing="9",
            font_size="2em",
            height="70vh",
        ),
        padding="1em",
        height=pg_size + "vh",
        background="radial-gradient(circle at 22% 11%,rgba(229, 255, 231,0.8),hsla(0,0%,100%,0) 30%),radial-gradient(circle at 82% 40%,rgba(253, 251, 230,0.8),hsla(0,0%,100%,0) 45%),radial-gradient(circle at 15% 85%,rgba(255, 227, 237, 0.8),hsla(0,0%,100%,0) 40%)",
    )

style1 = {
    "font_family": "Arial",
    rx.heading: {
        "color": "black",
    },
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
