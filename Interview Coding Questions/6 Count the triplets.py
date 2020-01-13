from itertools import combinations   
for _ in range(int(input())):
    count = 0
    n = int(input())
    a = list(map(int,input().split()))  
    
    comb = combinations(a, 2)   
    for i in list(comb): 
        if( sum(i) in a ):
            count+=1
    if(count):
        print(count)
    else:
        print("-1")
'''

for _ in range(int(input())):
    count = 0
    n = int(input())
    a = list(map(int,input().split()))  
    for i in range(n):
        for j in range(i+1,n):
            if( (a[i] + a[j]) in a  ):
                count+=1
    if(count):
        print(count)
    else:
        print("-1")
'''
