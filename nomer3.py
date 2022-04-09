s = []
a = input()
b = input()
c = input()
d = input()
e = input()
s = [a, b, c, d, e]
i = s.index(max(s))
j = s.index(min(s))
s[i], s[j] = s[j], s[i]
print(s)
