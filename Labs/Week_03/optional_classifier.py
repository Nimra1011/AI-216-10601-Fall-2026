class ThresholdClassifier:

    def __init__(self, threshold):
        self.threshold = threshold

    def predict_one(self, value):
        return value >= self.threshold

    def predict(self, values):
        predictions = []

        for value in values:
            predictions.append(self.predict_one(value))

        return predictions

    def accuracy(self, values, true_labels):
        if len(values) != len(true_labels):
            raise ValueError(
                "Values and true labels must have the same length."
            )

        predictions = self.predict(values)

        correct = 0

        for prediction, true_label in zip(predictions, true_labels):
            if prediction == true_label:
                correct += 1

        return correct / len(true_labels)


# Create model
model = ThresholdClassifier(threshold=60)

values = [45, 70, 80, 30]
labels = [False, True, True, False]

print("Predictions:")
print(model.predict(values))

print("Accuracy:")
print(model.accuracy(values, labels))