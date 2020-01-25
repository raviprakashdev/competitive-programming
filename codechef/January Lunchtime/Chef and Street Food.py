for _ in range(int(input())):
    high = 0
    for i in range(int(input())):
        s,p,v = map(int,input().split())
        if(p>(s+1)):
            m = int(p/(s+1)) * v
            print(m)
            if m > high:
                high= m
    print(high)
