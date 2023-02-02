# homework exercise 04 written by Zide Yang on Jan 27 2023
# Question 1
# 1) a=3 a+2          a=5 integer
# 2) a=a+1.0 a,        A   not defined (float)
# 3)a=3, b ,           b not defined
# 4)a=3, a==5.0                 false  boolean
# 5)b=10, c=b>9 c=10            true  boolean
# 6)5/2==5/2.0                  true


# Question 2
# 1) 3.0-1.0!=5.0-3.0      False
# 2) 3>4 or (2>3 and 9>10)      False
# 3) 4>5 or 3<4 and 9>8      True
# 4)not(4>3 and 100>6 )  False


# Question 3
import time

print(time.time())
# using days calculator from internet Today is Jan 28 2023 18:32
sec = int(time.time())
sec_inday = 24 * 60 * 60
hour_inday = 24
minutes_inhours = 60 * 60
days_fromepoch = sec / sec_inday
print("Today is", int(days_fromepoch), "days from epoch.")
mid_sec = int(days_fromepoch) * sec_inday
current_timeinsec = sec - mid_sec
cur_hour = current_timeinsec / minutes_inhours
cur_minutes = current_timeinsec / 60 - int(cur_hour) * 60
cur_seconds = (cur_minutes - int(cur_minutes)) * 60
print(
    "The current time is:",
    int(cur_hour),
    ":",
    int(cur_minutes),
    ":",
    f"{cur_seconds:.0f}",
)

# Question 4
# Create a program that prompts the user to input two integers, then calculates
#  prints the sum, difference, product, quotient,
# and exponentiation of the integers in the format of mathematical equations.
# Use f-string to format the output nicely. Example output:

a = float(input())
b = float(input())
print("The number you chose is", a, b)
sum = a + b
print(a, "+", b, "=", sum)
differences = a - b
print(f"{a} - {b}={differences:.2f}")
multiple = a * b
print(f"{a} * {b}= {multiple:.2f}")
quotient = a / b
print(f"{a} / {b}= {quotient:.2f}")
exponentiation = a**b
print(f"{a} ^ {b}={exponentiation:.2f}")
