# exercise 06
import math


def quadratic(a, b, c):
    """check the variable"""
    if a == 0:
        print("value need to be corrected here")
    if (
        isinstance(a, int or float)
        and isinstance(b, int or float)
        and isinstance(c, int or float) == False
    ):
        print("Value need to be int or float")
    else:
        """solve the root through quadratic formula"""
        if (b**2 - 4 * a * c) < 0:
            """check the probelm can be solved or not"""
            print("it cannot be solved")
        else:
            """solve the probem through formula"""
            root1 = -b + math.sqrt((b**2 - 4 * a * c) / (2 * a))
            root2 = b + math.sqrt((b**2 - 4 * a * c) / (2 * a))
            return (root1, root2)


print(quadratic(5, 10, -10))
# how can I convert a tuple to a string or how can I round it here?
# I have used f format or rounding
