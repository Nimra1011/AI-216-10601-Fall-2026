# Part A — List Comprehension

raw_scores = [78, -5, 92, 110, 67, 85]

valid_scores = [
    score
    for score in raw_scores
    if 0 <= score <= 100
]

normalized_scores = [
    score / 100
    for score in valid_scores
]

print("Valid:", valid_scores)
print("Normalized:", normalized_scores)


# Part B — Dictionary Comprehension

student_scores = {
    "Ali": 72,
    "Sara": 91,
    "Ahmed": 45,
    "Fatima": 88
}

pass_status = {
    student: score >= 50
    for student, score in student_scores.items()
}

print("Pass status:", pass_status)

# Part C — Set Comprehension

labels = [
    "Spam",
    "HAM",
    "spam",
    "Ham",
    "UNKNOWN"
]

normalized_labels = {
    label.lower()
    for label in labels
}

print("Labels:", sorted(normalized_labels))