# Part A — enumerate()

experiments = [
    0.81,
    0.86,
    0.79,
    0.91
]

for number, accuracy in enumerate(experiments, start=1):
    print(f"Experiment {number}: {accuracy}")

# Part B — zip()

predictions = [True, False, True, True]
actual = [True, False, False, True]

correct_count = 0

for predicted, actual_value in zip(predictions, actual):

    is_correct = predicted == actual_value

    if is_correct:
        correct_count += 1

    print(
        f"Predicted: {predicted} | "
        f"Actual: {actual_value} | "
        f"Correct: {is_correct}"
    )

accuracy = correct_count / len(actual)

print("Final accuracy:", accuracy)
print(f"Final accuracy percentage: {accuracy * 100:.2f}%")