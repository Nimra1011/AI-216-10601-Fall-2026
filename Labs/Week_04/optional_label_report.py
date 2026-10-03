from collections import defaultdict, Counter


cleaned_predictions = [
    {"id": 1, "label": "spam", "confidence": 0.94},
    {"id": 2, "label": "ham", "confidence": 0.72},
    {"id": 3, "label": "promotion", "confidence": 0.41},
    {"id": 4, "label": "spam", "confidence": 0.89},
    {"id": 5, "label": "ham", "confidence": 0.97},
    {"id": 6, "label": "promotion", "confidence": 0.83},
    {"id": 7, "label": "ham", "confidence": 0.58},
    {"id": 8, "label": "spam", "confidence": 0.91},
    {"id": 10, "label": "unknown", "confidence": 0.86},
    {"id": 11, "label": "ham", "confidence": 0.66}
]


# Version 1 — Plain Dictionary


confidence_by_label = {}

for prediction in cleaned_predictions:

    label = prediction["label"]
    confidence = prediction["confidence"]

    if label not in confidence_by_label:
        confidence_by_label[label] = []

    confidence_by_label[label].append(confidence)


print("Plain Dictionary Version")
print("label       count  avg_conf  max_conf")

for label in sorted(confidence_by_label):

    confidences = confidence_by_label[label]

    count = len(confidences)
    average = sum(confidences) / count
    highest = max(confidences)

    print(
        f"{label:<11} "
        f"{count:<6} "
        f"{average:.3f}     "
        f"{highest:.2f}"
    )

# Version 2 — defaultdict

confidence_by_label_default = defaultdict(list)

for prediction in cleaned_predictions:

    confidence_by_label_default[
        prediction["label"]
    ].append(
        prediction["confidence"]
    )


print("\nDefaultdict Version")
print("label       count  avg_conf  max_conf")

for label in sorted(confidence_by_label_default):

    confidences = confidence_by_label_default[label]

    count = len(confidences)
    average = sum(confidences) / count
    highest = max(confidences)

    print(
        f"{label:<11} "
        f"{count:<6} "
        f"{average:.3f}     "
        f"{highest:.2f}"
    )


# ==================================================
# Counter — Most Common Label
# ==================================================

label_counter = Counter(
    prediction["label"]
    for prediction in cleaned_predictions
)

most_common_label = label_counter.most_common(1)[0]

print("\nMost common label:", most_common_label)