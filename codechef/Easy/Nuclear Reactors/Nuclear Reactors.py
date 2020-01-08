import sys
ab,n,k = map(int,sys.stdin.readline().split())
a = []
for i in range(k):
    a.append(ab%(n+1))
    ab = ab//(n+1)
res = ""
for i in a:
    res+= str(i) + " "
print(res)
