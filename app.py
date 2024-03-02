import streamlit as st
import os
import json
from langchain.chat_models import ChatOpenAI



from utils import process_file_with_dedoc, extract_text_from_all_levels, generate_formatted_resume, generate_json_structured_resume
from utils_files import save_parsed_resume_as_text, save_parsed_resume_as_json


# os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

chat_llm_text = ChatOpenAI(model='gpt-3.5-turbo', temperature=0.5)
chat_llm_json = ChatOpenAI(model='gpt-3.5-turbo', temperature=0.5)

def home_page():
    # Home page
    st.write("""
    ResumeRevealer is an advanced tool designed to extract detailed information from resumes in various formats 
    such as PDF, HTML, JPG, DOC, and more. It aims to provide a comprehensive analysis of resumes, including 
    categorizing text into distinct sections such as education, work experience, and skills. Additionally, 
    ResumeRevealer addresses several challenges to enhance resume parsing:
    """)
    
    st.subheader("Primary Challenges:")
    st.write("""
    1. **Comprehensive Parsing:** Extract detailed information from resumes and sequence them based on dates.
    2. **Standardization:** Standardize job titles and occupations against the O-NET database for consistent taxonomy.
    3. **Skill Extraction:** Mine detailed skills and competencies from project descriptions and position roles.
    """)
    
    st.subheader("Key Features:")
    st.write("""
    - **Resume Parsing:** Extracts detailed information from resumes in various formats.
    - **Text and JSON Output:** Presents parsed information in both text and JSON formats.
    - **Standardized Job Titles:** Ensures consistency in job titles and occupations.
    - **Abstractive Skill Extraction:** Extracts and abstracts skills from project descriptions and job roles.
    - **Career Trajectory Prediction:** Predicts career trajectory based on parsed resume data.
    - **Downloadable Results:** Allows users to download parsed results in text or JSON format for further analysis.
    """)
    
    st.subheader("How to Use:")
    st.write("""
    1. **Upload Resumes:** Upload your resume(s) in any supported format (PDF, HTML, JPG, DOC, etc.).
    2. **Parsing:** ResumeRevealer will process the resumes and extract detailed information.
    3. **Exploration:** Explore the parsed information including education, work experience, skills, and more.
    4. **Download Results:** Download the parsed results in either text or JSON format for further analysis.
    """)


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
    and empowering users with comprehensive insights into their resumes. Our team comprises third year Artificial Intelligence and Machine Learning students of Symbiosis Institute of Technology, Pune.

    **Meet Our Team:**""")

    # Use columns layout option for horizontal arrangement
    col1, col2 = st.columns(2)

    # Team Member 1: Jainil Patel
    with col1:
        st.image("Images/jainil.jpg", width=100)
        st.write("""
        <ul style="list-style-type: none; padding-left: 0;">
        <li>&#10148; <b>Name:</b> Jainil Patel</li>
        <li>&#10148; <b>Branch:</b> Artificial Intelligence and Machine Learning</li>
        <li>&#10148; <b>LinkedIn:</b> <a href="https://www.linkedin.com/in/jainil-patel">Jainil Patel</a></li>
        <li>&#10148; <b>GitHub:</b> <a href="https://github.com/jainil23">jainil23</a></li>
        <li>&#10148; <b>Email:</b> jainil23@gmail.com</li>
        <li>&#10148; <b>Phone:</b> +91 XXXXXXXXXX</li>
        </ul>""", unsafe_allow_html=True)
    
    # Team Member 2: Divyam Kumar
    with col2:
        st.image("Images/prof.jpg", width=100)
        st.write("""
        <ul style="list-style-type: none; padding-left: 0;padding-bottom: 20px">
        <li>&#10148; <b>Name:</b> Divyam Kumar</li>
        <li>&#10148; <b>Branch:</b> Artificial Intelligence and Machine Learning</li>
        <li>&#10148; <b>LinkedIn:</b> <a href="https://www.linkedin.com/in/divyam-kumar">Divyam Kumar</a></li>
        <li>&#10148; <b>GitHub:</b> <a href="https://github.com/divyamkr100">divyamkr100</a></li>
        <li>&#10148; <b>Email:</b> divyamkr100@gmail.com</li>
        <li>&#10148; <b>Phone:</b> +91 XXXXXXXXXX</li>
        </ul>""", unsafe_allow_html=True)
    
    st.markdown("""
    <div style="text-align: center;">
        <img src="Images/amitesh.jpg" width="100">
        <ul style="list-style-type: none; padding-left: 0;">
            <li>&#10148; <b>Name:</b> Amitesh Patra</li>
            <li>&#10148; <b>Branch:</b> Artificial Intelligence and Machine Learning</li>
            <li>&#10148; <b>LinkedIn:</b> <a href="https://www.linkedin.com/in/amitesh-patra">Amitesh Patra</a></li>
            <li>&#10148; <b>GitHub:</b> <a href="https://github.com/amitesh67">amitesh67</a></li>
            <li>&#10148; <b>Email:</b> amitesh67@gmail.com</li>
            <li>&#10148; <b>Phone:</b> +91 XXXXXXXXXX</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("""If you have any questions, feedback, or suggestions, feel free to reach out to us. We are committed to continuously improving 
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
