arr = [2, -6, -3, 8, 4, 1]
n_arr = []
for i in arr:
    if(i>=0):
        n_arr.append(i)

n_arr.sort()
k = 0;
for i in range(len(arr)):
    if(arr[i]>=0):
        arr[i] = n_arr[k]
        k+=1;

print(arr)
