import streamlit as st
import os
import json
from langchain.chat_models import ChatOpenAI



from utils import process_file_with_dedoc, extract_text_from_all_levels, generate_formatted_resume, generate_json_structured_resume
from utils_files import save_parsed_resume_as_text, save_parsed_resume_as_json


# os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

chat_llm_text = ChatOpenAI(model='gpt-3.5-turbo', temperature=0.0)
chat_llm_json = ChatOpenAI(model='gpt-3.5-turbo', temperature=0.0)

def home_page():
    # Home page
    st.write("This is the home page of the application.")
    # You can add more information about your application here


def parser():
    # Parser section
    uploaded_files = st.file_uploader("Upload Files", type=["jpg", "jpeg", "png", "docx", "pdf", "html", "doc"],
                                      accept_multiple_files=True)

    if uploaded_files:
        st.write("Uploaded Resumes:")
        for resume in uploaded_files:

            st.write(resume.name)

            st.write("Parsed Resume:")

            text = process_file_with_dedoc(resume)
            text_f = extract_text_from_all_levels(text)
            if text:
                parsed_resume = generate_formatted_resume(text_f, chat_llm_text)

                st.text(parsed_resume)
                # Display extracted text on the app

            st.write("Parsed JSON Formated Resume:")
            parsed_json_resume = generate_json_structured_resume(text_f, chat_llm_json)
            print(parsed_json_resume)
            json_data = json.dumps(parsed_json_resume, indent=4)
            st.json(json_data)

            # Adding download buttons
            if parsed_resume:
                # Text file download button
                text_file_path = save_parsed_resume_as_text(parsed_resume, resume.name)
                st.download_button(label="Download Text File", data=open(text_file_path, 'rb'),
                                   file_name=f"{resume.name}.txt", mime="text/plain")

            if parsed_json_resume:
                # JSON file download button
                json_file_path = save_parsed_resume_as_json(parsed_json_resume, resume.name)
                st.download_button(label="Download JSON File", data=open(json_file_path, 'rb'),
                                   file_name=f"{resume.name}.json", mime="application/json")


def about():
    st.title("About This Application")
    st.write("""
    ResumeRevealer is developed by a team of passionate developers dedicated to revolutionizing the resume parsing process 
    and empowering users with comprehensive insights into their resumes. Our team comprises third year Artificial Intelligence and Machine Learning students of Symbiosis Institute of technology
    , Pune.

    **Meet Our Team:**
    - Jainil Patel: Email: jainil23@gmail.com
    - Divyam Kumar: Email: divyamkr100@gmail.com
    - Amitesh Patra: Email: amitesh67@gmail.com

    If you have any questions, feedback, or suggestions, feel free to reach out to us. We are committed to continuously improving 
    ResumeRevealer to meet your resume parsing needs.

    Thank you for choosing ResumeRevealer!
    """)
    
    
   


def main():
    st.title("ResumeRevealer")

    tab1, tab2, tab3 = st.tabs(["Our Project", "Model", "About us"])
    with tab1:
        home_page()
    with tab2:
        parser()
    with tab3:
        about()


if __name__ == "__main__":
    main()
