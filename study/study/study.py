"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from rxconfig import config

import reflex as rx

docs_url = "https://reflex.dev/docs/getting-started/introduction/"
filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""
    pass

def contained_card(input_heading: str, input_text: str) -> rx.container:
    """Makes a card and places it within a container, returns this 
    container with a card in it"""
    created_card = card(input_heading, input_text)

    return container(created_card)


def container(card: rx.card) -> rx.container:
    """Creates a container to hold a card"""
    return rx.container(
        # card function... 
        card
    ),
    size="3",


def card(input_heading: str, input_text: str) -> rx.card:
    """Creates a card that contains the information for a week
    of a study plan"""
    return rx.card(
        rx.flex(
            rx.box(
                rx.heading(input_heading),
                rx.text(
                    input_text,
                    width="100%"
                ),
            ),
            spacing="1",
        ),
        as_child=True,
        
    )
    
def index() -> rx.Component:
    # we're gonna test smth a little crazy...
    return rx.center(
        rx.theme_panel(),
        rx.vstack(
            # we want a vertical stack of all the containers that will
            # be created by parsing the text
            rx.box(
                rx.heading("Study Plan changed", size="8", padding='2'),
                # contained_card('test1', 'apple'),
                # contained_card('test2', 'no way....'),
                # card('test1', 'apple'),
                # card('test2', 'no way....'),
               
                # rx.text("Get started by editing ", rx.code(filename)),
            ),
            spacing='2',
        ),
        height="50vh",
    )


app = rx.App()
app.add_page(index)
