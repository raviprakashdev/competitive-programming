def lis(arr): 
    n = len(arr) 
    lis = [1]*n
    final_arr = []
    for i in range (1 , n):
        l = []
        for j in range(0 , i): 
            if arr[i] > arr[j] and lis[i]< lis[j] + 1 : 
                l.append(arr[j])  
                lis[i] = lis[j]+1
        if(len(l)>0):
            final_arr.append(l)
    maximum = 0
    print(final_arr)
    for i in range(n):
        maximum = max(maximum , lis[i])
    ret_arr = [ final_arr[0] ]
    print(ret_arr)
    for i in range(len(final_arr)):
        for j in range(len(final_arr)):
            if(len(final_arr[j]) > len(ret_arr[0])):
                ret_arr = [ arr[j] ]
            elif(len(final_arr[j]) == len(ret_arr[0]) and  i!=j ):
                 ret_arr.append(arr[j])   
    return ret_arr
#arr = [10, 22, 9, 33, 21, 50, 41, 60] 
arr = [ 4, 5, 3, 9, 8 , 1, 12, 0 ]
print("Length of lis is", lis(arr) )
