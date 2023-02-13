# 2
def factorial(n):
    """1!=1
    2!=2*1
    return the factorial =n"""
    if n == 1:
        print(f"{n}")
        return 1
    print(f"{n}*", end=" ")
    return n * factorial(n - 1)


# print(factorial(3))

# 2.1 fibonacci.py
def fibonacci(n):
    """1,1,2,3,5,8, (n-1)+(n-2)"""
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


for i in range(1, 10):
    print(fibonacci(i))
