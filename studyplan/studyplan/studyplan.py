from rxconfig import config

import reflex as rx

docs_url = "https://reflex.dev/docs/getting-started/introduction/"
filename = f"{config.app_name}/{config.app_name}.py"

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
    test_str = 'Week 1:\nFocus: Introduction to Syntax Analysis, Grammar, and Chomsky Hierarchy\nWeek 2:\nai_input ai_input ai_input ai_input ai_input ai_input ai_input ai_input ai_inpuuiefeufwuiefuishdfusehf\nWeek 3:\nai_input ai_input ai_input ai_input ai_input ai_input ai_input ai_input ai_input\n'
    ai_plan: str = format_input(test_str).replace('\n', '\n\n')


def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.box(
                rx.container(
                    rx.heading("Study Plan for ", rx.text.em("placeholder"), size="8", padding='25px 25px', align='center'),
                    rx.container(
                        rx.markdown(State.ai_plan, align='center'),
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