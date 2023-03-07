def friendly_ratio(first_name):
    count=0
    count_friendly=0
    f=open('data/words.txt')
    for line in f:
        word=line.strip()
        count=count+1
        if len(first_name)==len(word):
            count_freindly=count_friendly+1
        elif first_name[0]==word[0]:
            count_freindly=count_friendly+1
        else:
            pass
    print(count,count_friendly)
    return count_friendly/count

print(friendly_ratio("Zide"))

