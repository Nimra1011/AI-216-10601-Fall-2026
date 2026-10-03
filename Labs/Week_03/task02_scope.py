#part A
score = 90
def show_score():
    score = 70
    print("Inside function:", score)
show_score()
print("Outside function:", score)

#part B
threshold = 0.85
def is_qualified(score):
    return score >= threshold

print("\nPart B — Qualification Check")
print(f"Score 0.90:, {is_qualified(0.25)}")
print("Score 0.80:", is_qualified(0.80))
print("Score 0.85:", is_qualified(0.85))