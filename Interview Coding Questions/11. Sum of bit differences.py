from itertools import combinations   
def comb_ret(l):
    comb = combinations(l, 2)   
    count = 0
    for i in list(comb):
        a = list(i)
        c =  int(a[0]) ^ int(a[1])
        c = bin(c).replace('0b','')
        c = list(map(int,str(c)))
        count += sum(c)
    return count*2

for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    print(comb_ret(l))
