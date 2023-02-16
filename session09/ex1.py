# Ex9 Feb 16 2023 by zide yang
"""Calculate the sum of integers from 1 to 10.

Calculate the sum of integers from 1 to 1000. 

Calculate the sum of all the odd numbers from 1 to 1000. """

# sum  from 1 to 10
def sum10():
    """Calculate the sum of integers from 1 to 10"""
    result = 0
    for i in range(1, 11):
        result = result + i
    return result


# print(sum10())

# While
def whl10():
    """Calculate the sum of integers from 1 to 10use while"""
    Iteration = 0
    result = 0
    while Iteration < 11:
        for i in range(1, 11):
            result = result + 1
        Iteration = Iteration + 1
    return result


# print(whl10())


# sum from 1 to 1000
def sum1000():
    """Calculate the sum of integers from 1 to 1000."""
    result = 0
    for i in range(1, 1001):
        result += i
    return result


# print(sum1000())

# while
def whl1000():
    """Calculate the sum of integers from 1 to 10use while"""
    Iteration = 0
    result = 0
    while Iteration < 1001:
        result = result + Iteration
        Iteration = Iteration + 1
    return result


# print(whl1000())


# sum from 1 to 1000 Odd
def sum1000odd():
    """Calculate all the odd sum of integers from 1 to 1000."""
    result = 0
    for i in range(1, 1001, 2):
        result += i
    return result


# print(sum1000odd())


def whl1000odd():
    """Calculate all the odd sum of integers from 1 to 1000. using while"""
    iteration = 1
    result = 0
    while iteration < 1001:
        if (
            iteration % 2 == 1
        ):  # iteration not result here if result =0 it will eventually be false
            result = iteration + result
        iteration = iteration + 1
    return result


# print(whl1000odd())


# sum from 1 to 1000 even
def sum1000even():
    """Calculate all the even sum of integers from 1 to 1000."""
    result = 0
    for i in range(0, 1001, 2):
        result += i
    return result


print(sum1000even())


def whl1000even():
    """Calculate all the even sum of integers from 1 to 1000. using while"""
    iteration = 0
    result = 0
    while iteration < 1001:
        if iteration % 2 == 0:
            result = result + iteration
        iteration = iteration + 1
    return result


print(whl1000even())
