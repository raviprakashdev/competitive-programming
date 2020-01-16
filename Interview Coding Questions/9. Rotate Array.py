for _ in range(int(input())):
    n,d = map(int,input().split())
    arr = list(map(int,input().split()))
    final_arr = arr[d:]
    for i in range(d):
        final_arr.append(arr[0])
        arr.remove(arr[0])
    print(*final_arr)
