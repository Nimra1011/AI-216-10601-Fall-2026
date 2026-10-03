def calculate_average(scores):
    if len(scores) == 0:
        return None

    return sum(scores) / len(scores)


def is_passing(score, passing_score=50):
    return score >= passing_score


def count_above_threshold(scores, threshold):
    count = 0

    for score in scores:
        if score >= threshold:
            count += 1

    return count


if __name__ == "__main__":
    sample_scores = [72, 88, 45, 91, 67]

    print("Score Utilities Demo")
    print("Average:", calculate_average(sample_scores))
    print("First score passing:", is_passing(sample_scores[0]))
    print("Scores >= 80:", count_above_threshold(sample_scores, 80))