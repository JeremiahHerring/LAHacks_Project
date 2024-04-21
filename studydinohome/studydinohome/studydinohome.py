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

def navigation():
    return rx.box(
        rx.hstack(
            rx.link(
                rx.hstack(
                    rx.image(src="/dino_trans.png", width="50px"),
                    rx.heading("studydino | merging AI and mental health", size = "5",
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
            padding="1.5em",
            bg="rgba(255, 255, 255, 0.97)",
        ),
        position="fixed",
        width="100%",
        top="0px",
        z_index="500",
        height="50px",
    )

class FormState(rx.State):
    form_data: dict = {}

    def new_submission(self, form_data: dict):
        print(form_data)
        self.form_data = form_data
        time_str = ""
        mental_health = []

        for entry, value in form_data.items():
            if entry == "days":
                time_str += form_data["days"] + " days "
            if entry == "weeks":
                time_str += form_data["days"] + " weeks "
            if entry == "months":
                time_str += form_data["months"] + " months "
            if value == "on":
                mental_health.append(entry)
        selected_options_string = ', '.join(mental_health)

        print(selected_options_string)
        print(time_str)

def make_plan():
    return rx.dialog.root(
        rx.dialog.trigger(rx.button("Make my custom study plan", size="4", radius="full")),
        rx.dialog.content(
            rx.dialog.title("Your custom study plan", style=header1_style),
            rx.dialog.description(
                "Select all that you want in your plan",
                size="2",
                mb="0",
                paddying_bottom="7em"
            ),
            rx.form(
                rx.flex(
                    rx.text(
                        "Name",
                        as_='div',
                        size="2",
                        mb="1",
                        weight="bold",
                        style=header1_style,
                    ),
                    rx.input(placeholder="Ex. Cat Rogers", name="name"),
                    rx.text(
                        "Email",
                        as_='div',
                        size="2",
                        mb="1",
                        weight="bold",
                        style=header1_style,
                    ),
                    rx.input(placeholder="Ex. abc@gmail.com", name="email"),
                    rx.text(
                        "How long do you have to study?",
                        as_='div',
                        size="2",
                        mb="1",
                        weight="bold",
                        style=header1_style,
                    ),
                    rx.hstack(
                        rx.input(
                            name = "days",
                            default_value="0",
                            placeholder="0-31",
                            type="number",
                            min="0",
                            max="31",
                            required=False,
                        ),
                        rx.text(
                        "days",
                        as_='div',
                        size="2",
                        mb="1",
                        weight="bold",
                        style=header1_style,
                        ),
                        rx.input(
                            name = "weeks",
                            default_value="0",
                            placeholder="0-4",
                            type="number",
                            min="0",
                            max="4",
                            required=False,
                        ),
                        rx.text(
                        "weeks",
                        as_='div',
                        size="2",
                        mb="1",
                        weight="bold",
                        style=header1_style,
                        ),
                        rx.input(
                            name = "months",
                            default_value="0",
                            placeholder="0-12",
                            type="number",
                            min="0",
                            max="12",
                            required=False,
                        ),
                        rx.text(
                        "months",
                        as_='div',
                        size="2",
                        mb="1",
                        weight="bold",
                        style=header1_style,
                        ),
                        align="center",
                        spacing="4"
                    ),
                    rx.divider(),
                    rx.text(
                        "What should we customize your plan for?",
                        as_='div',
                        size="2",
                        mb="1",
                        weight="bold",
                        style=header1_style,
                    ),
                    rx.hstack(
                        rx.vstack(
                            rx.text("Stress"),
                            rx.text("Anxiety"),
                            rx.text("Procrastination"),
                            rx.text("Depression"),
                            rx.text("Motivation"),
                            rx.text("Time Management"),
                        ),
                        rx.vstack(
                            rx.switch(name="stress1", default_checked=False),
                            rx.switch(name="anxiety2", default_checked=False),
                            rx.switch(name="procrastination3", default_checked=False),
                            rx.switch(name="depression4", default_checked=False),
                            rx.switch(name="motivation5", default_checked=False),
                            rx.switch(name="timemanagement6", default_checked=False),
                            spacing="3",
                        ),
                        rx.vstack(
                            rx.text("Exam Stress"),
                            rx.text("Financial Difficulties"),
                            rx.text("Burnout"),
                            rx.text("Discrimination"),
                            rx.text("Physical Health"),
                            rx.text("Family Issues"),
                        ),
                        rx.vstack(
                            rx.switch(name="examstress7", default_checked=False),
                            rx.switch(name="finance8", default_checked=False),
                            rx.switch(name="burnout9", default_checked=False),
                            rx.switch(name="discrimination10", default_checked=False),
                            rx.switch(name="physical11", default_checked=False),
                            rx.switch(name="family12", default_checked=False),
                            spacing="3",
                        ),
                        spacing="8",
                        align="center",
                        justify="between",
                    ),
                    rx.flex(
                        rx.dialog.close(
                            rx.button("cancel", background_color="rgba(255, 227, 237, 0.8)"),
                        ),
                        rx.button("start a plan", type="submit"),
                        padding_top="1em",
                        spacing="3",
                        mt="4",
                        justify="end",
                    ), 
                    direction="column",
                    spacing="3",
                ),
                on_submit=FormState.new_submission,
                reset_on_submit=True,
            ),
            style={"max_width": 700},
            box_shadow="lg",
            padding="3em",
            border_radius="25px",
            font_family="Arial",
            size="4",
        ),
    )

def index() -> rx.Component:
    return rx.center(
        navigation(),
        rx.vstack(
            rx.vstack(
                rx.heading("Welcome to ", rx.text.em("studydino"), size="9", style=header1_style),
                rx.text("where academics meet AI and mental health",
                    size="6",
                    font_family="Arial Rounded MT Bold",
                ),
                align="center",
                spacing="2",
            ),
            make_plan(),
            align="center",
            spacing="9",
            font_size="2em",
            height="70vh",
        ),
        padding="1em",
        height=pg_size + "vh",
        background="radial-gradient(circle at 22% 11%,rgba(229, 255, 231,0.8),hsla(0,0%,100%,0) 30%),radial-gradient(circle at 82% 40%,rgba(253, 251, 230,0.8),hsla(0,0%,100%,0) 45%),radial-gradient(circle at 15% 85%,rgba(255, 227, 237, 0.8),hsla(0,0%,100%,0) 40%)",
    )

app = rx.App(style=style1,
             theme=rx.theme(
                appearance="light", has_background=True, radius="full"
            )
            )
app.add_page(index, title="studydino | home")
