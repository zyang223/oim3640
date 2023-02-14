"""
Question 1:

Write a function that prompts the user for a weight on earth and prints the equivalent weight on the moon (16.5%)

Weight on Moon = weight on Earth * 0.165

Notice:
1. Please write pseudo-code before coding the function.
2. Your function should include docstring.
3. Write your own test code, i.e. call the function.
"""

def transfer(e):
    """Write a function that prompts the user for a weight on earth and prints the equivalent weight on the moon (16.5%)
    Weight on Moon = weight on Earth * 0.165
    pseudocode
    1. enter the value,2 transfer the value do the multiply,3 return the value
    """

    m=e*0.165
    return m

print(transfer(10))

#print(transfer(10))

"""
Question 2:

Write a function that takes two arguments - 1. weight on earth (float), 2. planet (str) - and returns the equivalent weight on that planet. We assume Moon is a planet although it is not.

Weight on Moon = weight on Earth * 0.165
Weight on Mars = weight on Earth * 0.378
Weight on Venus = weight on Earth * 0.904

Notice:
1. You don't have to write pseudo-code before coding the function. However if pseudocode is provided, you will get partial credits even if you Python code is not working.
2. Your function should include docstring.
3. Write your own test code, i.e. call the function.
"""
def transfer2(e,weight):
    if e=="moon":
        m=weight*0.165
        return m
    elif e=="mars":
        m=weight *0.378
        return m
    elif e=="venus":
        m=weight*0.904
        return m

print(transfer2("mars",10))
