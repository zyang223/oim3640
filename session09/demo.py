def sum1000():
    result=0
    for i in range (1,1001):
        #third arguement  range we jumped
        result+=i
    return result

print(sum1000())

def sum_up(n):
    result=0
    n=n+1
    for i in range(1,n):
        result+=i #means result= result+i
    return result

print(sum_up(1000))
"""when to use for loop
-when we know eactly how many times to repeat a certain code block"""
"""
When to use for loop:
    - when we know exactly how many times to repeat a certain code block
    - when we iterate over a collection of items
        - a string
        - a list
        - a tuple
        - a dictionary
When to use while loop:
    - if we only know when / what condition to stop, and we don't know how many times
"""

    