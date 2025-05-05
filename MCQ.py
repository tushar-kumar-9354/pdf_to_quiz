from dotenv import load_dotenv
import os
import PyPDF2
import google.generativeai as genai

# Load API Key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Extract text from PDF using PyPDF2
def extract_text_from_pdf(pdf_file_path):
    text = ""
    with open(pdf_file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() or ""
    return text

# Generate MCQs using Gemini
def generate_mcq_questions_and_answers_from_pdf(pdf_file_path, difficulty_level, num_questions):
    pdf_text = extract_text_from_pdf(pdf_file_path)

    prompt = f"""
    Generate {num_questions} multiple-choice questions (MCQs) with four options (A, B, C, D) and provide the correct answer label only (A, B, C, or D).
    Difficulty Level: {difficulty_level}
    Content:
    {pdf_text[:5000]}

    Format:
    Q1. <Question text>
    A) <Option 1>
    B) <Option 2>
    C) <Option 3>
    D) <Option 4>
    Answer: <A/B/C/D>
    """

    model = genai.GenerativeModel('gemini-2.0-flash')
    response = model.generate_content(prompt)

    questions, options, answers = [], [], []

    if response.text:
        question_blocks = response.text.strip().split("\n\n")
        for block in question_blocks:
            lines = block.strip().split("\n")
            if len(lines) >= 6:
                question = lines[0].strip()
                option_a = lines[1].split("A) ")[-1].strip()
                option_b = lines[2].split("B) ")[-1].strip()
                option_c = lines[3].split("C) ")[-1].strip()
                option_d = lines[4].split("D) ")[-1].strip()
                answer = lines[5].split("Answer: ")[-1].strip().upper()

                questions.append(question)
                options.append([option_a, option_b, option_c, option_d])
                answers.append(answer)

    return questions, options, answers
