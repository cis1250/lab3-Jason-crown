#!/usr/bin/env python3
# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.

# I made sure to keep asking until the user gives a positive whole number
while True:
    user_input = input("How many terms of the Fibonacci sequence would you like? ")
    if user_input.isdigit() and int(user_input) > 0:
        n = int(user_input)
        break
    else:
        print("Please enter a positive integer.") # I made a case if they don't use follow the domain I set

# Make the sequence
a = 0
b = 1
nums = []  # store the numbers as we go to make it easier to get later

for _ in range(n):
    nums.append(a)
    a, b = b, a + b  # move to the next pair

# Print them on one line separated by spaces
print(" ".join(str(x) for x in nums))
