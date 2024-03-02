# %%
"""
## Install dedoc using pip

If you don't want to use docker for running the application, it's possible to run dedoc locally.
However, it isn't suitable for any operating system (`Ubuntu 20+` is recommended) and
there may be not enough machine's resources for its work.
You should have `python` (`python3.8`, `python3.9` are recommended) and `pip` installed.

### 1. Install necessary packages:
```shell
sudo apt-get install -y libreoffice djvulibre-bin unzip unrar
```

`libreoffice` and `djvulibre-bin` packages are used by converters (doc, odt to docx; xls, ods to xlsx; ppt, odp to pptx; djvu to pdf).
If you don't need converters, you can skip this step.
`unzip` and `unrar` packages are used in the process of extracting archives.

### 2. Install `Tesseract OCR 5` framework:
You can try any tutorial for this purpose or look [`here`](https://github.com/ispras/dedockerfiles/blob/master/dedoc_p3.9_base.Dockerfile)
to get the example of Tesseract installing for dedoc container or use next commands for building Tesseract OCR 5 from sources:

#### 2.1. Install compilers and libraries required by the Tesseract OCR:
```shell
sudo apt-get update
sudo apt-get install -y automake binutils-dev build-essential ca-certificates clang g++ g++-multilib gcc-multilib libcairo2 libffi-dev \
libgdk-pixbuf2.0-0 libglib2.0-dev libjpeg-dev libleptonica-dev libpango-1.0-0 libpango1.0-dev libpangocairo-1.0-0 libpng-dev libsm6 \
libtesseract-dev libtool libxext6 make pkg-config poppler-utils pstotext shared-mime-info software-properties-common swig zlib1g-dev
```
#### 2.2. Build Tesseract from sources:
```shell
sudo add-apt-repository -y ppa:alex-p/tesseract-ocr-devel
sudo apt-get update --allow-releaseinfo-change
sudo apt-get install -y tesseract-ocr tesseract-ocr-rus
git clone --depth 1 --branch 5.0.0-beta-20210916 https://github.com/tesseract-ocr/tesseract/
cd tesseract && ./autogen.sh && sudo ./configure && sudo make && sudo make install && sudo ldconfig && cd ..
export TESSDATA_PREFIX=/usr/share/tesseract-ocr/5/tessdata/
```


"""

# %%
from dedoc import DedocManager


# %%
manager = DedocManager()

# %%
"""
Dedoc is implemented in Python and works with semi-structured data formats (DOC/DOCX, ODT, XLS/XLSX, CSV, TXT, JSON) and none-structured data formats like images (PNG, JPG etc.), archives (ZIP, RAR etc.), PDF and HTML formats. Document structure extraction is fully automatic regardless of input data type. Metadata and text formatting are also extracted automatically.
"""

# %%
"""
We will be extracting .json files from the PDF , DOCX , HTML and Image files.
"""

# %%
# Utlity function to export  the json output
import json

def write_output_to_json(output, output_folder = None):
    """
    Write the given output data to a JSON file.

    Args:
    - output: The data to be converted to JSON format.
    """
    
    # extract the file name from the metadata and change the extension to .json
    filename = output['metadata']['file_name'].split('.')[0] + '.json'
    if output_folder:
        filename = os.path.join(output_folder, filename)
    else:
        filename = filename
    # Convert output to JSON format
    json_data = json.dumps(output, indent=4)

    # Write the JSON data to a file
    with open(filename, "w") as json_file:
        json_file.write(json_data)

    print(f"JSON data has been written to {filename}")




# %%
"""
### PDF
"""

# %%
pdf_file = "documents/pdf/1.pdf"
output = manager.parse(pdf_file)
pdf_output = output.to_api_schema().model_dump()


# %%
write_output_to_json(pdf_output)    


# %%
"""
### Making Generic function to extract the json from the files
"""

# %%
def process_file_with_dedoc(file_path):
    """
    Process the file using Dedoc and return the output data.

    Args:
    - file_path: The path of the file to be processed.

    Returns:
    - Output data if the file is processed successfully, None otherwise.
    """
    supported_formats = ['jpg', 'jpeg', 'png', 'docx', 'pdf', 'html' , 'doc']

    # Check if the file extension is supported
    file_extension = file_path.split('.')[-1].lower()
    if file_extension not in supported_formats:
        print(f"Cannot process file '{file_path}'. Unsupported file format.")
        return None

    # Process the file using Dedoc
    output = manager.parse(file_path)
    output_data = output.to_api_schema().model_dump()

    return output_data



# %%
# Example usage:
file_path = "documents/pdf/1.pdf"
output_data = process_file_with_dedoc(file_path)
if output_data:
    # Write the output to a JSON file
    write_output_to_json(output_data)

# %%
"""
### Making a function to process all files in a directory
"""

# %%
import os

def process_folder_with_dedoc(folder_path):
    """
    Process all files in the folder using Dedoc and write the output to JSON files.

    Args:
    - folder_path: The path of the folder containing the files to be processed.
    """
    # Create the output folder if it does not exist
    output_folder = os.path.join(folder_path, 'output_json')
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate over all files in the folder
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        print(file_path)

        # Process only files
        if os.path.isfile(file_path):
            
            print(f"Processing file '{file_path}'...")
            # Process the file using Dedoc
            output_data = process_file_with_dedoc(file_path)


            print(f"Processing file '{file_path}'...")
            if output_data:
                # Write the output to a JSON file in the output folder
                output_folder = os.path.join(folder_path, 'output_json')
                
                write_output_to_json(output_data , output_folder) 
                
                #change the directory to the parent folder
                



# %%
# Example usage:
folder_path = r"C:\Users\jaini\PycharmProjects\pythonProject3\files"
process_folder_with_dedoc(folder_path)


# %%
# Shot the files in the output folder
os.listdir(r'C:\Users\jaini\PycharmProjects\pythonProject3\files')

# %%
# Shot the files in the output folder
os.listdir(r'C:\Users\jaini\PycharmProjects\pythonProject3\files\output_json')

# %%
"""
## Extracting text from the JSON file
"""

# %%
import json

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

def extract_text_from_all_levels(json_file):
    """
    Extract text from all levels of subparagraphs in the JSON file.

    Args:
    - json_file: The path to the JSON file containing subparagraphs.

    Returns:
    - A string containing the text from all levels of subparagraphs.
    """
    with open(json_file, 'r') as f:
        data = json.load(f)
    text = ""
    if 'subparagraphs' in data['content']['structure']:
        subparagraphs = data['content']['structure']['subparagraphs']
        text += extract_text_from_subparagraphs(subparagraphs)
    return text




# %%
# Example usage:
json_file = r"C:\Users\jaini\PycharmProjects\pythonProject3\files\output_json\Jainil-Patel-FlowCV-Resume-20240228_page-0001.json"
pdf_text = extract_text_from_all_levels(json_file)
print(pdf_text)

# %%
