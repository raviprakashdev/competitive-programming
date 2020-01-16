from math import sqrt
for _ in range(int(input())):
    n1,n2 = map(int,input().split())
    nonprime = {}
    for i in range(2, int(sqrt(n2) + 1)):
        for j in range(max(n1//i, 2),(n2//i) + 1):
            nonprime[i*j] = 1
            
    for i in range(max(n1, 2), n2+1):
        if i not in nonprime:
            print(i)
    print('')
