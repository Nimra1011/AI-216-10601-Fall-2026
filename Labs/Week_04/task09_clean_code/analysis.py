def count_by_label(predictions):
    label_counts = {}

    for prediction in predictions:
        label = prediction["label"]

        if label not in label_counts:
            label_counts[label] = 0

        label_counts[label] += 1

    return label_counts


def get_unique_labels(predictions):
    labels = set()

    for prediction in predictions:
        labels.add(prediction["label"])

    return labels


def find_unexpected_labels(predictions, allowed_labels):
    actual_labels = get_unique_labels(predictions)

    return actual_labels - allowed_labels


def average_confidence(predictions):
    if len(predictions) == 0:
        return None

    total = 0

    for prediction in predictions:
        total += prediction["confidence"]

    return total / len(predictions)


def top_predictions(predictions, count):
    sorted_predictions = sorted(
        predictions,
        key=lambda prediction: prediction["confidence"],
        reverse=True
    )

    return sorted_predictions[:count]