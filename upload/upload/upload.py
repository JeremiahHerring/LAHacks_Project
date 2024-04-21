"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from rxconfig import config

import reflex as rx

docs_url = "https://reflex.dev/docs/getting-started/introduction/"
filename = f"{config.app_name}/{config.app_name}.py"
color = "rgb(107,99,246)"

class State(rx.State):
    """The app state."""

    # The images to show.
    img: list[str]
    
    # currently doesn't handle clicking the upload button yet not inputting any files; files = [] #type annotation?
    async def handle_upload(self, files: list[rx.UploadFile]):
        """Handle the upload of file(s)."""

        for file in files:
            try:
                upload_data = await file.read()
                outfile = rx.get_upload_dir() / file.filename

                # Save file
                with outfile.open("wb") as file_object:
                    file_object.write(upload_data)

                # Update the img var
                self.img.append(file.filename)
            except:
                pass


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