for _ in range(int(input())):
    n = int(input())
    arr = [int(x) for x in input().split()]
    i = 1
    a = arr[0]
    while( i < len(arr) ):
        if(a < arr[i]):
            arr.remove( arr[i] )
        else:
            a = arr[i]
            i+=1
    print(i)
