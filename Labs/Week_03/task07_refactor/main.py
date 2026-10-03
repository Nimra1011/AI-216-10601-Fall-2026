from preprocessing import clean_scores
from analyzer import ScoreAnalyzer

scores = [78, -5, 92, 110, 67, 88]
cleaned_scores = clean_scores(scores)
analyzer = ScoreAnalyzer(cleaned_scores)

print("Score Analysis")
print("--------------")

print("Raw scores:", scores)
print("Cleaned scores:", cleaned_scores)
print("Average:", analyzer.average())
print("Qualified (>= 70):", analyzer.count_above(70))
print("Highest:", analyzer.highest())
print("Lowest:", analyzer.lowest())