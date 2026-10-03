age = 18
programming_score = 72
prerequisite_completed = True

print("Applicant Eligibility Check")

eligible = True

if age < 18:
    print("- Age requirement not met")
    eligible = False

if programming_score < 60:
    print("- Programming score requirement not met")
    eligible = False

if not prerequisite_completed:
    print("- Prerequisite course not completed")
    eligible = False

if eligible:
    print("Result: Eligible")
else:
    print("Result: Not eligible")