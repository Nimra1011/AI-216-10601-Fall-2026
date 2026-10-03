scores = [78, 85, 92, 67, 88]
def calculate_average(scores):
    if scores==0:
        return None
    total = sum(scores) 
    return total/ len(scores)

def find_highest(scores):
    if scores==0:
        return None
    return max(scores)

def count_above_threshold(scores, threshold):
    count=0
    for score in scores:
        if score>=threshold:
            count += 1
    return count

def classify_average(average):
    if average is None:
        return "No valid data"
    if average>90:
        return ""
    elif average >= 70:
        return "Good"
    elif average >= 50:
        return "Satisfactory"
    else:
        return "Needs Improvement"

average = calculate_average(scores)
highest = find_highest(scores)
above_80 = count_above_threshold(scores, 80)
classification = classify_average(average)

print("Student Score Summary")
print("---------------------")
print("Scores:", scores)
print("Average:", average)
print("Highest:", highest)
print("Scores >= 80:", above_80)
print("Classification:", classification)
