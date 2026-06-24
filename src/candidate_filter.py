RELEVANT_TITLES = {

    "Recommendation Systems Engineer",
    "Search Engineer",
    "NLP Engineer",
    "Applied ML Engineer",

    "ML Engineer",
    "AI Research Engineer",
    "Data Scientist",

    "Data Engineer",
    "Analytics Engineer",
    "Backend Engineer",

    "Software Engineer",
    "Full Stack Developer",

    "Cloud Engineer",
    "DevOps Engineer",

    "Java Developer"
}


def is_relevant_candidate(candidate):

    current_title = candidate["profile"]["current_title"]

    if current_title in RELEVANT_TITLES:
        return True

    for job in candidate["career_history"]:

        if job["title"] in RELEVANT_TITLES:
            return True

    return False