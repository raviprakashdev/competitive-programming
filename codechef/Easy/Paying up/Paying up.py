from itertools import combinations   
t = int(input())
for k in range(t):
    n,m = map(int,input().split())
    l = []
    flag = 0
    for q in range(n):
        l.append(int(input()))
    for j in range(1,len(l)+1):
        comb = combinations(l,j)        
        for i in list(comb):
            if(sum(i) == m):
                flag = 1
                break
            else:
                flag = 0
        if(flag == 1):
            break
        
    if(flag == 1):
        print("Yes")
    else:
        print("No")

