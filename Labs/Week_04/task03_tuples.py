image_size = (224, 224)
model_result = ("baseline_cnn", 0.91)

width, height = image_size
model_name, accuracy = model_result

print("Image size:", width, "x", height)
print(f"Model: {model_name} | Accuracy: {accuracy}")


def summarize_scores(scores):
    if len(scores) == 0:
        return None

    minimum = min(scores)
    maximum = max(scores)
    average = sum(scores) / len(scores)

    return minimum, maximum, average


scores = [72, 88, 91, 67]

result = summarize_scores(scores)

if result is not None:
    minimum, maximum, average = result

    print(f"Minimum: {minimum} | Maximum: {maximum} | Average: {average}")

empty_result = summarize_scores([])

print("Empty:", empty_result)


input_models = {
    (224, 224): "resnet50",
    (299, 299): "inception_v3",
    (384, 384): "vit_base"
}

print("Model for 299x299:", input_models[(299, 299)])


try:
    invalid_registry = {
        [224, 224]: "resnet50"
    }

except TypeError as error:
    print("TypeError:", error)