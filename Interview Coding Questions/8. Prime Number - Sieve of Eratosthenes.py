from math import sqrt
n = int(input())
nonprimes = {}
for i in range( 2, int(sqrt(n))+1 ):
    for j in range( 2, n//i + 1 ):
        nonprimes[i*j] = 1
for j in range(2,n+1):
    if j not in nonprimes:
        print(j,end=" ")
print(nonprimes)
