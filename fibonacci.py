#!/usr/bin/env python3

# Fibonacci Sequence Exercise

num = input("How many Fibonacci terms do you want? ")

while not isinstance(num, int) or num <= 0:
    print("Invalid input: please enter a positive integer.")
    num = input("How many Fibonacci terms do you want? ")

num = int(num)

term2 = 1
output = 1

for i in range(0, int(num)):
    if i == 0:
        output = 0
    elif i == 1 or i == 2:
        output = 1
    else:
        term1 = term2
        term2 = output

        output = term1 + term2
    print(output, end=' ')

# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.
