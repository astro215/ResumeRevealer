# ResumeRevealer: Advanced Resume Parsing Challenge
<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="">
    <img src="https://www.mined2024.tech/logo.png" alt="Logo" width="500" height="350">
  </a>

  <p align="center">
    ResumeRevealer: Advanced Resume Parsing 
    <br />
<!--     <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a> -->
    <br />
    <br />
    <a href="https://resume-revealer.streamlit.app/">View Demo</a>
    
<!--     <a href="https://github.com/othneildrew/Best-README-Template/issues">Report Bug</a> -->
    
<!--     <a href="https://github.com/othneildrew/Best-README-Template/issues">Request Feature</a> -->
  </p>
</div>

## Primary Challenge
The primary challenge of the ResumeRevealer project is to develop a comprehensive resume parser capable of extracting detailed information from resumes in various formats, including PDF, JPG, HTML, DOC, etc. The parser should accurately classify text into distinct sections such as education, work experience, and skills. Additionally, it should sequence these sections based on dates wherever available.

## Standardization Challenge
In addition to parsing resumes, the ResumeRevealer project aims to enhance standardization by aligning different job titles and occupations against the O-NET database. This process ensures a consistent taxonomy across parsed resumes, making it easier to analyze and compare candidate profiles.

## Skill Extraction Challenge
An advanced feature of the ResumeRevealer project involves implementing a skill extraction mechanism. This feature mines detailed skills and competencies from project descriptions and position roles within the resume, highlighting the candidate's specific abilities and expertise. Abstractive skill extraction, if achieved, would be considered a bonus feature.


## ResumeRevealer: Advanced Resume Parsing Challenge - Primary Challenge

This repository contains the code for the ResumeRevealer project, which aims to develop a comprehensive resume parser that can extract detailed information from resumes in various formats such as PDF, JPG, HTML, DOC, etc. The parser accurately classifies text into distinct sections like education, work experience, skills, and sequences them based on dates, where available.

ResumeRevealer utilizes [Dedoc](https://github.com/ispras/dedoc/tree/master) for document processing.

> Dedoc is an open universal system for converting documents to a unified output format. It extracts a document’s logical structure and content, its tables, text formatting and metadata. The document’s content is represented as a tree storing headings and lists of any level. Dedoc can be integrated in a document contents and structure analysis system as a separate module.


## <div align="center">Environments</div>

<div align="center">
  <a href="">
    <img src="Images/Screenshot 2024-03-02 120118.png" width="100%" /></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="5%" alt="" />
  
</div>

## 📝 Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Functionality](#functionality)
4. [Limitations](#limitations)
5. [Contributing](#contributing)
6. [Acknowledgements](#Acknowledgements)


## <div align="center">Environments</div>

Get started in seconds with our verified environments.

<div align="center">
  <a href="">
    <img src="https://raw.githubusercontent.com/ispras/dedoc/master/dedoc_logo.png" width="10%" /></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="5%" alt="" />
  <a href="">
    <img src="https://python.langchain.com/img/brand/wordmark-dark.png" width="40%" /></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="5%" alt="" />
   <a href="">
     <img src="https://avatars.githubusercontent.com/u/45109972?s=200&v=4" width="10%" /></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="5%" alt="" />
   <a href="">
     <img src="https://avatars.githubusercontent.com/u/14957082?s=200&v=4" width="10%" /></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="5%" alt="" />
<!--    <a href="">
     <img src="https://github.com/ultralytics/yolov5/releases/download/v1.0/logo-aws-small.png" width="10%" /></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="5%" alt="" /> -->
  <a href="">
    <img src="https://raw.githubusercontent.com/github/explore/d8574c7bce27faa27fb879bca56dfe351ee66efd/topics/pycharm/pycharm.png" width="10%" /></a>
</div>

## <div align="center">Installation</div>

If you don't want to use docker for running the application, it's possible to run dedoc locally.
However, it isn't suitable for any operating system (`Ubuntu 20+` is recommended) and
there may be not enough machine's resources for its work.
You should have `python` (`python3.9`, `python3.10` are recommended) and `pip` installed.

## Getting Started with the Awesome Streamlit Repository

### Prerequisites

- An Operating System like Windows, OsX or Linux
- A working [Python](https://www.python.org/) installation.
  - We recommend using 64bit Python 3.8
- a Shell
  - We recommend [Git Bash](https://git-scm.com/downloads) for Windows 8.1
  - We recommend [wsl](https://en.wikipedia.org/wiki/Windows_Subsystem_for_Linux) for For Windows 10 ,11 or earlier.
- an Editor
  - We recommend [VS Code](https://code.visualstudio.com/) (Preferred) or [PyCharm](https://www.jetbrains.com/pycharm/).
- The [Git cli](https://git-scm.com/downloads)

### <div align="center">Environment Installation</div>

Clone the repo

```bash
https://github.com/astro215/ResumeRevealer.git
```

cd into the project root folder

```bash
cd streamlit-Directory
```

#### Create virtual environment

##### via python

Then you should create a virtual environment named .venv

```bash
python -m venv .venv
```

and activate the environment.

On Linux, OsX or in a Windows Git Bash terminal it's

```bash
source .venv/Scripts/activate
```

or alternatively

```bash
source .venv/bin/activate
```

In a Windows terminal it's

```bash
.venv/Scripts/activate.bat
```

##### or via anaconda

Create virtual environment named awesome-streamlit

```bash
conda create -n awesome-streamlit python
```

and activate environment.

```bash
activate atreamlit
```

If you are on windows you need to install some things required by GeoPandas by following [these instructions](https://geoffboeing.com/2014/09/using-geopandas-windows/).

Then you should install the local requirements

```bash
pip install -r requirements.txt
```

### Build and run the Application Locally

```bash
streamlit run app.py
```

### 2. Install necessary packages :
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

<!-- ACKNOWLEDGMENTS -->

## 🎉 Acknowledgements <a name = "acknowledgement"></a>

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

* [Dedoc](https://github.com/ispras/dedoc)
* [Langchain-LLM-Model](https://github.com/langchain-ai/langchain)
* [Open-ai](https://github.com/openai)
  




## ✍️ Authors <a name = "authors"></a>

- [@Jainil Patel](https://github.com/astro215) - Contributor
- [@Divyam Kumar](https://github.com/Divyam-kr) - Contributor
- [@Amitesh Patra](https://github.com/amitesh30) - Contributor

<p align="right">(<a href="#readme-top">back to top</a>)</p>
