AFC_east = ['New England Patriots', 'Buffalo Bills', 'Miami Dolphins', 'New York Jets']

# print('kkk' in AFC_east)
# print('Buffalo Bills' in AFC_east)

# for team in AFC_east:
#     print(team)

# numbers = [2, 0, 1, 6, 9]

# for i in range(len(numbers)):
#     numbers[i] = numbers[i] * 2
    
# print(numbers)

# my_list = ['spam', 1, ['New England Patriots', \
#                        'Buffalo Bills', 'Miami Dolphins', \
#                        'New York Giants'], \
#            [1, 2, 3]]
# print(len(my_list))

# a = [1, 2, 3]
# b = [4, 5, 6]
# c = a + b
# print(c)
print([0] * 4)
print(['Tom Brady', 'Bill Belichick'] * 3)

t = ['a', 'b', 'c', 'd', 'e', 'f']
# print(t[5:6])
t[1:3] = ['x', 'y']
# print(t)
"""EX2"""
#append add an item to the end of list
a=[1,2,3,4,"a","b","c","z"]
a[len(a):7]=["x"]
# print(a)
a[len(a):8]=["x"]
# print(a)
a.append(("a","d"))

print(a)   

#extend Extend the list by appending all the items from the iterable (MORE LIKE COMBINE TWO LIST)

b=[1,2,3,4,"a","b","c","z"]
list.extend(b,["a","d"])
b.extend(["b","c","D"])
print(b)

C=[1,2,3,4,5,6,7,4,3,1]
C.sort()
C.sort(reverse=False)
C.sort(key=lambda x:x%2) 

def duo(x):
    return x%2
C.sort(key=duo) # similar with  C.sort(key=lambda x:x%2)
print(C)

t = ['a', 'b', 'c', 'd']
x = t.pop(1)
# pop modifies the list and returns 
# the element that was removed. 
print(x)
print(t)

t = ['a', 'b', 'c', 'd', 'e']
del t[1:3]
print(t)

a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0:2]
print(a)
del a[1:3]
print(a)

t = ['a', 'b', 'c', 'd']
x = t.pop(1)
# pop modifies the list and returns 
# the element that was removed. 
print(x)
print(t)

team = 'New England Patriots'
t = team.split()
print(t)

a = [1, 2, 3]
b = [1, 2, 3]
a is b #false

a = [1, 2, 3]
b = a
b is a #true