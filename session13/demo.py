def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


h = histogram("Bookkeeper")
# print(h)
number_of_e = h.get("e", 0)
number_of_a = h.get("a", 0)
# print(number_of_e)
# print(number_of_a)


def print_hist(h):
    for c in h:
        print(c, h[c])


h = histogram("Massachusetts")
# print_hist(h)


def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise LookupError()


h = histogram("Massachusetts")
key = reverse_lookup(h, 2)
print(key)
