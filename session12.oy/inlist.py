def make_word_list():
    """Reads lines from a file and builds a list using append.

    returns: list of strings
    """
    word_list = []
    fin = open("data/words.txt")
    for line in fin:
        word = line.strip()
        word_list.append(word)
    return word_list


def in_bisect(word_list, word):
    """Checks whether a word is in a list using bisection search.

    Precondition: the words in the list are sorted

    word_list: list of strings
    word: string

    Initialize two variables low and high to the first and last indices of the list, respectively.
Compute the index of the middle item of the list by taking the average of low and high and rounding down to the nearest integer.
If the middle item is equal to the target value, return True.
If the middle item is greater than the target value, update high to be the index of the middle item minus 1.
If the middle item is less than the target value, update low to be the index of the middle item plus 1.
If low is greater than high, the target value is not in the list, so return False.
    """
    
    word_list=make_word_list()
    word_list.sort()
    for line in word_list:
        line=word.strip()
        
    


def main():
    word_list = make_word_list()

    for word in ["aa", "alien", "allen", "zymurgy"]:
        print(word, "in list", in_bisect(word_list, word))


if __name__ == "__main__":
    main()
