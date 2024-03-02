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
    Welcome to the CV Rankings application!
    
    This application is designed to help you analyze and rank CVs (resumes) based on their content. 
    You can upload CVs in various formats such as PDF, Word documents, HTML, and images. 
    Once uploaded, the application will process the CVs, extract relevant information, and provide insights 
    to help you make informed decisions.
    
    **Key Features:**
    
    - Upload CVs in multiple formats including PDF, Word documents, HTML, and images.
    - Extract and analyze information from the CVs.
    - Rank CVs based on specified criteria.
    - Visualize insights and statistics.
    
    **How to Use:**
    
    1. Click on the "Upload Files" button in the navigation menu to upload one or more CVs.
    2. Once uploaded, the application will process the CVs and display extracted information.
    3. Navigate to the "Rankings" section to view rankings based on specified criteria.
    4. Explore the visualizations and insights to make informed decisions.
    
    **About the Developer:**
    
    This application is developed by [Your Name]. 
    If you have any feedback, suggestions, or issues, feel free to reach out to [Your Email Address].
    
    Enjoy analyzing CVs with CV Rankings!
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
