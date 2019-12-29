n = int(input())
l = []
for i in range(n):
    p = []
    for j in range(n):
        p.append(i*(j+1))
    l.append(p)
print(l)
