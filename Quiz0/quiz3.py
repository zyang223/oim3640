"""
You've been hired as a content moderator for a social media platform, and your task is to identify and flag inappropriate language used by users. Your team has received a tip that some users are using coded language to bypass the platform's filters and post inappropriate content.

After analyzing the data, you've discovered a text file, "drunkard_words.txt", which contains a list of words that are likely being used to disguise inappropriate language. You can access and download this text file via link (https://gist.githubusercontent.com/lzblack/cd9d6187dfdc4fbd363e0fbc538275a5/raw/43dbeda41c0c7ef1223e1ac2e64ef87aad4c054d/drunkard_words.txt). 

Your job is to create a function, `identify_inappropriate_words`, that identifies the inappropriate words and return the complete list of these words.

A word is considered as "inappropriate" if it meets all the following three conditions:
- The word contains at least three letters from "covid".
- The word contains at least one letter (any letter) that occurs twice in a row.
- The word starts and ends with the same letter (any letter).

Requirements:
- You can create helper function(s) to be used in the major function, `identify_inappropriate_words`.
- You should write docstring(s) to the function(s) you create, describing its purpose, input parameters, and output.
- To test your function(s), you should add test code that calls the function(s) you create.
- You can write comments and pseudo-code appropriately in order to improve the readability and understandability of your code.
- Use meaningful function and variable names.
"""

def identify_inappropriate_words():
    f = open('data/words.txt')
    for line in f:
        word=line.strip()
        if covid(word) and twice(word)and startwithend(word)==True:
            print (f"{word} is inappropriate")
            return True
        else:
            return False
            



def covid(word):
    count=0
    list=["c","o","v","i","d"]
    for letter in word:
        if list in word:     #different need to be updated
            count=count+1  
        if count >3:
            return True
        return False

            

def twice(word):
    """Returns True if any element appears more than once in a sequence.
    s: string or list
    returns: bool
    """
    # make a copy of t to avoid modifying the parameter
    t = list(word)
    t.sort()

    # check for adjacent elements that are equal
    for i in range(len(t) - 1):
        if t[i] == t[i + 1]:
            return True
    return False

def startwithend(word):
    t=list[word]
    start=t[0]
    end=t[-1]
    if start!=end:
        return False
    return True


