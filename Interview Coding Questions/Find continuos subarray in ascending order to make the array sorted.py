'''

Given an integer array you need to find one continuos 
subarray that if you only sort the subarray in 
ascending order then the whole array will be sorted

'''

#l = [2,6,4,8,10,9,15]
l = list(map(int,input().split()))
while min(l) == l[0]:
    l.remove(l[0])
while max(l) == l[-1]:
    l.remove(l[-1])
print(len(l))
