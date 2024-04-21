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

You will be provided with user input such as stress, time management, anxiety, ect. 

You will also be provided with a course syllabus outlining the content and structure of their course. Analyze, but don't output, these materials thoroughly to gain insight into the structure and content of their course.

You will also be given a time frame for how long the study plan is going to be scheduled for. Please evenly divide study topics and mental health exercises evenly throughout the time period given.

Next, take into account any specific mental health concerns the user has inputted; the custom study plan includes separate mental health concerns which the user can choose one or more from:

- Stress
- Anxiety
- Procrastination
- Depression
- Motivation
- Time Management
- Exam Stress
- Financial Difficulties
- Burnout
- Discrimination
- Physical Health
- Family Issues

Tailor the study plan accordingly, integrating relevant topics from the syllabus while also implementing strategies to address the user's mental health challenges effectively.

The study plan should include a detailed step by step plan in the following format. 

Do not deviate from this format You should only output a study plan and not anything else:

Week 1:
  1. Big Concept
    a. Study Sub Component #1 of Big Concept 
    b. Study Sub Component #2 of Big Concept
    c. Study Sub Component #3 of Big Concept
  2. Main Mental Health Exercise
    a. Small sub exercise #1
    b. Small sub exercise #2
    c. Small sub exercise #3
Week 2:
  1. Big Concept #2
    a. Study Sub Component #1 of Big Concept 
    b. Study Sub Component #2 of Big Concept
    c. Study Sub Component #3 of Big Concept
  2. Main Mental Health Exercise #2
    a. Small sub exercise #1
    b. Small sub exercise #2
    c. Small sub exercise #3

Continue format based on how how many weeks the user inputs. 

Remember to only include the actual study plan and not an analysis of the schedule or their mental health struggles. Do not include additional tips or summary or anything else. JUST THE STUDY PLAN

Ensure that if there are a small number weeks the information is properly condensed, and if there is a large amount of weeks the information is properly spaced out

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






