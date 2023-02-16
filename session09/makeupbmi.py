# Makeup for the last assignment of part two in exercise 1
# By Zide Feb 16 2023
"""Write a function, calculate_bmi that takes two parameters,
 weight and height, to return BMI value. Write another function, 
 get_bmi_category that prompts user to input values for weight and height,
  converts them to floats, uses calculate_bmi to calculate BMI value, and returns the corresponding BMI category."""


def calculate_bmi():
    """Write a function, calculate_bmi that takes two parameters,
    weight and height, to return BMI value."""
    weight = float(input("please enter your weight in kg"))
    height = float(input("please enter your heightin in m"))
    BMI = weight / height**2
    print(BMI)
    return BMI


def get_bmi_category():
    """get_bmi_category that prompts user to input values for weight and heightand returns the corresponding BMI category"""
    BMI = calculate_bmi()
    if BMI <= 18.5:
        print("You are under weight")
    elif BMI <= 24.9:
        print("you are normal weight")
    elif BMI <= 29.9:
        print("you are overweight")
    else:
        print("you are obesity")


get_bmi_category()
