from docx import Document

doc = Document("data/job_description.docx")

jd_text = ""

for para in doc.paragraphs:
    jd_text += para.text + "\n"

print(jd_text)