t = int(input())
for i in range(t):
   arr = list(map(int,input().split()))
   #n is total number of jobs that must be completed before closing
   n = arr[0]
   #m is number of jobs that are already complete
   m = arr[1]
   #arr1 contains the integers that are complete. 
   arr1 = list(map(int,input().split()))
   set1 = set(range(1,n+1))
   set2 = set(arr1)
   arr2 = list(set1 ^ set2)
   for j in range(len(arr2)):
        if(j%2 == 0 and (len(arr2) == j+1 or len(arr2) == j+2)):
           print(arr2[j])
        elif(j%2 == 0):
            print(arr2[j],end=" ")
   for j in range(len(arr2)):
        if(j%2 != 0 and (len(arr2) == j+1 or len(arr2) == j+2)):
           print(arr2[j])
        elif(j%2 != 0):
            print(arr2[j],end=" ")
   if(len(arr2)==1):
       print('')
   

