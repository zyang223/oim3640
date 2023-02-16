def mysqrt(a):
    """Copy the loop from above and encapsulate it in a function called mysqrt that takes a as a param
    eter, chooses a reasonable value of x, and returns an estimate of the square root of a."""
    x=a/3
    epsilon=0.00000001
    while True:
        print(x)
        y = (x + a/x) / 2
        if abs(y-x) <epsilon:
            break
        x = y
    return y

# print(mysqrt(16))

import math
def test_square_root():
    """write a function named test_square_root that prints a table to evaluate the differences among results"""
    print("a","mysqrt(a)","math.sqrt(a)","diff") # need help of how to make a table
    for a in range(1,11 ):
        diff=abs(mysqrt(a)-math.sqrt(a))
        print(a,mysqrt(a),math.sqrt(a),diff)  # same here
    # print(f"{a}\t{mysqrt:(a.10f)}\t{math.sqrt:(a.10f)}\t{diff:.10f}") format error

test_square_root()