t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split(' ')))
    i = 1
    count = 1;
    a = arr[0]
    while( i < len(arr) ):
        if(a < arr[i]):
            i+=1
        else:
            a = arr[i]
            count+=1
            i+=1
    print(count)
