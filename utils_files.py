import os
import json

# Create temporary directories if they don't exist
TEMP_DIR_TEXT = "temp_files_text"
TEMP_DIR_JSON = "temp_files_json"
if not os.path.exists(TEMP_DIR_TEXT):
    os.makedirs(TEMP_DIR_TEXT)
if not os.path.exists(TEMP_DIR_JSON):
    os.makedirs(TEMP_DIR_JSON)


def save_parsed_resume_as_text(parsed_resume, filename):
    filename_without_extension = os.path.splitext(filename)[0]
    text_file_path = os.path.join(TEMP_DIR_TEXT, f"{filename_without_extension}.txt")
    with open(text_file_path, 'w') as text_file:
        text_file.write(parsed_resume)
    return text_file_path

def save_parsed_resume_as_json(parsed_json_resume, filename):
    filename_without_extension = os.path.splitext(filename)[0]
    json_file_path = os.path.join(TEMP_DIR_JSON, f"{filename_without_extension}.json")
    with open(json_file_path, 'w') as json_file:
        json.dump(parsed_json_resume, json_file, indent=4)
    return json_file_path