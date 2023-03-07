def nested_sum(t):
    """Computes the total of all numbers in a list of lists.

    t: list of list of numbers

    returns: number

    Expected output:
    # >>> 
    t=[[1, 2], [3], [4, 5, 6]]
    >>> 
    21
    """
    a=sum(sum(sublist) for sublist in t)
    print(a)
    return a 
t=[[1, 2], [3], [4, 5, 6]]
nested_sum(t)


def cumsum(t):
    """Computes the cumulative sum of the numbers in t.

    t: list of numbers

    returns: list of numbers

    Expected output:
    >>> t = [1, 2, 3]
    >>> cumsum(t)
    [1, 3, 6]
    """
    total=0
    result=[]
    for n in (t):
        total=total+n
        result.append(total)
    return result
t = [1, 2, 3]
print(cumsum(t))



def middle(t):
    """Returns all but the first and last elements of t.

    t: list

    returns: new list

    Expected output:
    >>> t = [1, 2, 3, 4]
    >>> middle(t)
    [2, 3]
    """
    result=t[1:-1]



def chop(t):
    """Removes the first and last elements of t.

    t: list

    returns: None

    Expected output:
    >>> t = [1, 2, 3, 4]
    >>> chop(t)
    >>> t
    [2, 3]
    return"""
    t.pop(0)
    t.pop(-1)
    print(t)
    return t



def is_sorted(t):
    """Checks whether a list is sorted.

    t: list

    returns: boolean

    Expected output:
    >>> is_sorted([1, 2, 2])
    True
    >>> is_sorted(['b', 'a'])
    False
    """
    a=t.copy()
    a.sort()
    if a!=t:
        return False
    return True

1, 2, 2
print(is_sorted(t))



def is_anagram(word1, word2):
    """Checks whether two words are anagrams

    Two words are anagrams if you can rearrange the letters from one to
    spell the other.

    word1: string or list
    word2: string or list

    returns: boolean

    Expected output:
    >>> is_anagram('stop', 'pots')
    True
    >>> is_anagram('different', 'letters')
    False
    >>> is_anagram([1, 2, 2], [2, 1, 2])
    Ture
    """# From CHATGPT I feel I still not understand the logic here
    # Class note sorted(name)=sorted(word)
    count1={}
    count2={}
    for letter in word1:
        count1[letter]=count1.get(letter,0)+1
    for letter in word2:
        count2[letter]=count2.get(letter,0)+1
    if count1==count2:
        return True
    return False
print(is_anagram('different', 'letters'))

def has_duplicates(s):
    """Returns True if any element appears more than once in a sequence.

    s: string or list

    returns: bool

    output:
    >>> print(has_duplicates('cba'))
    False
    >>> print(has_duplicates('abba'))
    True
    """
    result={}
    for letter in s:
        if letter in result:
            return True
        result[letter]=1
    return False


def has_adjacent_duplicates(s):
    """Returns True if there are two same adjacent elements.

    s: string or list

    returns: bool
    

    output:
    >>> print(has_adjacent_duplicates('cba'))
    False
    >>> print(has_adjacent_duplicates('abca'))
    Flase
    >>> print(has_adjacent_duplicates('abbc'))
    True
    """
    for i in range(len(s)-1): #len(s)-1 returns the index of the last element in the sequence s from chat gpt
        if s[i]==s[i+1]:
            return True
        return False


def main():
    t = [[1, 2], [3], [4, 5, 6]]
    print(nested_sum(t))

    t = [1, 2, 3]
    print(cumsum(t))

    t = [1, 2, 3, 4]
    print(middle(t))
    chop(t)
    print(t)

    print(is_sorted([1, 2, 2]))
    print(is_sorted(['b', 'a']))

    print(is_anagram('stop', 'pots'))
    print(is_anagram('different', 'letters'))
    print(is_anagram([1, 2, 2], [2, 1, 2]))

    print(has_duplicates('cba'))
    print(has_duplicates('abba'))


if __name__ == "__main__":
    main()
