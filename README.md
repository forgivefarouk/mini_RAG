# mini_RAG
Small demo for Retrieval Augmented Generation

## Requirements

- Python 3.8 or later

### Install python and Miniconda

1) Download and install Miniconda from [here](https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh)

2) Create Conda enviroment using the following command:
``` bash
$ conda create --name mini-rag python=3.8
```

3) Activate the Enviroment:
```bash
$ conda activate mini-rag
```

## Installation

### Install the required packages
```bash
$ pip install -r requirements.txt
```

### setup the enviroment variables
```bash
$ cp .env.example .env
```
Set your variables in the `.env` file. Like `OPENAI_API_KRY` value.

## Run the FastAPI server
```bash
$ uvicorn main:app --reload --host 0.0.0.0 --port 5000
```