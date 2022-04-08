a = input()
b = input()
c = []
for i in a:
    if i in c:
        continue
    for j in b:
        if i == j:
            c.append(i)
            break

print(c)

