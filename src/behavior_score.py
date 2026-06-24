def calculate_behavior_score(candidate):

    signals = candidate["redrob_signals"]

    score = 0

    # Open To Work
    if signals["open_to_work_flag"]:
        score += 30

    # Recruiter Response Rate
    response_rate = signals["recruiter_response_rate"]

    if response_rate > 0:
        score += response_rate * 30

    # Interview Completion Rate
    interview_rate = signals["interview_completion_rate"]

    if interview_rate > 0:
        score += interview_rate * 20

    # GitHub Activity
    github_score = signals["github_activity_score"]

    if github_score > 0:
        score += min(github_score, 20)

    # Normalize to 0–1
    return score / 100