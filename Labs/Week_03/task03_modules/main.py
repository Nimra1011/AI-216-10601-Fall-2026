from score_utils import (
    calculate_average,
    is_passing,
    count_above_threshold
)


scores = [72, 88, 45, 91, 67]

average = calculate_average(scores)
first_score_passing = is_passing(scores[0])
scores_above_80 = count_above_threshold(scores, 80)

print("Student Score Analysis")
print("----------------------")
print("Scores:", scores)
print("Average:", average)
print("First score passing:", first_score_passing)
print("Scores >= 80:", scores_above_80)