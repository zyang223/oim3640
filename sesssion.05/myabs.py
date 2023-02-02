# exercise 03
def my_abs_3(n):
    """print the absolute value of any value"""
    if n < 0:
        print(-n)
    else:
        print(n)


a = -20
my_abs_3(a)
my_abs_3(-5555)
print(my_abs_3(a))
# exercise 04##################################
def my_abs_4(n):
    """return the absolute value of any value"""
    if n < 0:
        return -n
    else:
        return n


print(my_abs_4(-10))
my_abs_4(a)
print(my_abs_4(a))

import math

print(my_abs_4(math.sqrt(10)))
print(my_abs_3(math.sqrt(10)))

##################
n = -30


def my_abs_5(n):
    """add a condition to check that if the number is int or float or not"""
    if isinstance(n, int or float) == False:
        print("We need a int or a float number here")
        return n
    else:
        if n < 0:
            return -n
        else:
            return n
    # Could I use the function my_abs_4 here instead ?


print(my_abs_5("camal"))
print(my_abs_5(n))
print(my_abs_5(-60))

