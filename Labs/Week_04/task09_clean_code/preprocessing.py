def filter_by_confidence(predictions, min_confidence):
    return [
        prediction
        for prediction in predictions
        if prediction["confidence"] >= min_confidence
    ]


def split_complete_records(predictions, required_fields):
    complete_records = []
    incomplete_records = []

    for prediction in predictions:
        if all(field in prediction for field in required_fields):
            complete_records.append(prediction)
        else:
            incomplete_records.append(prediction)

    return complete_records, incomplete_records


def normalize_labels(predictions):
    normalized_predictions = []

    for prediction in predictions:
        copied_prediction = prediction.copy()

        copied_prediction["label"] = (
            copied_prediction["label"].strip().lower()
        )

        normalized_predictions.append(copied_prediction)

    return normalized_predictions