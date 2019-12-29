#l = [[0,30], [5,10], [15,20]]
l = [[7,10], [2,4]]
res = set(range(l[0][0],l[0][1]+1))
for i in range(1,len(l)):
    res = set(range(l[i][0],l[i][1]+1)) ^ res
    print(res)
print(res)
