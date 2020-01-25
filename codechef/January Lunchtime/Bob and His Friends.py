for i in range(int(input())):
    n,a,b,c = map(int,input().split())
    f = list(map(int, input().split()))
    t = 10**18
    for i in range(n):
        t = min(t, abs(f[i] - a) + abs(f[i] - b) + c)
    print(int(t))
