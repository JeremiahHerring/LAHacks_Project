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

def upload_to_gemini(pdf_path):
    """Upload the PDF file to GeminiAPI."""
    text_data = extract_text_from_pdf(pdf_path)
    time = "3 months"
    mental_health = "test anxiety, burnt out"
    combined_prompt = time + "\n" + mental_health + "\n" + text_data
    response = model.generate_content(combined_prompt)
    print(response.text)

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

def index():
    """The main view"""
    return rx.center(
        rx.vstack(
                rx.upload(
                    rx.vstack(
                        rx.button("Select File", color=color, bg="white", border=f"1px solid {color}",),
                        rx.text("Drag and drop files here or click to select files"),
                    ),
                    id="upload_file",
                    border=f"1px dotted {color}",
                    padding="5em",
                    align="center",
                    
                ),
                rx.hstack(rx.foreach(rx.selected_files("upload_file"), rx.text)),
                rx.flex(
                    rx.button(
                        "Upload",
                        on_click=State.handle_upload(rx.upload_files(upload_id="upload_file")),
                    ),
                    rx.button(
                        "Clear",
                        on_click=rx.clear_selected_files("upload_file"),
                    ),
                    
                    rx.foreach(State.img, lambda img: rx.image(src=rx.get_upload_url(img))),

                    spacing="2",
                    align="center",

                ),
                
            
                padding="5em",
        )

    )

app = rx.App()
app.add_page(index)
