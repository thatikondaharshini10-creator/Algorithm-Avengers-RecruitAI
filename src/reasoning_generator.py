def generate_reasoning(candidate):

    profile = candidate["profile"]
    signals = candidate["redrob_signals"]

    title = profile["current_title"]
    years = profile["years_of_experience"]

    reasons = []

    # Experience

    reasons.append(
        f"{title} with {years} years of experience"
    )

    # Career history

    career_text = ""

    for job in candidate["career_history"]:

        career_text += (
            job["title"] + " " +
            job["description"] + " "
        ).lower()

    if any(word in career_text for word in
           ["recommendation", "ranking"]):

        reasons.append(
            "Direct experience building recommendation or ranking systems"
        )

    elif any(word in career_text for word in
             ["retrieval", "search"]):

        reasons.append(
            "Career history includes search or retrieval systems"
        )

    elif any(word in career_text for word in
             ["machine learning", "nlp", "ai"]):

        reasons.append(
            "Applied machine learning experience across previous roles"
        )

    elif any(word in career_text for word in
             ["analytics", "data pipeline"]):

        reasons.append(
            "Strong analytics and data engineering background"
        )

    # Skills

    skills = [
        skill["name"]
        for skill in candidate["skills"]
    ]

    retrieval_skills = []

    for skill in [
        "FAISS",
        "Pinecone",
        "Milvus",
        "Weaviate",
        "Information Retrieval",
        "Embeddings",
        "Sentence Transformers",
        "Elasticsearch",
        "BM25"
    ]:

        if skill in skills:
            retrieval_skills.append(skill)

    if retrieval_skills:

        reasons.append(
            "Relevant retrieval stack: " +
            ", ".join(retrieval_skills[:3])
        )

    # Behavioral Signals

    if signals["open_to_work_flag"]:

        reasons.append(
            "Currently open to work"
        )

    if signals["recruiter_response_rate"] > 0.70:

        reasons.append(
            "Very high recruiter response rate"
        )

    elif signals["recruiter_response_rate"] > 0.50:

        reasons.append(
            "Good recruiter engagement"
        )

    # Honest concern

    if years < 5:

        reasons.append(
            "Slightly below preferred experience range but demonstrates strong domain alignment"
        )

    elif signals["notice_period_days"] >= 90:

        reasons.append(
            "Long notice period may impact immediate availability"
        )

    return ". ".join(reasons)