# Scenario A — List

evaluated_models = [
    "resnet50",
    "inception_v3",
    "vit_base"
]

print("A - Models:", evaluated_models)


# Scenario B — Tuple

image_size = (224, 224)

print("B - Image size:", image_size)


# Scenario C — Dictionary

model_config = {
    "name": "spam_classifier",
    "threshold": 0.80,
    "version": 2,
    "debug": True
}

print("C - Model configuration:", model_config)


# Scenario D — Set

class_labels = {
    "spam",
    "ham",
    "promotion"
}

print("D - Unique labels:", sorted(class_labels))


# Scenario E — List of dictionaries

prediction_records = [
    {
        "id": 1,
        "label": "spam",
        "confidence": 0.94
    },
    {
        "id": 2,
        "label": "ham",
        "confidence": 0.72
    }
]

print("E - Prediction records:", prediction_records)


# Scenario F — Set difference

allowed_labels = {
    "spam",
    "ham",
    "promotion"
}
received_labels = {
    "spam",
    "ham",
    "unknown"
}

unexpected_labels = received_labels - allowed_labels

print("F - Unexpected labels:", sorted(unexpected_labels))