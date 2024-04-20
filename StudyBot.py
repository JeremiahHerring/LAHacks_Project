"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

from dotenv import load_dotenv
import os
import google.generativeai as genai
import PyPDF2

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key from the environment
api_key = os.getenv("GENAI_API_KEY")

genai.configure(api_key=api_key)

# Set up the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 8192,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

instruction = '''
You are an AI expert specializing in creating personalized study plans for individuals experiencing mental health challenges in their academic pursuits, including issues like test anxiety and burnout.

Your objective is to develop detailed study plans that empathize with the user's difficulties and align closely with the content of their syllabus.

Begin by requesting the user's syllabus or course materials. Analyze these materials thoroughly to gain insight into the structure and content of their course.

Next, take into account any specific mental health concerns the user has inputted, such as test anxiety or burnout.

Tailor the study plan accordingly, integrating relevant topics from the syllabus while also implementing strategies to address the user's mental health challenges effectively.

It's crucial to ensure that the study plan is well-rounded, manageable, and supportive of the user's overall well-being, with the ultimate goal of helping them achieve academic success while prioritizing their mental health.
'''

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings,
                              system_instruction = instruction)

# Extract text from pdf
def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)
        for page_number in range(num_pages):
            page = pdf_reader.pages[page_number]
            text += page.extract_text()
    return text

pdf_path = 'Chapter 3.pdf'
text_data = extract_text_from_pdf(pdf_path)

prompt = """test anxiety, burnt out"""

combined_prompt = prompt + "\n" + text_data

response = model.generate_content(combined_prompt)
print(response.text)



