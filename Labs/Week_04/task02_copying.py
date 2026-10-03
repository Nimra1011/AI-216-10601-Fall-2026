import copy

original_scores = [70, 80, 90]
processed_scores = original_scores
processed_scores.append(100)

print("Part A — Aliasing")
print("Original:", original_scores)
print("Processed:", processed_scores)


original_scores = [70, 80, 90]
processed_scores = original_scores.copy()
processed_scores.append(100)

print("\nPart B — Shallow Copy")
print("Original:", original_scores)
print("Processed:", processed_scores)


raw_data = {
    "scores": [70, 80, 90]
}
shallow_data = raw_data.copy()
deep_data = copy.deepcopy(raw_data)

# Change nested list in shallow copy
shallow_data["scores"].append(100)

# Change nested list in deep copy
deep_data["scores"].append(110)

print("\nPart C — Shallow vs Deep Copy")
print("Raw data:", raw_data)
print("Shallow copy:", shallow_data)
print("Deep copy:", deep_data)