Sure! Here’s an enhanced version of your `README.md` for your **TUSHAR PDF to MCQ Generator** project, making it more comprehensive and structured:

---

# TUSHAR PDF to MCQ Generator: Transforming PDFs into Interactive Quizzes 🚀

The **MCQ Generator** is an innovative web application that allows users to effortlessly convert PDF documents into interactive multiple-choice quizzes. This app integrates **Google's Generative AI** and **Streamlit** to provide an intuitive, engaging, and fully customizable quiz experience.

## Table of Contents

1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Configuration](#configuration)


## Features

* **Generate MCQs from PDFs**: Seamlessly convert your PDFs into multiple-choice questions, enhancing your learning or teaching experience.
* **Customizable Difficulty Levels**: Select from three difficulty levels (Easy, Medium, Hard) to match your learning or quiz needs.
* **Adjustable Question Count**: Specify how many questions you want the app to generate based on the content of your PDF.
* **Interactive and Engaging Interface**: A sleek, intuitive interface for answering questions and tracking your progress.
* **Progress Tracking**: Keep track of the questions you've attempted and receive detailed feedback upon quiz completion.
* **Detailed Results & Answer Key**: Get your score, along with a detailed answer key, after submitting your quiz for further analysis.

## Installation

Follow these steps to set up the project locally:

1. **Clone the repository**:
   First, clone the repository to your local machine:

   ```bash
   git clone https://github.com/tushar-kumar-9354/pdf_to_quiz.git
   ```

2. **Navigate to the project directory**:
   Change to the project folder:

   ```bash
   cd pdf_to_quiz
   ```

3. **Install dependencies**:
   Install all required libraries and dependencies by running the following command:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up Google API key**:

   * Create a `.env` file in the root directory of the project.
   * Add your Google API key to the `.env` file:

     ```
     GEMINI_API_KEY=your_api_key_here
     ```

   **Note**: You can get a Google API key by following the [Google API documentation](https://cloud.google.com/docs/authentication/getting-started).

## Usage

To run the application locally, follow these steps:

1. **Start the Streamlit app**:

   ```bash
   streamlit run app.py
   ```

2. **Upload a PDF file**:
   Use the file uploader to select the PDF document you want to convert into a quiz.

3. **Select quiz settings**:

   * Choose the **difficulty level** (Easy, Medium, or Hard).
   * Specify the **number of questions** you wish to generate.

4. **Start the quiz**:
   Click the "Start Quiz" button to begin answering the MCQs generated from the PDF.

5. **Submit the quiz**:
   After answering all the questions, click the "Submit" button to see your results and the answer key.

## Configuration

You can customize the app’s settings through the following configurations:

* **Difficulty Levels**: Select from Easy, Medium, or Hard. The app uses a generative AI model to tailor the complexity of the questions based on the difficulty setting.
* **Number of Questions**: Define the number of questions to be generated from your PDF. The more questions, the more thorough the quiz.

## Contributing

We welcome contributions from the community to make this project even better! Here’s how you can contribute:

1. Fork this repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature/your-feature-name`).
6. Open a pull request to the `main` branch.



