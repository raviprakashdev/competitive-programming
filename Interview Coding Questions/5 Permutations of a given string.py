#code
from itertools import permutations 
for _ in range(int(input())):
    p = list(input())
    p.sort()
    perm = permutations(p)
    for i in list(perm):
        for j in range(len(i)):
            print(i[j],end="")
        print('',end=" ")
    print('')
