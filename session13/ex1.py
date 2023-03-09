# exercise 1 written by Zide Yang
"""
Rewrite function histogram using get. You should be able to eliminate the if statement.

Use function histogram to count the frequency of each word in your favorite song.

"""


def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d


print(histogram("bookkeeper"))
starboy = "I'm tryna put you in the worst mood, ah P1 cleaner than your church shoes, ah Milli point two just to hurt you, ah All red Lamb' just to tease you, ah None of these toys on lease too, ah Made your whole year in a week too, yah Main bitch out your league too, ah Side bitch out of your league too, ah House so empty, need a centerpiece 20 racks a table cut from ebony Cut that ivory into skinny pieces Then she clean it with her face man I love my baby You talking money, need a hearing aid You talking bout me, I don't see the shade Switch up my style, I take any lane I switch up my cup, I kill any pain"
print(histogram(starboy))

# 2 Play with _fibonaccicounted.py.


def fibonacci(n):
    """
    an intuitive version of fibonacci
    """
    global number_fib_calls
    if "number_fib_calls" not in globals():
        number_fib_calls = 0
    number_fib_calls += 1
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


known = {0: 1, 1: 1}
known = {0: 1, 1: 1}  # CODE from with _fibonaccicounted.py


def fib_efficient(n):
    """
    a "memori version of fibonacci
    """
    global number_fib_calls  # what does global mean here? Variables in __main__ are sometimes called global because they can be accessed from any function.
    if "number_fib_calls" not in globals():
        number_fib_calls = 0
    number_fib_calls += 1
    if n in known:
        return known[n]
    else:
        ans = fib_efficient(n - 1) + fib_efficient(n - 2)
        known[n] = ans
        return ans


def main():
    fib_args = 8
    global number_fib_calls
    number_fib_calls = 0
    print(f"The {fib_args}th Fibonacci number is {fibonacci(fib_args)}.")
    print("# of function calls:", number_fib_calls)

    number_fib_calls = 0
    print(f"The {fib_args}th Fibonacci number is {fib_efficient(fib_args)}.")
    print("# of function calls:", number_fib_calls)


if __name__ == "__main__":
    main()
print(fib_efficient(5))

# Exercise 03
# Find out another global variable that is used inside functions. What is the difference between this global variable and known? Why?

z = False


def magic_true():
    global z
    z = True
    print(z)
    return z


magic_true()

zide = ["z", "i", "d", "e"]


def magic_zide():
    global zide
    zide = ["e", "i", "d", "z"]
    print(zide)
    return zide


magic_zide()

# exercise04
"""Write a function that reads the words in words.txt and stores them as keys in a dictionary. 
It doesn’t matter what the values are. 
Then you can use the in operator as a fast way to check whether a string is in the dictionary."""


def check_words(n):
    """check whether a string is in the dictionary"""
    fin = open("data/words.txt")
    word_dict = {}  # initialize an empty dictionary
    for line in fin:
        word = line.strip()
        word_dict[word] = None
    if n in word_dict:
        print(f"The word {n} is in the dictionary.")
    else:
        print(f"The word {n} is not in the dictionary.")


n = "dog"
check_words(n)

# Write a function named has_duplicates that takes a list as a parameter and returns True if there is any object that appears more than once in the list.
def has_duplicate(d):
    """takes a list as a parameter and returns True if there is any object that appears more than once"""
    count = 0
    list = {}
    for n in d:
        if n not in list:
            count = 1
        else:
            count = count + 1
            if count >= 2:
                return True
    return False


d = ["a", "b", "a"]
print(has_duplicate(d))
