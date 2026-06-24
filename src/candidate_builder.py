def build_candidate_text(candidate):

    profile = candidate["profile"]

    text = f"""
    CURRENT ROLE

    Title:
    {profile['current_title']}

    Headline:
    {profile['headline']}

    Summary:
    {profile['summary']}

    Years of Experience:
    {profile['years_of_experience']}
    """

    text += "\n\nCAREER HISTORY\n"

    for job in candidate["career_history"]:

        text += f"""
        Previous Role:
        {job['title']}

        Company:
        {job['company']}

        Description:
        {job['description']}
        """

    text += "\n\nSKILLS\n"

    for skill in candidate["skills"]:

        text += (
            f"{skill['name']} "
            f"({skill['proficiency']}, "
            f"{skill['duration_months']} months)\n"
        )

    return text