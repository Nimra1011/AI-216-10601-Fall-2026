# Problem:
# Classify electricity usage as Low, Normal, or High.

# Inputs:
# Daily electricity usage values in kWh.

# Rules:
# Low: below 5 kWh
# Normal: 5 to 10 kWh
# High: above 10 kWh

# Repetition:
# Check every value in the daily usage list.

# Outputs:
# Count and percentage of Low, Normal, and High usage.

daily_usage_kwh = [3.2, 5.0, 7.5, 10.0, 12.4, 4.9, 10.1]

low_count = 0
normal_count = 0
high_count = 0

for usage in daily_usage_kwh:
    if usage < 5:
        low_count += 1
    elif usage <= 10:
        normal_count += 1
    else:
        high_count += 1

total_days = len(daily_usage_kwh)

low_percentage = (low_count / total_days) * 100
normal_percentage = (normal_count / total_days) * 100
high_percentage = (high_count / total_days) * 100

print(f"Low: {low_count} ({low_percentage:.2f}%)")
print(f"Normal: {normal_count} ({normal_percentage:.2f}%)")
print(f"High: {high_count} ({high_percentage:.2f}%)")