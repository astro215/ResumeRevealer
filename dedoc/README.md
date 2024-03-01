# ResumeRevealer: Advanced Resume Parsing Challenge - Primary Challenge

This repository contains the code for the ResumeRevealer project, which aims to develop a comprehensive resume parser that can extract detailed information from resumes in various formats such as PDF, JPG, HTML, DOC, etc. The parser accurately classifies text into distinct sections like education, work experience, skills, and sequences them based on dates, where available.

ResumeRevealer utilizes [Dedoc](https://github.com/ispras/dedoc/tree/master) for document processing.

> Dedoc is an open universal system for converting documents to a unified output format. It extracts a document’s logical structure and content, its tables, text formatting and metadata. The document’s content is represented as a tree storing headings and lists of any level. Dedoc can be integrated in a document contents and structure analysis system as a separate module.

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Functionality](#functionality)
4. [Limitations](#limitations)
5. [Contributing](#contributing)
6. [License](#license)

## Installation <a name="Installation"></a>

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



## Usage <a name="usage"></a>

To use the ResumeRevealer parser, follow these steps:

1. Import the necessary libraries and create a DedocManager instance:
```python
from dedoc import DedocManager

manager = DedocManager()
```
2. Process a single file using the `process_file_with_dedoc` function:
```python
file_path = "path/to/your/file.extension"
output_data = process_file_with_dedoc(file_path)
if output_data:
    write_output_to_json(output_data)
```
3. Process all files in a directory using the `process_folder_with_dedoc` function:
```python
folder_path = "path/to/your/folder"
process_folder_with_dedoc(folder_path)
```

## Functionality <a name="functionality"></a>

The ResumeRevealer parser performs the following tasks:

1. Extracts structured data from resumes in various formats (PDF, JPG, HTML, DOC, etc.).
2. Classifies text into distinct sections such as education, work experience, and skills.
3. Sequences sections based on dates, where available.

## Limitations <a name="limitations"></a>

Please note that the current implementation has the following limitations:

1. The parser might not work on all operating systems (Ubuntu 20+ is recommended).
2. The parser may require significant machine resources for optimal performance.
3. The accuracy of text classification and date sequencing depends on the quality and formatting of the input resumes.

## Contributing <a name="contributing"></a>

Contributions to the ResumeRevealer project are welcome! To contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make the necessary changes and commit them.
4. Submit a pull request detailing your changes.

