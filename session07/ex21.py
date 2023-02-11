""" factorial, define the """

def factorial(n):
    """1!=1
       2!=2*1
       return the factorial =n"""
    if n==1:
        print(f'{n}')
        return 1
    print(f'{n} *', end=' ')
    return n*factorial(n-1)
   

print(factorial(10))
