accuracies = [0.82, 0.91, 0.87, 0.78, 0.93, 0.85]
MIN_ACCURACY = 0.85

print("First:", accuracies[0])
print("Last:", accuracies[-1])

print("Middle four:", accuracies[1:5])

accuracies.append(0.89)
accuracies.extend([0.84, 0.90])

position = accuracies.index(0.78)
accuracies[position] = 0.80

print("Updated:", accuracies)

count = 0
for accuracy in accuracies:
    if accuracy >= MIN_ACCURACY:
        count += 1
print("Scores >= 0.85:", count)

print("Highest:", max(accuracies))
print("Lowest:", min(accuracies))


sorted_accuracies = sorted(accuracies, reverse=True)
print("Sorted (high to low):", sorted_accuracies)
print("Original order kept:", accuracies)