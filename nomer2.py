from collections import Counter
lst = [1, 2, 3, 4, 5, 6, 7, 8, 1, 3, 4, 6]
a = [k for k,v in Counter(lst).items() if v>1]
print(a)
