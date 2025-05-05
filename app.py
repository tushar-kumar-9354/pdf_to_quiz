import streamlit as st
import os
from dotenv import load_dotenv
from MCQ import generate_mcq_questions_and_answers_from_pdf
import io

# Load environment variables
load_dotenv()

def format_answer_key(questions, options, key_answers, user_answers):
    letter_map = {0: "A", 1: "B", 2: "C", 3: "D"}
    answer_text = "Answer Key\n\n"
    for i, (q, opts, correct, user_ans) in enumerate(zip(questions, options, key_answers, user_answers), start=1):
        answer_text += f"Q{i}: {q}\n"
        for idx, opt in enumerate(opts):
            label = letter_map[idx]
            answer_text += f"   {label}. {opt}\n"
        answer_text += f"Correct Answer: {correct}\n"
        answer_text += f"Your Answer: {user_ans if user_ans else 'Not Attempted'}\n"
        answer_text += "-" * 40 + "\n"
    return answer_text

def main():
    st.set_page_config(page_title="PDF to Quiz App", layout="wide")

    st.title("📘 PDF to MCQ Quiz Generator")

    if "questions" not in st.session_state:
        st.markdown("Upload a PDF, select difficulty and number of questions, then start the quiz.")

        # Create a vertical layout with equal sizes
        with st.form(key="quiz_form"):
            col1, col2, col3 = st.columns(3)

            with col1:
                pdf_file = st.file_uploader("Upload your PDF file", type=["pdf"], label_visibility="collapsed")
            with col2:
                num_questions = st.number_input("Number of Questions", min_value=1, max_value=30, label_visibility="collapsed")
            with col3:
                difficulty = st.selectbox("Select Difficulty", ["Easy", "Medium", "Hard"], label_visibility="collapsed")

            # Submit button for form
            submit_button = st.form_submit_button(label="Generate Quiz")

            if submit_button:
                if pdf_file and num_questions and difficulty:
                    pdf_path = pdf_file.name
                    with open(pdf_path, "wb") as f:
                        f.write(pdf_file.getbuffer())

                    questions, options, key_answers = generate_mcq_questions_and_answers_from_pdf(
                        pdf_path, difficulty, num_questions
                    )

                    if questions:
                        st.session_state["questions"] = questions
                        st.session_state["options"] = options
                        st.session_state["key_answers"] = key_answers
                        st.session_state["user_answers"] = [None] * len(questions)
                        st.session_state["attempted_questions"] = [False] * len(questions)
                        st.session_state["submitted"] = False
                        st.rerun()
                    else:
                        st.error("Unable to generate questions. Please try another file.")
    else:
        st.subheader("Quiz Questions")

        questions = st.session_state["questions"]
        options = st.session_state["options"]
        key_answers = st.session_state["key_answers"]
        user_answers = st.session_state["user_answers"]
        attempted_questions = st.session_state["attempted_questions"]
        letter_map = {0: "A", 1: "B", 2: "C", 3: "D"}

        for i, (q, opts, attempted) in enumerate(zip(questions, options, attempted_questions), start=1):
            st.markdown(f"**Q{i}.** {q}")
            user_answer = st.radio("Choose an option:", opts, key=f"question_{i}", index=None, label_visibility="collapsed")
            if user_answer is not None:
                st.session_state["user_answers"][i - 1] = user_answer
                st.session_state["attempted_questions"][i - 1] = True
            st.markdown("---")

        attempted_count = sum(attempted_questions)
        st.info(f"Attempted: {attempted_count}/{len(questions)}")

        if st.button("Submit Quiz"):
            st.session_state["submitted"] = True

        if st.session_state.get("submitted", False):
            score = 0
            st.subheader("Results")
            for i, (user_ans, opts, correct_label, attempted) in enumerate(zip(user_answers, options, key_answers, attempted_questions), start=1):
                user_label = None
                if attempted:
                    user_index = opts.index(user_ans)
                    user_label = letter_map[user_index]
                    correct = user_label == correct_label
                    if correct:
                        score += 1
                        st.success(f"Q{i}: Correct")
                    else:
                        st.error(f"Q{i}: Incorrect (Correct: {correct_label})")
                else:
                    st.warning(f"Q{i}: Not Attempted")

            st.markdown(f"### Final Score: {score}/{len(questions)}")

            # Answer Key Download
            answer_key_text = format_answer_key(questions, options, key_answers, user_answers)
            st.download_button(
                label="📄 Download Answer Key",
                data=answer_key_text,
                file_name="answer_key.txt",
                mime="text/plain"
            )

            

if __name__ == "__main__":
    main()
