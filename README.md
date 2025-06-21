# AI-Powered Job Application Assistant

This is a Python-based AI-powered web application that helps job seekers generate tailored, professional cover letters based on their resume and job description using LLMs (via OpenRouter / LangChain).

---

## Features

* Upload your resume (PDF or text)
* Paste the job description
* Choose a target tone (e.g., Professional, Friendly)
* AI-generated personalized cover letter using LangChain + OpenRouter
* Export the result as a downloadable PDF (Unicode-safe)

---

## Tech Stack

* Frontend: Streamlit
* Backend: Python (LangChain, OpenRouter API)
* PDF Export: fpdf
* Resume Parsing: PyPDF2

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone {The repository link}
cd {file path}
```

### 2. Create virtual environment 
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your API key to `.env`

```
OPENAI_API_KEY=#Use your API key that you generated
#Use this link to generate one {it only takes api form this website:https://openrouter.ai/settings/keys}
```

### 5. Add DejaVuSans font 

Download `DejaVuSans.ttf` from the official DejaVu repository and place it in:

```
AI_Job_Application_Assistant/fonts/DejaVuSans.ttf
```

### 6. Run the app

```bash
streamlit run app.py
```

---

## Project Structure

```
├── app.py               # Main Streamlit application
├── core.py              # LangChain logic and AI integration
├── .env                 # Environment file with API key
├── fonts/
│   └── DejaVuSans.ttf   # Unicode-safe font
├── requirements.txt     # All dependencies
└── README.md            # This file
```

---

## Example Use Case

1. Upload your resume PDF or paste resume text
2. Paste a job description from LinkedIn or company site
3. Select tone: "Professional"
4. Click "Generate Cover Letter"
5. Download your polished, job-specific cover letter as a PDF

---

## API Notes

* This app uses OpenRouter-compatible API keys
* You can also modify the code to use OpenAI directly or local models via Ollama/Groq

---

## Credits

Built using Streamlit, LangChain, and OpenRouter

---

## Future Ideas

* Add multi-model support (Claude, Gemini, GPT-4)
* Auto-scan skills from resume and match to JD
* Save user profiles and history
