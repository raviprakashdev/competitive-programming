ab,n,k = map(int,input().split())
a = [0]*k
for i in range(ab):
    a[0] = a[0] + 1
    while(max(a) == (n+1)):
        i = a.index(max(a))
        a[i] = 0
        a[i+1] = a[i+1] + 1
res = ""
for i in a:
    res += str(i)+" " 
print(res)
