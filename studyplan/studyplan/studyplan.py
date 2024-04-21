from rxconfig import config

import reflex as rx

docs_url = "https://reflex.dev/docs/getting-started/introduction/"
filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""
    # include the given text
    ai_plan: str = 'ai_input ai_input ai_input \n\nai_input ai_input ai_input ai_input \n\nai_input ai_input \n\nai_input ai_input ai_input ai_input ai_input ai_input ai_input ai_input ai_input'.replace('*', '').replace('\n', '\n\n')


def index() -> rx.Component:
    # we're gonna test smth a little crazy...
    return rx.center(
        rx.vstack(
            rx.box(
                rx.container(
                    rx.heading("Study Plan for ", rx.text.em("placeholder"), size="8", padding='25px 25px', align='center'),
                    rx.container(
                        rx.markdown(State.ai_plan),
                        padding='25px 25px'
                    ),
                    size="4",
                ),
            ),
            spacing='2',
        ),
        height="50vh",
    )


app = rx.App()
app.add_page(index)