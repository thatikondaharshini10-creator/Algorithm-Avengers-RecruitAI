import json

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

print("Loading model...")
model = SentenceTransformer("all-MiniLM-L6-v2")

print("Loading candidates...")

# Load candidates
with open("data/sample_candidates.json", "r", encoding="utf-8") as file:
    candidates = json.load(file)

# Load JD text
with open("data/job_description.txt", "r", encoding="utf-8") as file:
    jd_text = file.read()

# Generate JD embedding once
jd_embedding = model.encode(jd_text)

results = []

for candidate in candidates:

    profile = candidate["profile"]

    # --------------------
    # Skills
    # --------------------
    skills_text = ""

    for skill in candidate["skills"]:
        skills_text += f"{skill['name']} ({skill['proficiency']}), "

    # --------------------
    # Career History
    # --------------------
    career_text = ""

    for job in candidate["career_history"]:
        career_text += f"""
        Company: {job['company']}
        Title: {job['title']}
        Description: {job['description']}
        """

    # --------------------
    # Education
    # --------------------
    education_text = ""

    for edu in candidate["education"]:
        education_text += f"""
        Degree: {edu['degree']}
        Field: {edu['field_of_study']}
        Institution: {edu['institution']}
        Tier: {edu['tier']}
        """

    # --------------------
    # Certifications
    # --------------------
    certifications_text = ""

    for cert in candidate["certifications"]:
        certifications_text += f"{cert.get('name', '')}, "

    # --------------------
    # Candidate Text
    # --------------------
    candidate_text = f"""
    Title: {profile['current_title']}

    Headline:
    {profile['headline']}

    Summary:
    {profile['summary']}

    Experience:
    {profile['years_of_experience']} years

    Skills:
    {skills_text}

    Career History:
    {career_text}

    Education:
    {education_text}

    Certifications:
    {certifications_text}
    """

    # Generate embedding
    candidate_embedding = model.encode(candidate_text)

    # Similarity score
    score = cosine_similarity(
        [jd_embedding],
        [candidate_embedding]
    )[0][0]

    results.append(
        (
            candidate["candidate_id"],
            score
        )
    )

# Sort descending
results.sort(
    key=lambda x: x[1],
    reverse=True
)

print("\nTOP 10 CANDIDATES\n")

for candidate_id, score in results[:10]:
    print(candidate_id, "->", round(score, 4))