# Ask the user to enter mass in talents, pounds, and lots
talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))

# Convert the inputs to grams
# 1 talent = 20 pounds, 1 pound = 32 lots, 1 lot = 13.3 grams
total_grams = (talents * 20 * 32 * 13.3) + (pounds * 32 * 13.3) + (lots * 13.3)

# Convert total grams to kilograms and grams
kilograms = int(total_grams // 1000)
grams = total_grams % 1000

# Print the result
print(f"The weight in modern units: {kilograms} kilograms and {grams:.2f} grams.")