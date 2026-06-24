from docx import Document

doc = Document("data/job_description.docx")

jd_text = ""

for para in doc.paragraphs:
    jd_text += para.text + "\n"

with open("data/job_description.txt", "w", encoding="utf-8") as file:
    file.write(jd_text)

print("JD saved successfully!")