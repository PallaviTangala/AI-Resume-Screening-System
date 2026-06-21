import streamlit as st

st.set_page_config(
    page_title="AI Resume Screening System",
    page_icon="📄"
)

st.title("📄 AI Resume Screening System")

st.markdown("""
Upload your resume and compare it with a job description.
""")

uploaded_resume = st.file_uploader(
    "Upload Resume",
    type=["pdf","docx"]
)

job_description = st.text_area(
    "Paste Job Description"
)

if st.button("Analyze Resume"):

    st.success("Resume Analysis Completed")

    st.metric(
        "ATS Score",
        "85%"
    )

    st.write("### Matched Skills")

    st.write("""
    Python
    SQL
    Power BI
    """)

    st.write("### Missing Skills")

    st.write("""
    Tableau
    Excel
    """)