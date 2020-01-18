for _ in range(int(input())):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    print(*a[:k])
