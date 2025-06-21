import streamlit as st
from PyPDF2 import PdfReader
from fpdf import FPDF
import os
import re
from core import generate_cover_letter

st.set_page_config(page_title="AI Cover Letter Generator", page_icon="📝")
st.title("📝 AI Cover Letter Generator")

mode = st.radio("Resume Input Method:", ["Paste text", "Upload PDF"])
resume = ""
if mode == "Paste text":
    resume = st.text_area("Paste your resume content:")
else:
    file = st.file_uploader("Upload your resume (PDF only)", type="pdf")
    if file:
        reader = PdfReader(file)
        resume = "\n".join(page.extract_text() for page in reader.pages if page.extract_text())


job = st.text_area("Paste the job description:")


tone = st.selectbox("Select tone for the cover letter:", ["Professional", "Friendly", "Assertive", "Formal"])


if st.button("Generate Cover Letter"):
    if not resume or not job:
        st.error("Please provide both resume and job description.")
    else:
        cl = generate_cover_letter(resume, job, tone)
        st.subheader("✉️ Generated Cover Letter")
        st.write(cl)

        
        def sanitize(text):
            text = re.sub(r'[^\x00-\x7F]+', ' ', text)  
            text = re.sub(r'\s+', ' ', text)  
            return text.strip()

        cl_cleaned = sanitize(cl)

        
        pdf = FPDF()
        pdf.add_page()
        font_path = os.path.join("fonts", "DejaVuSans.ttf")
        pdf.add_font("DejaVu", "", font_path, uni=True)
        pdf.set_font("DejaVu", size=12)

        for line in cl_cleaned.split("\n"):
            pdf.multi_cell(0, 8, line)

        pdf_output = bytes(pdf.output(dest="S"))  

        st.download_button(
            label="📥 Download as PDF",
            data=pdf_output,
            file_name="cover_letter.pdf",
            mime="application/pdf"
        )