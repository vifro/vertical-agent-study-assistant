import streamlit as st
from agent.qa.qa_agent import QAGenerationAgent
from database.handler import DatabaseHandler

# Initialize session state variables if they don't exist
if 'current_question' not in st.session_state:
    st.session_state.current_question = None
if 'submitted' not in st.session_state:
    st.session_state.submitted = False

# Initialize the DatabaseHandler and fetch lecture titles
db_handler = DatabaseHandler()
lecture_titles = db_handler.fetch_all_lecture_titles()

st.title("Vertical Study Agent - QA Generator")
st.markdown("Select a lecture to generate a multiple-choice question:")

# Display a dropdown of available lecture titles
selected_lecture = st.selectbox("Lecture Title", lecture_titles)

# When a lecture is selected, fetch and display its transcript
if selected_lecture:
    transcript_text = db_handler.get_transcript(selected_lecture)
    st.subheader("Transcript")
    st.text_area("Transcript", value=transcript_text, height=200)

    # Clear the current question and submission state when generating a new question
    if st.button("Generate Question"):
        st.session_state.submitted = False
        if transcript_text:
            with st.spinner("Generating question..."):
                # Initialize the QA generation agent
                qa_agent = QAGenerationAgent(model_name="deepseek-r1:8b")
                qa_result = qa_agent.process(transcript_text)

                try:
                    # Check if we have a successful response
                    if qa_result.get("status") != "success":
                        st.error("Failed to generate question")
                        with st.expander("Show error details"):
                            st.write(qa_result.get("error", {}))
                        st.stop()

                    # Store the question data in session state
                    st.session_state.current_question = qa_result.get("data", {}).get("qa", {})
                    
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
                    with st.expander("Show debug information"):
                        st.write("Raw QA result:", qa_result)
                        st.write("Error details:", str(e))
                    st.session_state.current_question = None

    # Display the current question if it exists
    if st.session_state.current_question:
        qa_data = st.session_state.current_question
        
        st.subheader("Generated Question")
        st.write(qa_data.get("question", "No question provided."))

        # Create a radio button list for the answer options
        options = qa_data.get("options", {})
        if options:
            option_keys = list(options.keys())
            user_answer = st.radio(
                "Select your answer:",
                option_keys,
                format_func=lambda key: f"{key}: {options[key]}"
            )

            # Submit button for the answer
            submit = st.button("Submit Answer")
            if submit:
                st.session_state.submitted = True

            # Show feedback if answer was submitted
            if st.session_state.submitted:
                correct = qa_data.get("correct_answer", "")
                if user_answer == correct:
                    st.success("🎉 Correct!")
                else:
                    st.error(f"❌ Incorrect. The correct answer was {correct}.")
                
                st.markdown("**Explanation:**")
                st.markdown(qa_data.get("explanation", "No explanation provided."))
                
                # Add a "Try Another Question" button
                if st.button("Try Another Question"):
                    st.session_state.current_question = None
                    st.session_state.submitted = False
                    st.rerun()
        else:
            st.error("No options available.")
else:
    st.error("Please select a lecture to continue.")