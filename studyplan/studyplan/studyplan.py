from rxconfig import config

import reflex as rx

docs_url = "https://reflex.dev/docs/getting-started/introduction/"
filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""
    # include the given text
    ai_plan: str = '**Study Plan:**\n\n**Week 1:**\n\n* **Focus:** Introduction to Syntax Analysis, Grammar, and Chomsky Hierarchy. \n\n* **Activities:**\n\n* Read sections 3.1-3.3 of the textbook.\n\n* Create flashcards for key terms and concepts.\n\n* Practice writing simple grammars in BNF notation.\
        \n\n* **Mindfulness:** Start each study session with a 5-minute breathing exercise.\n\n**Week 2:**\n\n* **Focus:** Left Recursion, Backtracking, and Top-Down Parsing (RDP).\n\n* **Activities:**\n\n* Read sections 3.4-3.5a of the textbook.'.replace('*', '')

def index() -> rx.Component:
    # we're gonna test smth a little crazy...
    return rx.center(
        rx.vstack(
            rx.box(
                rx.container(
                    rx.heading("Study Plan for [we'll figure it out]", size="8", padding='70px 25px', align="center"),
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