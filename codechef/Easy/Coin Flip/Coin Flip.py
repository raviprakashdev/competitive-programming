t = int(input())
for i in range(t):
    g = int(input())
    for j in range(g):
        i,n,q = map(int,input().split())
        if(i == q):
            print(n//2)
        else:
            print((n+1)//2)
