def calculate_experience_score(candidate):

    years = candidate["profile"]["years_of_experience"]

    if years < 3:
        return 0.2

    elif years < 5:
        return 0.7

    elif years <= 9:
        return 1.0

    elif years <= 12:
        return 0.8

    else:
        return 0.6