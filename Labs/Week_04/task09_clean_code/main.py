from preprocessing import (
    filter_by_confidence,
    split_complete_records,
    normalize_labels
)

from analysis import (
    count_by_label,
    get_unique_labels,
    find_unexpected_labels,
    average_confidence,
    top_predictions
)

# Constants

MIN_CONFIDENCE = 0.80

ALLOWED_LABELS = {
    "spam",
    "ham",
    "promotion"
}

REQUIRED_FIELDS = (
    "id",
    "label",
    "confidence"
)

TOP_COUNT = 3

# Initial prediction records

initial_predictions = [
    {"id": 1, "label": "spam", "confidence": 0.94},
    {"id": 2, "label": "ham", "confidence": 0.72},
    {"id": 3, "label": "promotion", "confidence": 0.41},
    {"id": 4, "label": "spam", "confidence": 0.89},
    {"id": 5, "label": "ham", "confidence": 0.97},
    {"id": 6, "label": "promotion", "confidence": 0.83},
    {"id": 7, "label": "ham", "confidence": 0.58}
]

# New batch

new_batch = [
    {"id": 8, "label": "Spam", "confidence": 0.91},
    {"id": 9, "label": "ham"},
    {"id": 10, "label": "unknown", "confidence": 0.86},
    {"id": 11, "label": " HAM ", "confidence": 0.66}
]

# Combine both batches

all_predictions = initial_predictions + new_batch

# Remove incomplete records

complete_records, incomplete_records = split_complete_records(
    all_predictions,
    REQUIRED_FIELDS
)
skipped_ids = [
    prediction["id"]
    for prediction in incomplete_records
]


# Normalize labels

cleaned_predictions = normalize_labels(complete_records)

# Build summary

high_confidence_predictions = filter_by_confidence(
    cleaned_predictions,
    MIN_CONFIDENCE
)

label_counts = count_by_label(cleaned_predictions)

unique_labels = sorted(
    get_unique_labels(cleaned_predictions)
)

unexpected_labels = sorted(
    find_unexpected_labels(
        cleaned_predictions,
        ALLOWED_LABELS
    )
)

average = average_confidence(cleaned_predictions)

top_records = top_predictions(
    cleaned_predictions,
    TOP_COUNT
)

top_ids = [
    prediction["id"]
    for prediction in top_records
]


summary = {
    "total_records": len(all_predictions),
    "valid_records": len(cleaned_predictions),
    "skipped_ids": skipped_ids,
    "labels": unique_labels,
    "label_counts": label_counts,
    "high_confidence_count": len(high_confidence_predictions),
    "unexpected_labels": unexpected_labels,
    "average_confidence": average,
    "top_ids": top_ids
}

# Display report

print("=== Prediction Report ===")

print("Total records:", summary["total_records"])

print("Valid records:", summary["valid_records"])

print(
    "Skipped (missing data):",
    summary["skipped_ids"]
)

print("Labels:", summary["labels"])

print(
    "Label counts:",
    summary["label_counts"]
)

print(
    f"High confidence (>= {MIN_CONFIDENCE}):",
    summary["high_confidence_count"]
)

print(
    "Unexpected labels:",
    summary["unexpected_labels"]
)

print(
    f"Average confidence: {summary['average_confidence']:.3f}"
)

print(
    "Top 3 by confidence:",
    summary["top_ids"]
)

# Prove raw data was not changed

print(
    "Original label of record 8:",
    new_batch[0]["label"]
)