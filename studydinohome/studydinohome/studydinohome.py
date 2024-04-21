"""Welcome to Reflex! This file outlines the steps to create a basic app."""
import os
import sys
# Get the current directory of Script.py
current_dir = os.path.dirname(os.path.realpath(__file__))

# Move up two directories to reach the project root directory
project_root = os.path.abspath(os.path.join(current_dir, "..", ".."))

# Add the project root directory to the Python path
sys.path.append(project_root)
from rxconfig import config
import reflex as rx
from gemini_api.api import extract_text_from_pdf, model
import google.generativeai as genai

docs_url = "https://reflex.dev/docs/getting-started/introduction/"
filename = f"{config.app_name}/{config.app_name}.py"
pg_size = "150"
black = "rgba(0, 0, 0, 0.97)"
white = "rgba(255, 255, 255, 0.97)"

def upload_to_gemini(pdf_path):
    """Upload the PDF file to GeminiAPI."""
    text_data = extract_text_from_pdf(pdf_path)
    time = "3 months"
    mental_health = "test anxiety, burnt out"
    combined_prompt = time + "\n" + mental_health + "\n" + text_data
    response = model.generate_content(combined_prompt)
    print(response.text)

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

    # The images to show.
    img: list[str]
    
    # currently doesn't handle clicking the upload button yet not inputting any files; files = [] #type annotation?
    async def handle_upload(self, files: list[rx.UploadFile]):
        """Handle the upload of file(s)."""

        for file in files:
            try:
                # Get the path to the uploaded file
                pdf_path = os.path.join(rx.get_upload_dir(), file.filename)
                
                # Save the uploaded file
                with open(pdf_path, "wb") as pdf_file:
                    upload_data = await file.read()
                    pdf_file.write(upload_data)

                # Upload PDF to Gemini and convert to text
                upload_to_gemini(pdf_path)

                # Update the img var
                self.img.append(file.filename)
            except Exception as e:
                print(f"Error handling upload: {e}")

    def upload_page(self):
        return rx.redirect("/upload")
    def studyplan_page(self):
        return rx.redirect("/studyplan")

header1_style = { #sets font for header
    "font_family": "Arial Rounded MT Bold",
}

style1 = {
    "font_family": "Arial",
    rx.button: {
        "background_color": rx.color_mode_cond("#C3E3C3", "#568356"), #default CSS color: DarkSeaGreen
        "color": "black",
    },
}

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
            rx.button(
                    "Home",
                    on_click=lambda: rx.redirect("/"),
                    size="3",
                    radius="full",
                    background_color=rx.color_mode_cond("#C3E3C3", "#568356"),
                    color=rx.color_mode_cond(black, white),
                ),
            rx.color_mode.button(rx.color_mode.icon(), size="3", float="right", color=rx.color_mode_cond(black, white)),
            bg=rx.color_mode_cond(white, black),
            align="center",
            justify="center",
            border_bottom="0.2em solid #F0F0F0",
            padding_x="10em",
            padding="1.5em",
            spacing="4",
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
        with open("form_data.txt", "w") as file:
            file.write(selected_options_string + "\n")
            file.write(time_str + "\n")

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
                        rx.button("start a plan",
                                  type="submit",
                                  background_color="#C3E3C3",
                                  on_click=State.upload_page,
                        ),
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
        background=rx.color_mode_cond(
            "radial-gradient(circle at 22% 11%,rgba(229, 255, 231,0.8),hsla(0,0%,100%,0) 30%),radial-gradient(circle at 82% 40%,rgba(253, 251, 230,0.8),hsla(0,0%,100%,0) 45%),radial-gradient(circle at 15% 85%,rgba(255, 227, 237, 0.8),hsla(0,0%,100%,0) 40%)",
            "radial-gradient(circle at 22% 11%,rgba(124, 147, 124,0.8),hsla(0,0%,100%,0) 30%),radial-gradient(circle at 82% 40%,rgba(187, 184, 159,0.8),hsla(0,0%,100%,0) 45%),radial-gradient(circle at 15% 85%,rgba(221, 203, 209, 0.8),hsla(0,0%,100%,0) 40%)"
        ),                 
    )

# class VarActionState(rx.State):
#     def act(self):
#         State.handle_upload(rx.upload_files(upload_id="upload_file")),
#         State.studyplan_page,

def upload():
    """The main view"""
    return rx.center(
        navigation(),
        rx.vstack(
            rx.heading("Your upload page", size="8", style=header1_style),
            rx.upload(
                rx.vstack(
                    rx.button("Select file", bg="white", size="4", radius="full", color=rx.color_mode_cond(black, white), background_color=rx.color_mode_cond("#C3E3C3", "#568356")),
                    rx.text(
                        "Drag and drop files here or click to select files",
                        size="7",
                        font_family="Arial",
                    ),
                    spacing="7",
                ),
                id="upload_file",
                border=f"1px dotted {rx.color_mode_cond(black, white)}",
                border_radius="25px",
                background_color=rx.color_mode_cond(white, black),
                padding="5em",
                align="center",
                width="85%",    
            ),
            rx.hstack(rx.foreach(rx.selected_files("upload_file"), rx.text)),
            rx.flex(
                rx.button(
                    "Get my plan",
                    on_click=State.studyplan_page,
                    size="4",
                    radius="full",
                    background_color=rx.color_mode_cond("#C3E3C3", "#568356"),
                    color=rx.color_mode_cond(black, white),
                ),
                rx.button(
                    "Upload",
                    on_click=State.handle_upload(rx.upload_files(upload_id="upload_file")),
                    size="4",
                    radius="full",
                    background_color=rx.color_mode_cond("#C3E3C3", "#568356"),
                    color=rx.color_mode_cond(black, white),
                ),
                rx.button(
                    "Clear",
                    on_click=rx.clear_selected_files("upload_file"),
                    size="4",
                    radius="full",
                    background_color=rx.color_mode_cond("rgba(255, 227, 237, 0.8)", "rgba(244, 189, 208, 0.8)"),
                    color=rx.color_mode_cond(black, white),
                ),
                
                rx.foreach(State.img, lambda img: rx.image(src=rx.get_upload_url(img))),

                spacing="3",
                align="center",
            ),
            align="center",
            spacing="5",
            font_size="2em",
            height="110vh",
        ),
        padding="1em",
        height=pg_size + "vh",
        background=rx.color_mode_cond(
            "radial-gradient(circle at 22% 11%,rgba(229, 255, 231,0.8),hsla(0,0%,100%,0) 30%),radial-gradient(circle at 82% 40%,rgba(253, 251, 230,0.8),hsla(0,0%,100%,0) 45%),radial-gradient(circle at 15% 85%,rgba(255, 227, 237, 0.8),hsla(0,0%,100%,0) 40%)",
            "radial-gradient(circle at 22% 11%,rgba(124, 147, 124,0.8),hsla(0,0%,100%,0) 30%),radial-gradient(circle at 82% 40%,rgba(187, 184, 159,0.8),hsla(0,0%,100%,0) 45%),radial-gradient(circle at 15% 85%,rgba(221, 203, 209, 0.8),hsla(0,0%,100%,0) 40%)"
        ),  
    )

def studyplan() -> rx.Component:
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
        height="300vh",
        background=rx.color_mode_cond(
            "radial-gradient(circle at 22% 11%,rgba(229, 255, 231,0.8),hsla(0,0%,100%,0) 30%),radial-gradient(circle at 82% 40%,rgba(253, 251, 230,0.8),hsla(0,0%,100%,0) 45%),radial-gradient(circle at 15% 85%,rgba(255, 227, 237, 0.8),hsla(0,0%,100%,0) 40%)",
            "radial-gradient(circle at 22% 11%,rgba(124, 147, 124,0.8),hsla(0,0%,100%,0) 30%),radial-gradient(circle at 82% 40%,rgba(187, 184, 159,0.8),hsla(0,0%,100%,0) 45%),radial-gradient(circle at 15% 85%,rgba(221, 203, 209, 0.8),hsla(0,0%,100%,0) 40%)"
        ), 
    )

app = rx.App(style=style1,
             theme=rx.theme(
                appearance="light", has_background=True, radius="full"
            )
            )
app.add_page(index, title="studydino | home")
app.add_page(upload, route="/upload", title="studydino | upload")
app.add_page(studyplan, route="/studyplan", title="studydino | studyplan")