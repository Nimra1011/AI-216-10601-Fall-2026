class ScoreAnalyzer:

    def __init__(self, scores):
        self.scores = scores

    def clean(self):
        self.scores = [
            score for score in self.scores
            if 0 <= score <= 100
        ]

    def average(self):
        if len(self.scores) == 0:
            return None

        return sum(self.scores) / len(self.scores)

    def count_above(self, threshold):
        count = 0

        for score in self.scores:
            if score >= threshold:
                count += 1

        return count

    def summary(self):
        if len(self.scores) == 0:
            return {
                "count": 0,
                "average": None,
                "highest": None,
                "lowest": None
            }

        return {
            "count": len(self.scores),
            "average": self.average(),
            "highest": max(self.scores),
            "lowest": min(self.scores)
        }


raw_scores = [78, -5, 110, 67, 90, 88]
analyzer = ScoreAnalyzer(raw_scores)

print("Before cleaning:")
print(analyzer.scores)

analyzer.clean()

print("\nAfter cleaning:")
print(analyzer.scores)

print("\nAverage:")
print(analyzer.average())

print("\nScores >= 80:")
print(analyzer.count_above(80))

print("\nSummary:")
print(analyzer.summary())