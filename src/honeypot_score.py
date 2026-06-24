def calculate_honeypot_penalty(candidate):

    penalty = 0.0

    profile = candidate["profile"]

    years_exp = profile["years_of_experience"]

    total_months = 0

    for job in candidate["career_history"]:
        total_months += job.get(
            "duration_months",
            0
        )

    career_years = total_months / 12

    # Rule 1
    # Career duration far from claimed experience

    if abs(career_years - years_exp) > 5:
        penalty += 0.15

    # Rule 2
    # Expert skill with tiny duration

    for skill in candidate["skills"]:

        duration = skill.get(
            "duration_months",
            0
        )

        proficiency = skill.get(
            "proficiency",
            ""
        ).lower()

        if (
            proficiency == "expert"
            and duration < 6
        ):
            penalty += 0.10

    # Rule 3
    # Too many expert skills

    expert_count = 0

    for skill in candidate["skills"]:

        if (
            skill.get(
                "proficiency",
                ""
            ).lower()
            == "expert"
        ):
            expert_count += 1

    if expert_count > 8:
        penalty += 0.10

    # Rule 4
    # Experience less than skill durations suggest

    for skill in candidate["skills"]:

        duration_years = (
            skill.get(
                "duration_months",
                0
            ) / 12
        )

        if duration_years > years_exp + 3:
            penalty += 0.05
            break

    return min(penalty, 0.30)