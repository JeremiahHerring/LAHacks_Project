from rxconfig import config

import reflex as rx

docs_url = "https://reflex.dev/docs/getting-started/introduction/"
filename = f"{config.app_name}/{config.app_name}.py"

pg_size = "300"
black = "rgba(0, 0, 0, 0.97)"
white = "rgba(255, 255, 255, 0.97)"

header1_style = { #sets font for header
    "font_family": "Arial Rounded MT Bold",
}

style1 = {
    "font_family": "Arial",
    rx.button: {
        "background_color": "#C3E3C3", #default CSS color: DarkSeaGreen
        "color": "black",
    },
}

# the removed astrick version should be passed through here 
def format_input(s: str) -> str:
    """Formats the given string to be formatted properly
    when displayed"""
    s = s.replace('*', '')
    each_line = s.split('\n')
    dupe_each_line = each_line.copy()
    
    # check for week # (if it's not week 1, then add '\n\n' to the start)
    for line in range(len(each_line)):
        curr_line = each_line[line]

        if len(curr_line.strip()) >= 4 and curr_line.strip()[0:4] == 'Week':
            week_num = curr_line.strip()[4:-1]
            if week_num != '' and int(week_num) != 1:
                dupe_each_line.insert(line, '\n\n')

    s = '\n'.join(dupe_each_line)

    return s


# list.insert(element, index) -- only updates curr list 
# ' '.join(list) -- convert a list into a string again

class State(rx.State):
    """The app state."""
    # include the given text
    test_str = 'Week 1:\nFocus: Introduction to Syntax Analysis, Grammar, and Chomsky Hierarchy\nWeek 2:\nai_input ai_input ai_input ai_input ai_input ai_input ai_input ai_input ai_inpuuiefeufwuiefuishdfusehf\nWeek 3:\nai_input ai_input ai_input ai_input ai_input ai_input ai_input ai_input ai_input\n\nWeek 2:\nai_input ai_input ai_input ai_input ai_input ai_input ai_input ai_input ai_inpuuiefeufwuiefuishdfusehf\nWeek 3:\nai_input ai_input ai_input ai_input ai_input ai_input ai_input ai_input ai_input\nWeek 2:\nai_input ai_input ai_input ai_input ai_input ai_input ai_input ai_input ai_inpuuiefeufwuiefuishdfusehf\nWeek 3:\nai_input ai_input ai_input ai_input ai_input ai_input ai_input ai_input ai_input\nWeek 2:\nai_input ai_input ai_input ai_input ai_input ai_input ai_input ai_input ai_inpuuiefeufwuiefuishdfusehf\nWeek 3:\nai_input ai_input ai_input ai_input ai_input ai_input ai_input ai_input ai_input\n'
    ai_plan: str = format_input(test_str).replace('\n', '\n\n')

def navigation():
    return rx.box(
        rx.hstack(
            rx.link(
                rx.hstack(
                    rx.image(src="/dino_trans.png", width="50px"),
                    rx.heading(rx.text.em("studydino"), " | merging AI and mental health", size = "5",
                               style=header1_style, color=rx.color_mode_cond(black, white)
                    ),
                    align="center",
                ),
                href="/",
            ),
            rx.spacer(width="100%"),
            #menu here
            rx.color_mode.button(rx.color_mode.icon(), size="3", float="right", color=rx.color_mode_cond(black, white), background_color=rx.color_mode_cond("#C3E3C3", "#568356")),
            bg=rx.color_mode_cond(white, black),
            align="center",
            justify="center",
            border_bottom="0.2em solid #F0F0F0",
            padding_x="10em",
            padding="1.5em",
        ),
        position="fixed",
        width="100%",
        top="0px",
        z_index="500",
        height="50px",
    )

def index() -> rx.Component:
    return rx.center(
        navigation(),
        rx.vstack(
            rx.heading("Your custom ", rx.text.em("studydino"), " study plan", size="8", style=header1_style),
            rx.box(
                rx.container(
                    rx.markdown(State.ai_plan, padding='50px 25px', align='center', position="center"),
                ),
                size="4",
                border=f"1px dotted {rx.color_mode_cond(black, white)}",
                border_radius="25px",
                background_color=rx.color_mode_cond(white, black),
                padding="5em",
                align="center",
                width="85%",    
            ),   
            align="center",
            spacing="5",
            font_size="1.5em",
            height="260vh",
        ),
        padding="1em",
        height=pg_size + "vh",
        background=rx.color_mode_cond(
            "radial-gradient(circle at 22% 11%,rgba(229, 255, 231,0.8),hsla(0,0%,100%,0) 30%),radial-gradient(circle at 82% 40%,rgba(253, 251, 230,0.8),hsla(0,0%,100%,0) 45%),radial-gradient(circle at 15% 85%,rgba(255, 227, 237, 0.8),hsla(0,0%,100%,0) 40%)",
            "radial-gradient(circle at 22% 11%,rgba(124, 147, 124,0.8),hsla(0,0%,100%,0) 30%),radial-gradient(circle at 82% 40%,rgba(187, 184, 159,0.8),hsla(0,0%,100%,0) 45%),radial-gradient(circle at 15% 85%,rgba(221, 203, 209, 0.8),hsla(0,0%,100%,0) 40%)"
        ), 
    )


app = rx.App()
app.add_page(index)