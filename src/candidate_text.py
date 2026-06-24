import json

with open("data/sample_candidates.json", "r", encoding="utf-8") as file:
    data = json.load(file)

candidate = data[0]

profile = candidate["profile"]

text = f"""
Title: {profile['current_title']}

Headline:
{profile['headline']}

Summary:
{profile['summary']}

Experience:
{profile['years_of_experience']} years

Skills:
"""

# Skills
for skill in candidate["skills"]:
    text += f"\n- {skill['name']} ({skill['proficiency']})"

# Career History
text += "\n\nCareer History:\n"

for job in candidate["career_history"]:
    text += f"""
Company: {job['company']}
Title: {job['title']}
Description: {job['description']}
"""

# Education
text += "\n\nEducation:\n"

for edu in candidate["education"]:
    text += f"""
Institution: {edu['institution']}
Degree: {edu['degree']}
Field: {edu['field_of_study']}
Tier: {edu['tier']}
"""

# Certifications
text += "\n\nCertifications:\n"

for cert in candidate["certifications"]:
    text += f"\n- {cert['name']}"

print(text)