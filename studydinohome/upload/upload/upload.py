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
color = "rgb(107,99,246)"
pg_size = "150"
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

def upload_to_gemini(pdf_path):
    """Upload the PDF file to GeminiAPI."""
    text_data = extract_text_from_pdf(pdf_path)
    time = ""
    mental_health = ""
    with open("form_data.txt", "r") as file:
        time = file.readline().strip()
        mental_health = file.readline().strip()
    combined_prompt = time + "\n" + mental_health + "\n" + text_data
    response = model.generate_content(combined_prompt)
    with open("response.txt", "w") as file:
            file.write(response + "\n")
    

class State(rx.State):
    """The app state."""

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

def index():
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
                    background_color=rx.color_mode_cond("#C3E3C3", "#568356"),
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
        background="radial-gradient(circle at 22% 11%,rgba(229, 255, 231,0.8),hsla(0,0%,100%,0) 30%),radial-gradient(circle at 82% 40%,rgba(253, 251, 230,0.8),hsla(0,0%,100%,0) 45%),radial-gradient(circle at 15% 85%,rgba(255, 227, 237, 0.8),hsla(0,0%,100%,0) 40%)",
    )

app = rx.App(style=style1,
             theme=rx.theme(
                appearance="light", has_background=True, radius="full"
            )
            )
app.add_page(index, title="studydino | upload")
