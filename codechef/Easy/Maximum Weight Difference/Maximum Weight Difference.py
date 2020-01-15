for _ in range(int(input())):
    n,k = map(int,input().split())
    w = list(map(int,input().split()))
    s = 0
    w.sort()
    S = sum(w)
    S1 = sum(w[:k])
    S2 = sum(w[-k:])
    print(max(abs(S1 - (S - S1)), abs(S2 - (S - S2))))
