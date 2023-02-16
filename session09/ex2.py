"""1. What is the value of the variable count that is printed out (at the print statement) on iteration 0? 
12

2. What is the value of the variable count that is printed out (at the print statement) on iteration 1?
24 

3. What is the value of the variable count that is printed out (at the print statement) on iteration 2? 
36

4. What is the value of the variable count that is printed out (at the print statement) on iteration 3? 
48

5. What is the value of the variable count that is printed out (at the print statement) on iteration 4?
60"""


iteration = 0
count = 0
while iteration < 5:
    # the variable 'letter' in the loop stands for every 
    # character, including spaces and commas!
    for letter in "hello, world": 
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count)) #"+" here is used for concatatenatation
    iteration += 1  

#2
"""
1. What is the value of the variable count that is printed out (at the print statement) on iteration 0? 
12
2. What is the value of the variable count that is printed out (at the print statement) on iteration 1? 
12
3. What is the value of the variable count that is printed out (at the print statement) on iteration 2? 
12
4. What is the value of the variable count that is printed out (at the print statement) on iteration 3? 
12
5. What is the value of the variable count that is printed out (at the print statement) on iteration 4?
12
"""

iteration = 0
while iteration < 5:
    count = 0
    for letter in "hello, world":
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 

#3
"""How many times will the print statement be executed? 3 
2. What is the largest value of the variable iteration that will be printed out (at the print statement)?  3
3. What is the largest value of the variable count that will be printed out (at the print statement)? 48
4. What is the smallest value of the variable count that will be printed out (at the print statement)? 12 """
iteration = 0
while iteration < 5:
    count = 0
    for letter in "hello, world":
        count += 1
        if iteration % 2 == 0:
            break
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1  

