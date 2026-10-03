# Input:
# Food expense, transport expense, other expense, daily budget

# Processing:
# Calculate total expense and remaining budget
# Check whether the student is within, exactly at, or over budget

# Output:
# Total expense, remaining budget, and budget status

food_expense = 450
transport_expense = 200
other_expense = 150
daily_budget = 1000

total_expense = food_expense + transport_expense + other_expense
remaining_budget = daily_budget - total_expense

print(f"Total expense: {total_expense}")
print(f"Remaining budget: {remaining_budget}")

if total_expense < daily_budget:
    print("Status: Within budget")
elif total_expense == daily_budget:
    print("Status: Exactly at budget")
else:
    print("Status: Over budget")
