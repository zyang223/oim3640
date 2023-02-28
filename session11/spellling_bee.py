#feb 23 letter
"""write a program that use the letter below to found out as many word as possible
1. define a variable that doing owrd check contained the letter
2.import the dictonary and solving the problem using diconary.
3. use for loop to scan the dictonary
4.writing if condition to check if the word is meeting the coniditon or not
  """
word_list=("a","r","l","d","k","y","w")
def word_check(word):
    for letter in word:
        if letter not in word_list:
            return False
    print(word)
    return True
# Why is the code below not working properly? ( I am still quite confused.)
#         if letter not in word_list:
#             return False
#         else:
#             print(word)
#         return True
# # word_check("ldk")


def bubble():
    word_list=("a","r","l","d","k","y","w")
    count=0
    f=open('data/words.txt')
    for line in f:
        word=line.strip()
        if word_check(word):
            count=count+1
    return count

bubble()
            
        
