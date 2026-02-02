# Super Resume Generator 🦸

A humorous AI-powered resume generator built with Flask and Jinja2.

# PoC (Proof of Concept for hackathons?)
A proof of concept project that demonstrates:

Reading user input through HTML at index.html

App routing using Python Flask library. 

Calling POE API with poe.com api key, prompt engineering (differentiating system prompt and user prompt), post processing manipulation of bot raw response to obtain Json data type from string data type.

Uses Jinja2 like template injection library (docxtpl) to inject Json data into relevant fields within a docx template.

Returns generated docx file to user direct download.


## Features
- Hyperbolic resume generation
- Competitiveness slider (0–10)
- DOCX resume output
- Structured AI → template pipeline

## Setup

```bash
git clone https://github.com/v4L0r/resume-builder.git
cd resume-builder
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Please use your own API KEY for local testing. You need to set the environment variable POE_API_KEY (in .env, rename .env.example to .env) to access AI service on POE.
