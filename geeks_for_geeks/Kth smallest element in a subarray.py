#arr = [3, 2, 5, 4, 7, 1, 9]
arr = [2, 3, 4, 1, 6, 5, 8]
#query = (2, 6, 3)
query = (1, 5, 2)
l = query[0]
r = query[1]
k = query[2]

n_arr = arr[l-1:r]
n_arr.sort()
print(n_arr)
print(n_arr[k-1])
