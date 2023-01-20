#exercise 2 produced by Zide Yang in Jan 21 2023
#1. How many seconds are there in 42 minutes 42 seconds?
print("There are",42*60+42,"seconds")
time_sec=42*60+42
time_min=42+42/60

#2.How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile.
print("There are",10*1.61,"miles")
distance=10*1.61

#3. If you run a 10 kilometer race in 42 minutes 42 seconds, 
# what is your average pace (time per mile in minutes and seconds)? 
print("It takes",time_sec/distance,"seconds to finish a mile")
print("It takes",time_min/distance,"minutes to finish a mile")
# What is your average speed in miles per hour?
print("Average speed per hour is equal to",60/(time_min/distance),"miles per hour") 