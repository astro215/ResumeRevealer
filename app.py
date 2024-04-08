import streamlit as st
import os
import json
from langchain.chat_models import ChatOpenAI
import shutil



from utils import process_file_with_dedoc, extract_text_from_all_levels, generate_formatted_resume, generate_json_structured_resume, create_career_trajectory
from utils_files import save_parsed_resume_as_text, save_parsed_resume_as_json
from onet import onet_job_title_to_onet_code

TEMP_DIR = "temp_files"
TEMP_DIR_TEXT = "temp_files_text"
TEMP_DIR_JSON = "temp_files_json"



# os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]


def home_page():
    # Home page title
    st.title("Welcome to ResumeRevealer - Your Comprehensive Resume Parser!")

    # Introduction section
    # Introduction section
    st.markdown("""
    <div style="margin-top: 20px; margin-bottom: 30px;">
        <p style="font-size: 18px; text-align: center;">ResumeRevealer is an advanced tool designed to extract detailed information from resumes in various formats such as PDF, HTML, JPG, DOC, and more. It aims to provide a comprehensive analysis of resumes, including categorizing text into distinct sections such as education, work experience, and skills.</p>
        <p style="font-size: 18px; text-align: center;">Additionally, ResumeRevealer addresses several challenges to enhance resume parsing:</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.subtitle("Challenges section")
    st.subheader("Primary Challenges:")
    st.markdown("""
    <div style="margin-bottom: 30px;">
        <p style="font-size: 16px;">1. <b>Comprehensive Parsing:</b> Extract detailed information from resumes and sequence them based on dates.</p>
        <p style="font-size: 16px;">2. <b>Standardization:</b> Standardize job titles and occupations against the O-NET database for consistent taxonomy.</p>
        <p style="font-size: 16px;">3. <b>Skill Extraction:</b> Mine detailed skills and competencies from project descriptions and position roles.</p>
    </div>
    """, unsafe_allow_html=True)

    # Key Features section
    st.subheader("Key Features:")
    st.markdown("""
    <div style="margin-bottom: 30px;">
        <ul style="font-size: 16px;">
            <li><b>Resume Parsing:</b> Extracts detailed information from resumes in various formats.</li>
            <li><b>Text and JSON Output:</b> Presents parsed information in both text and JSON formats.</li>
            <li><b>Standardized Job Titles:</b> Ensures consistency in job titles and occupations.</li>
            <li><b>Abstractive Skill Extraction:</b> Extracts and abstracts skills from project descriptions and job roles.</li>
            <li><b>Career Trajectory Prediction:</b> Predicts career trajectory based on parsed resume data.</li>
            <li><b>Downloadable Results:</b> Allows users to download parsed results in text or JSON format for further analysis.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # How to Use section
    st.subheader("How to Use:")
    st.markdown("""
    <div style="margin-bottom: 30px;">
        <ol style="font-size: 16px;">
            <li><b>Upload Resumes:</b> Upload your resume(s) in any supported format (PDF, HTML, JPG, DOC, etc.).</li>
            <li><b>Parsing:</b> ResumeRevealer will process the resumes and extract detailed information.</li>
            <li><b>Exploration:</b> Explore the parsed information including education, work experience, skills, and more.</li>
            <li><b>Download Results:</b> Download the parsed results in either text or JSON format for further analysis.</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)


def parser():
    # Parser section
    uploaded_files = st.file_uploader("Upload Files", type=["jpg", "jpeg", "png", "docx", "pdf", "html", "doc"],
                                      accept_multiple_files=True)

    if uploaded_files:
        # if os.path.exists(TEMP_DIR_TEXT):
        #     shutil.rmtree(TEMP_DIR_TEXT)
        # if os.path.exists(TEMP_DIR_JSON):
        #     shutil.rmtree(TEMP_DIR_JSON)
        # if  os.path.exists(TEMP_DIR):
        #     shutil.rmtree(TEMP_DIR_JSON)
        st.write("Uploaded Resumes:")
        for resume in uploaded_files:

            
            chat_llm_text = ChatOpenAI(model='gpt-3.5-turbo', temperature=0.0)

            st.write(resume.name)

            st.write("Parsed Resume:")

            text = process_file_with_dedoc(resume)
            text_f = extract_text_from_all_levels(text)
            if text:
                parsed_resume = generate_formatted_resume(text_f, chat_llm_text)

                st.text(parsed_resume)
                # Display extracted text on the app

            st.write("Parsed JSON Formated Resume:")
            
            parsed_json_resume = None

            while parsed_json_resume is None:
                # Execute your code to generate parsed_json_resume
                chat_llm_json = ChatOpenAI(model='gpt-3.5-turbo', temperature=0.4)

                parsed_json_resume = generate_json_structured_resume(text_f, chat_llm_json)
            
    
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

            career_trajectory = create_career_trajectory(parsed_json_resume['work'])

            st.write("Final Carrier  trajectory :")
            st.write(career_trajectory)

            st.write("Final ONET Parsed Formated Resume:")
            chat_llm_onet = ChatOpenAI(model='gpt-3.5-turbo', temperature=0.4)

            result = onet_job_title_to_onet_code(parsed_json_resume,chat_llm_onet)
            
            st.write(result)
            

            


def about():
    st.title("About This Application")
    st.write("""
    ResumeRevealer is developed by a team of passionate developers dedicated to revolutionizing the resume parsing process 
    and empowering users with comprehensive insights into their resumes. Our team comprises third year Artificial Intelligence and Machine Learning students of Symbiosis Institute of Technology, Pune.

    **Meet Our Team:**""")

    # Use columns layout option for horizontal arrangement
    col1, col2, col3 = st.columns(3)

    # Team Member 1: Jainil Patel
    with col1:
        st.image("Images/jainil.jpg", width=100)
        st.write("""
        <ul style="list-style-type: none; padding-left: 0;">
        <li>&#10148; <b>Name:</b> Jainil Patel</li>
        <li>&#10148; <b>Branch:</b> Artificial Intelligence and Machine Learning</li>
        <li>&#10148; <b>LinkedIn:</b> <a href="https://www.linkedin.com/in/jainil-patel-2857ab202/">Jainil Patel</a></li>
        <li>&#10148; <b>GitHub:</b> <a href="https://github.com/astro215">jainil23</a></li>
        <li>&#10148; <b>Email:</b> jainil.patel.btech2021@sitpune.edu.in</li>
        <li>&#10148; <b>Phone:</b> +91 7774036728</li>
        </ul>""", unsafe_allow_html=True)
    
    # Team Member 2: Divyam Kumar
    with col2:
        st.image("Images/prof.jpg", width=100)
        st.write("""
        <ul style="list-style-type: none; padding-left: 20px;">
        <li>&#10148; <b>Name:</b> Divyam Kumar</li>
        <li>&#10148; <b>Branch:</b> Artificial Intelligence and Machine Learning</li>
        <li>&#10148; <b>LinkedIn:</b> <a href="https://www.linkedin.com/in/divyam-kumar-2462a2264/">Divyam Kumar</a></li>
        <li>&#10148; <b>GitHub:</b> <a href="https://github.com/Divyam-kr">divyamkr100</a></li>
        <li>&#10148; <b>Email:</b> divyamkr100@gmail.com</li>
        <li>&#10148; <b>Phone:</b> +91 9430957531</li>
        </ul>""", unsafe_allow_html=True)
    
    # Team Member 3: Amitesh Patra
    with col3:
        st.image("Images/amitesh.jpg",width=100)
        st.write("""
        <ul style="list-style-type: none; padding-left: 0;">
            <li>&#10148; <b>Name:</b> Amitesh Patra</li>
            <li>&#10148; <b>Branch:</b> Artificial Intelligence and Machine Learning</li>
            <li>&#10148; <b>LinkedIn:</b> <a href="https://www.linkedin.com/in/amitesh30patra/">Amitesh Patra</a></li>
            <li>&#10148; <b>GitHub:</b> <a href="https://github.com/amitesh30">amitesh67</a></li>
            <li>&#10148; <b>Email:</b> amitesh.patra.btech2021@sitpune.edu.in</li>
            <li>&#10148; <b>Phone:</b> +91 9325409292</li>
        </ul>
    """, unsafe_allow_html=True)

    st.write("""
    If you have any questions, feedback, or suggestions, feel free to reach out to us. We are committed to continuously improving 
    ResumeRevealer to meet your resume parsing needs.

    Thank you for choosing ResumeRevealer!
    

    <br><br>

    Find us on [GitHub](https://github.com/astro215/ResumeRevealer) for the source code.
    """, unsafe_allow_html=True)
    
   


def main():
    st.title("""
<a href="https://github.com/astro215/ResumeRevealer" target="_blank" rel="noopener noreferrer">ResumeRevealer</a>
""")



    tab1, tab2, tab3 = st.tabs(["Our Project", "Model", "About us"])
    with tab1:
        home_page()
    with tab2:
        parser()
    with tab3:
        about()


if __name__ == "__main__":
    main()
