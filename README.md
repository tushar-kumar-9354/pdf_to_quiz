# Shree MCQ Generator: Transforming PDFs into Interactive Quizzes 🚀

The MCQ Generator is a powerful web application that allows users to generate multiple-choice questions (MCQs) from PDF files. This application leverages the power of Google's Generative AI and Streamlit to create an interactive and user-friendly experience.

## Features

- **Generate MCQs from PDF files**: Easily convert your PDF documents into interactive quizzes.
- **Select Difficulty Level**: Choose from three difficulty levels (Easy, Medium, or Hard) to suit your needs.
- **Customizable Question Count**: Specify the desired number of questions to generate.
- **Interactive Quiz Interface**: Engage with the generated questions in a sleek and intuitive interface.
- **Question Tracking**: Keep track of the questions you've attempted and those you haven't.
- **Results and Answer Key**: Upon submission, view your score and the answer key for further analysis.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/tushar-kumar-9354/pdf_to_quiz.git
```

2. Navigate to the project directory:

cd "project directory"
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Set up the Google API key:
   - Create a `.env` file in the project root directory.
   - Add your Google API key to the file: `GEMINI_API_KEY=your_api_key_here`

## Usage

1. Run the Streamlit app:

```bash
streamlit run app.py
```

2. Upload a PDF file through the file uploader.
3. Select the difficulty level and the number of questions to generate.
4. Click the "Start Quiz" button to generate the MCQs.
5. Answer the questions and click the "Submit" button to view your results and the answer key.

"""""""DONE"""""""