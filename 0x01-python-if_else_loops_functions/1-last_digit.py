#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

# Get the last digit of the number
last_digit = abs(number) % 10

if number < 0:
    last_digit = -last_digit

# Determine the appropriate message based on the last digit
if last_digit > 5:
    message = "and is greater than 5"
elif last_digit == 0:
    message = "and is 0"
else:
    message = "and is less than 6 and not 0"

# Print the output
print(f"Last digit of {number} is {last_digit} {message}")
