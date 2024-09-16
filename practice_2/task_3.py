# -*- coding: utf-8 -*-
"""
Write a program to calculate the body mass index (BMI) of a person. The user must enter their height and weight, after which you use one of the formulas below to determine the index.
BMI = weight/height**2
"""
weight = input("Weight in kg: ")
height = input("Height in cm: ") # Let's assume it is in cantimeters

# code here

weight = float(weight)
height = float(height) / 100

if height == 0:
    print("Height can't be zero")
    exit(1)

bmi = weight / (height)**2
print(round(bmi, 2))
