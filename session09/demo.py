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


 