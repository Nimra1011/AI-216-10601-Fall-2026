temperatures = [21.5, 29.0, 32.5, 18.0, 35.2, 27.8, 14.0]

below_normal_count = 0
normal_count = 0
high_count = 0

for temperature in temperatures:
    if temperature < 15:
        print(f"{temperature}°C: Below Normal")
        below_normal_count += 1

    elif temperature <= 30:
        print(f"{temperature}°C: Normal")
        normal_count += 1

    else:
        print(f"{temperature}°C: High")
        high_count += 1

print("\nSummary:")
print(f"Below Normal: {below_normal_count}")
print(f"Normal: {normal_count}")
print(f"High: {high_count}")