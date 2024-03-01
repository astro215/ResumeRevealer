import streamlit as st
import os
from dedoc import DedocManager

# Create a directory to store temporary files
TEMP_DIR = "temp_files"
if not os.path.exists(TEMP_DIR):
    os.makedirs(TEMP_DIR)


def process_file_with_dedoc(file):
    """
    Process the file using Dedoc and return the output data.

    Args:
    - file: The UploadedFile object to be processed.

    Returns:
    - Output data if the file is processed successfully, None otherwise.
    """

    manager = DedocManager()

    supported_formats = ['jpg', 'jpeg', 'png', 'docx', 'pdf', 'html', 'doc']

    print(f"Processing file '{file.name}'...")

    # Save the uploaded file to a temporary directory
    file_path = os.path.join(TEMP_DIR, file.name)
    with open(file_path, "wb") as f:
        f.write(file.getbuffer())

    # Extract file extension from the file name
    file_name, file_extension = os.path.splitext(file.name)
    file_extension = file_extension[1:].lower()  # Remove the leading dot and convert to lowercase

    # Check if the file extension is supported
    if file_extension not in supported_formats:
        print(f"Cannot process file '{file.name}'. Unsupported file format.")
        return None

    # Process the file using Dedoc
    output = manager.parse(file_path)
    output_data = output.to_api_schema().model_dump()

    # Remove the temporary file
    os.remove(file_path)

    return output_data


def extract_text_from_subparagraphs(subparagraphs):
    """
    Recursively extract text from subparagraphs.

    Args:
    - subparagraphs: A list of subparagraphs.

    Returns:
    - A string containing the text from all subparagraphs.
    """
    text = ""
    for subpara in subparagraphs:
        text += subpara['text'] + "\n"
        if 'subparagraphs' in subpara:
            text += extract_text_from_subparagraphs(subpara['subparagraphs'])
    return text


def extract_text_from_all_levels(data):
    """
    Extract text from all levels of subparagraphs in the JSON file.

    Args:
    - dedoc object: The Dedoc object containing the parsed data.

    Returns:
    - A string containing the text from all levels of subparagraphs.
    """
    text = ""

    if 'subparagraphs' in data['content']['structure']:
        subparagraphs = data['content']['structure']['subparagraphs']
        text += extract_text_from_subparagraphs(subparagraphs)
    return text


def main():
    st.title("CV Ranking")

    uploaded_files = st.file_uploader("Upload Files", type=["jpg", "jpeg", "png", "docx", "pdf", "html", "doc"],
                                      accept_multiple_files=True)

    if uploaded_files:
        st.write("Uploaded Resumes:")
        for resume in uploaded_files:
            st.write(resume.name)

            text = process_file_with_dedoc(resume)
            text_f = extract_text_from_all_levels(text)
            if text:
                st.text(text_f)
                # Display extracted text on the app


if __name__ == "__main__":
    main()
