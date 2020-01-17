for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    arr2 = arr[:]
    arr2.sort()
    for i in arr:
        a = arr2.index(i)
        print(a,end=" ")
    print()
