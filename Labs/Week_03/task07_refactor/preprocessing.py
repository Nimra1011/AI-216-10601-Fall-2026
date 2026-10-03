def clean_scores(scores):
    cleaned = []

    for score in scores:
        if 0 <= score <= 100:
            cleaned.append(score)

    return cleaned