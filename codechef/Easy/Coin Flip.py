t = int(input())
for i in range(t):
    g = int(input())
    for j in range(g):
        i,n,q = map(int,input().split())
        if(i == 1):
            if(n%2 == 1):
                if(q == 1):
                    print(n//2)
                else:
                    print((n+1)//2)
            else:
                print(n//2)
        else:            
            if(n%2 == 1):
                if(q == 1):
                    print((n+1)//2)
                else:
                    print(n//2)
            else:
                print(n//2)
