for _ in range(int(input())):
    n = int(input())
    A  = list(map(int,input().split()))
    ni = 0
    nli = 0

    if(len(A) == 1):
        print("YES")
    else:        
        for i in range(n):
            for j in range(i+1,n):
                if(A[i] > A[j]):
                    ni +=1
        
        for i in range(n-1):
            if(A[i] > A[i+1]):
                nli+=1
        if(ni == nli):
            print("YES")
        else:
            print("NO")
