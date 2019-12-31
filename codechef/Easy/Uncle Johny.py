t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    k = int(input())
    v = a[k-1]
    a.sort();
    print(a.index(v)+1)
