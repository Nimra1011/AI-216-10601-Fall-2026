class ScoreAnalyzer:

    def __init__(self, scores):
        self.scores = scores

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

    def highest(self):
        if len(self.scores) == 0:
            return None

        return max(self.scores)

    def lowest(self):
        if len(self.scores) == 0:
            return None

        return min(self.scores)