t = int(input())
n = int(input())
s = list(map(int,input().split()))
s.sort()
k = set()
for i in range(len(s)-1):
    k.add(s[i+1] - s[i])
print(min(k))
