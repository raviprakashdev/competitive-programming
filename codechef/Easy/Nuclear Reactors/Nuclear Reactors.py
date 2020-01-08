ab,n,k = map(int,input().split())
a = [0]*k

def change(i,j):
    if(a[i+j] > n):
        change(i,(j+1))
        a[i+j+1] = 0
    else:
        a[i+1]= a[i+1] + 1

for k in range(ab):
    i = 0
    print(k,a)
    if(a[i]+1 > n):
        print(a)
        change(i,1)
    else:
        a[i] = a[i] + 1
        
print(a)
