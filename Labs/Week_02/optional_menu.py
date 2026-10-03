def calculate_percentage(obtained, total):
    if total == 0:
        return 0

    return (obtained / total) * 100


def is_passing(score, passing_score):
    return score >= passing_score


choice = ""

while choice != "3":
    print("\n--- Menu ---")
    print("1. Check pass/fail")
    print("2. Calculate percentage")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        score = float(input("Enter your score: "))
        passing_score = float(input("Enter passing score: "))

        result = is_passing(score, passing_score)

        if result:
            print("Result: Pass")
        else:
            print("Result: Fail")

    elif choice == "2":
        obtained = float(input("Enter obtained marks: "))
        total = float(input("Enter total marks: "))

        percentage = calculate_percentage(obtained, total)

        print(f"Percentage: {percentage:.2f}%")

    elif choice == "3":
        print("Program ended.")

    else:
        print("Invalid choice. Please select 1, 2, or 3.")