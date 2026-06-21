import streamlit as st
from docx import Document

st.set_page_config(
    page_title="AI Resume Screening System",
    page_icon="📄"
)

st.title("📄 AI Resume Screening System")

skills_db = [
    "python",
    "sql",
    "power bi",
    "excel",
    "tableau",
    "machine learning",
    "deep learning",
    "pandas",
    "html",
    "css",
    "javascript",
    "flask",
    "streamlit",
    "mysql",
    "git",
    "github",
    "aws",
    "docker",
    "linux"
]

def extract_skills(text):

    found = []

    text = text.lower()

    for skill in skills_db:

        if skill in text:
            found.append(skill)

    return found

uploaded_resume = st.file_uploader(
    "Upload Resume",
    type=["docx"]
)

job_description = st.text_area(
    "Paste Job Description"
)

if st.button("Analyze Resume"):

    if uploaded_resume is not None and job_description:

        doc = Document(uploaded_resume)

        resume_text = ""

        for para in doc.paragraphs:
            resume_text += para.text + "\n"

        resume_skills = extract_skills(
            resume_text
        )

        jd_skills = extract_skills(
            job_description
        )

        matched_skills = list(
            set(resume_skills)
            &
            set(jd_skills)
        )

        missing_skills = list(
            set(jd_skills)
            -
            set(resume_skills)
        )

        if len(jd_skills) > 0:

            ats_score = (
                len(matched_skills)
                /
                len(jd_skills)
            ) * 100

        else:

            ats_score = 0

        st.success(
            "Resume Analysis Completed"
        )

        st.metric(
            "ATS Score",
            f"{round(ats_score,2)}%"
        )

        st.subheader(
            "Matched Skills"
        )

        st.write(
            matched_skills
        )

        st.subheader(
            "Missing Skills"
        )

        st.write(
            missing_skills
        )

    else:

        st.error(
            "Upload resume and enter job description"
        )
