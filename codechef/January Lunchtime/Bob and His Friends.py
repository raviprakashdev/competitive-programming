for i in range(int(input())):
    n,a,b,c = map(int,input().split())
    f = list(map(int, input().split()))
    t = 0
    if( (min(f) < b and max(f) < b) and (min(f) > a and max(f) > a) or (min(f) > b and max(f) > b) and (min(f) < a and max(f) < a) ):
        t = abs(b-a) + c
    else:
        m = (a+b)/2
        p = []
        for i in range(n):
            p.append(f[i] - m)
        p = list(p)
        val = p[0] + m
        minp = abs(val - a)
        maxp = abs(val - b)
        t = maxp + minp + c
    print(int(t))
