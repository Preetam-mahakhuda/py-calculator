# -*- coding: utf-8 -*-
"""
Created on Wed Jul 16 16:09:39 2025

@author: ACER
"""

first_input = int(input("Enter a number")) #Taking value from the user
ope = (input("Enter an operation (+),(-), (*), (/)")) #Taking valid operation to perform
second_input = int(input("Enter an another number")) #Taking second value from the user

#declaring valid operations

addition = (first_input + second_input)
substraction = (first_input - second_input)
mltiplication = (first_input * second_input)
division = (first_input / second_input)

#if-else condition

if ope == '+':
    print(addition)
elif ope == '-':
    print(substraction)
elif ope == '*':
    print(mltiplication)
elif ope == '/':
    print(division)
else:
    print("Enter valid input & operations")