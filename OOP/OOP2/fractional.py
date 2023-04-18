#Design a class to represent a fractional number
class fractional:





# Attributes Numerator and denomonitor
# methods:
# __init__tp create an object/ instance of this type 
    
    

    def __init__(self,a,b):
        if b==0:
            raise ZeroDivisionError("denominintor cannot be zero")
        self.numerator=a
        self.denomintor=b
        import math
        gcd=math.gcd(a,b)
        if gcd>1:
            a //=gcd
            b //=gcd
        
    def __str__(self):
        """The human readble form"""
        return f"{self.numerator:^3}\n----\n{self.denomintor:^3}" # :^3 center it 
    def __add__(self,other:"fractional"):
        "overload the "+"operaro"
        new_numerator=self.numerator*other.denomintor + self.denomintor*other.numerator
        new_denomnitor=self.denomintor*other.denomintor
        return fractional(new_numerator,new_denomnitor)
    def __eq__(self,other:"fractional"):
        """return true if the value of two numbers are the same"""
        return self.numerator==other.numerator and self.denomintor==other.denomintor
    
    def __contains__(self,number):
        return number==self.numerator or number==self.denomintor

frac_1=fractional(3,2)
print(frac_1)

frac_2=fractional(1,1)
print(frac_2)

result=frac_1+frac_2
print(result)

frac_3=fractional(6,4)
print(frac_3)
print(frac_1==frac_3)

print(2 in frec_1)