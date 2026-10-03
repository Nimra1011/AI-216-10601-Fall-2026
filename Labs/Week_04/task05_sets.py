training_labels = [
    "spam",
    "ham",
    "spam",
    "promotion",
    "ham"
]

test_labels = [
    "spam",
    "ham",
    "unknown",
    "promotion"
]

training_set = set(training_labels)
test_set = set(test_labels)


print("Unique training labels:", sorted(training_set))

in_both = training_set & test_set
print("In both:", sorted(in_both))


only_in_test = test_set - training_set
print("Only in test:", sorted(only_in_test))


in_either = training_set | test_set
print("In either:", sorted(in_either))