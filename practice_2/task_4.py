# -*- coding: utf-8 -*-
"""
Develop a program that asks the user for an integer 4-digit number and calculates the sum of its constituent digits. For example, if the user enters the number 3141, the program should output the following result:
3 + 1 + 4 + 1 = 9

"""

number = input("Enter four-digit number: ")

try:
    number = int(number)
except ValueError:
    print("That wasn't a number")
    exit(1)

if not (1000 <= number <= 9999):
    print("That wasn't a four-digit number")
    exit(1)

result = sum(number // 10**i % 10 for i in range(0, 4))
print(result)
