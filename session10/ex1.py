#Ex10 by Zide Yang Feb 21
#ex1
prefixes = 'JKLMNOPQ'
suffix = 'ack'
for letter in prefixes:
    if letter=="O"or letter=="Q": #nonempty string always considered true so be more specific
    # if letter in ['Q', 'O']:
        print(letter+"uack")
    else:
        print(letter + suffix)

#ex2
def count(word,letter):
    """Encapsulate this code in a function named count, and generalize it so that it accepts the string and the letter as arguments."""
    count = 0
    for i in word:
        if i==letter:
            count = count + 1
    return count

word="abcdefgaa"
letter='a'
print(count(word,letter))

#ex3 split,strip replace
name="zide ,is a student"
print(name)
print(name.split(","))

name2="   z  k   s   s    "
print(name2)
print(name2.strip())

name3="new england patriots"
name4=name3.replace("england","jersey") # need to assign the result in to a new variable
print(name3)
print(name4)

def in_both(word1, word2):
    for letter in word1:
        if letter in word2:
            print(letter)
word1="and"
word2="a and b and c"
in_both(word1,word2)

#ex 4
s="grouP"
def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False
print(any_lowercase1(s))
"""in the for loop if there is a c is all lower case return true, if there is an upper return false"""
        
def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'
print(any_lowercase2(s))
"""this one will always be true because "c" is lower"""

def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag
print(any_lowercase3(s))
""" if the last character character in the s will be lower case it will be trueit will check the """

def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag
print(any_lowercase4(s))
"""this will eventaully be true if there were any lower cases"""
def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True
"""if the c is not  all lower it will return false otherwise its true"""
print(any_lowercase5(s))


