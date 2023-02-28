def avoids(word, forbidden):
    """
    returns True if the given word does not use any of the forbidden letters
    using if statement and in to return false for false value and true for true value
    
    We have modify the forbidden in char here for AEIOU IN THE LATER problem
    """
    for char in forbidden:
        if char in word:
            return False
        else:
            return True


# print(avoids('Babson', 'abcde'))
# print(avoids('College', 'e'))
# print(avoids('Boston', 'xyz'))

def find_words_no_vowels():
    """
    returns the percentage of the words that don't have vowel letters
    MODIFY avoid to char here so it can print out the out put aeious
    """
    forbidden= "a", "e", "i", "o", "u", "A", "E", "I", "O", "U"
    words_novowels = 0
    count = 0
    with open('data/words.txt') as f:
        for line in f:
            word = line.strip()
            count += 1
            if avoids(word,forbidden):
                words_novowels += 1
    print(count)
    print(words_novowels)
    return words_novowels / count

    

    


# perc_no_vowel = find_words_no_vowels()
# print(f'The percentage of the words without vowel letters is {perc_no_vowel*100:.2f}%.')


def uses_only(word, available):
    """
    takes a word and a string of letters, and that returns True if the word
    contains only letters in the string available.
    """
    for letter in word:
        if letter not in available:
            return False
    return True



# print(uses_only('Babson', 'aBbsonxyz'))
# print(uses_only('college', 'aBbsonxyz'))


def find_words_only_use_planet():
    """
     According to Dan Brown's The Da Vinci Code, 
     there are 62 other English words of varying lengths that could be formed using the letters in word "planets". 
     Can you find them out?
     Write a function named uses_only that takes a word and a string of letters, and that returns True if the word contains only letters in the string.
    """
    available = "planets"
    words_only_use_planet=0
    with open('data/words.txt') as f:
        for line in f:
            word = line.strip()
            if uses_only(word,available):
                words_only_use_planet += 1
    print(words_only_use_planet)
    return words_only_use_planet


print('Number of words that use only letters from "planets" is', find_words_only_use_planet())


def uses_all(word, required):
    """
    takes a word and a string of required letters, and that returns True if
    the word uses all the required letters at least once.
    """
    for char in word:
        if char not in required:
            return False
        else:
            return True


print(uses_all("a","apple"))
print(uses_all("b","apple"))


# please write test cases


def find_words_using_all_vowels():
    """
    return the number of the words that use all the vowel letters
    """
    f= open('data/words.txt')
    vowel_letter=0
    required="a","e","i","o","u"
    word=0
    for line in f:
        word=line.strip()
        if uses_all(word, required):
            vowel_letter+=1
        return vowel_letter
# print(find_words_using_all_vowels())




    


# print('The number of words that use all the vowels:', find_words_using_all_vowels())


def is_abecedarian(word):
    """
    returns True if the letters in a word appear in alphabetical order
    (double letters are ok).
    """
    previous=word[0]
    for c in word:
        if c<previous:
            return False
        previous=c
    return True


print(is_abecedarian('abs'))
# print(is_abecedarian('college'))


def find_abecedarian_words():
    """
    returns the number of abecedarian words
    """
    number=0
    f=open('data/words.txt')
    for line in f:
        word=line.strip()
        if is_abecedarian(word):
            number=number+1
    return number
    

        



print(find_abecedarian_words())


def is_abecedarian_using_recursion(word):
    """
    returns True if the letters in a word appear in alphabetical order
    (double letters are ok).
    """
    pass


# print(is_abecedarian_using_recursion('abcdef'))


def is_abecedarian_using_while(word):
    """
    returns True if the letters in a word appear in alphabetical order
    (double letters are ok).
    """
    pass


# print(is_abecedarian_using_while('abcdef'))
