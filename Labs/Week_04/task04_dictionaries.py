model = {
    "name": "spam_classifier",
    "version": 2,
    "accuracy": 0.92,
    "threshold": 0.80,
    "status": "evaluated"
}

print("Model name:", model["name"])

model["accuracy"] = 0.94
model["owner"] = "AI-216 Team"

description = model.get("description", "No description available")
print("Description:", description)


print("\nModel Information:")
for key, value in model.items():
    print(f"{key}: {value}")


model["metrics"] = {
    "accuracy": 0.94,
    "precision": 0.91,
    "recall": 0.89
}
print("\nNested Metrics")
print("Precision:", model["metrics"]["precision"])
print("Recall:", model["metrics"]["recall"])