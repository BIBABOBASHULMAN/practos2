from collections import Counter
#lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 8, 7, 6, 4, 3, 2, 3, 4, 6, 7, 8, 7]
lst = input()
a = [k for k,v in Counter(lst).items() if v>1]
print(a)
