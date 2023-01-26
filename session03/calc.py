# homework exercise 03 written by Zide Yang on Jan 25 2023

# Q1
# What is the volume of a sphere with radius 5?
r = 5
pi = 3.1415926
v = (4 / 3) * pi * r * r * r
print("The volume of a sphere with radiu 5 equal to", f"{v:5.2f}.")
""
# Q2
#  Suppose the cover price of a book is $24.95, but bookstores get a 40% discount.
# Shipping costs $3 for the first copy and 75 cents for each additional copy.
# What is the total wholesale cost for 60 copies?

n = 60
Price = 24.95
discount = 0.4
shipcost = (n - 1) * 0.75 + 3
# 0.4 equal to 40% discount,
# I inted to write a if then statement here to define the value of ship cost,
# but the knowledge I learened could not support with it.
# INTENDED CODE : if n=1 then shipcost =3,elif n>1 then shipcost=3+(n-1)*0.75,else shipcost=0
wholesale = n * Price * (1 - discount) + shipcost
print("the wholesale cost for 60 copies equal to", f"{wholesale:.5}$.")


# Question 3
# If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile),
# then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again,
# what time do I get home for breakfast?
easypace = 8 * 60 + 15
tempo = 7 * 60 + 12
m_easypace = 2
m_tempo = 3
Time = m_easypace * easypace + tempo * m_tempo
Time_min = Time / 60
print(
    "6:52+",
    f"{Time_min:.2f}",
    "minutes means Expected  go back to home get breakfast at 7:30",
)
#################################################################
Current_Time = 6 * 60 + 52
sum_timeinmin = Time_min + Current_Time
Expected_Timehour = sum_timeinmin / 60
Expected_Timemin = (Expected_Timehour - 7) * 60

print(f"{Expected_Timehour:1.0f}", ":", f"{Expected_Timemin:3.0f}")

# I would like to calculate the total minutes together and
# then show the hours and minutes seperatedly, my problem here is I could not make 7.50 turn in to 7:30
#  But I cannot keep 7.5 round up to 8 here


# Question 4
# If my average grade rises from 82 to 89. What is the percentage of the increase?
# Format the result as xx.x%. Keep one figure after decimal point
old_grade = 82
new_grade = 89
change = (new_grade - old_grade) / old_grade * 100
str(change) + "%"
print("the percentage of increase equal to", f"{change:.1f}%.")
