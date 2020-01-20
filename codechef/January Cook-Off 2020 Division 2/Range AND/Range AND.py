for _ in range(int(input())):
    start, end = map(int,input().split())
    m = 1000000007
    if(start > m):
        start = start%m
    if(end > m):
        end = end%m
    s = start
    b = start
    for i in range(start,end):
        b = b & i & (i+1)
        b = b % m
        s = (s + b)%m
        if(b == 0):
            break
    print(s)
    
