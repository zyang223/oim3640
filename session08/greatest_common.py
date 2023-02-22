#ex3
def gcd(a,b):
    """The greatest common divisor of two positive integers is the largest 
    integer that divides each of them without remainder. For example"""
    a=int(a)
    b=int(b)
    if b==0:
        return(a)
    return(gcd(b,a%b))
print(gcd(17,1