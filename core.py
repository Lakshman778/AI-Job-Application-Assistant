import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain_core.prompts import PromptTemplate


load_dotenv()
OPENAI_KEY = os.getenv("OPENAI_API_KEY")
print("[DEBUG] .env loaded:", OPENAI_KEY is not None)

if not OPENAI_KEY:
    raise EnvironmentError("🔑 OPENAI_API_KEY not found! Check your .env file.")


SYSTEM_PROMPT = (
    "You are a professional resume assistant. "
    "Write a concise, engaging cover letter based on the inputs."
)

tpl = PromptTemplate.from_template(
    "{SYSTEM}\n\nResume Snippet:\n{resume}\n\nJob Description:\n{job}\n\nTone:\n{tone}\n\nCover Letter:"
)

llm = ChatOpenAI(
    model_name="mistralai/mistral-7b-instruct",
    temperature=0.3,
    openai_api_key=OPENAI_KEY,
    openai_api_base="https://openrouter.ai/api/v1"
)

chain = tpl | llm

def generate_cover_letter(resume: str, job: str, tone: str = "Professional") -> str:
    inputs = {
        "SYSTEM": SYSTEM_PROMPT,
        "resume": resume,
        "job": job,
        "tone": tone
    }
    try:
        response = chain.invoke(inputs)
        return str(response.content) if hasattr(response, 'content') else str(response)
    except Exception as e:
        return f"⚠️ Failed to generate cover letter: {str(e)}"
