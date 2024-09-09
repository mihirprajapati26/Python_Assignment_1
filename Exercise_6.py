import random

# Generate a 3-digit code where each number is between 0 and 9
code_3_digits = [random.randint(0, 9) for _ in range(3)]
# Generate a 4-digit code where each number is between 1 and 6
code_4_digits = [random.randint(1, 6) for _ in range(4)]

# Print the generated codes
print(f"3-digit code: {''.join(map(str, code_3_digits))}")
print(f"4-digit code: {''.join(map(str, code_4_digits))}")