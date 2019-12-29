#l = [2,6,4,8,10,9,15]
l = list(map(int,input().split()))
while min(l) == l[0]:
    l.remove(l[0])
while max(l) == l[-1]:
    l.remove(l[-1])
print(len(l))
