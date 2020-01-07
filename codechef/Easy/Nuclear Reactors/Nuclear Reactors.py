ab,n,k = map(int,input().split())
a = [0]*k

def change(i,j):
    #set = 0
    #while(set == 0):
    if(a[i+j] > n):
        #a[i+j]+=1
        #j+=1
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
        set = 0
        j = 1
        '''
        while(set == 0):
            if(a[i+j] > n):
                a[i+j]+=1
                j+=1
            else:
                a[i+1]= a[i+1] + 1
                set = 1
        
        while(j >= 1):
            a[i+j] = 0
            j-=1
            
        if(a[i+1] > n):
            a[i+2]+=1
            if(a[i+2] > n):
                a[i+3]+=1
                a[i+2]=0
            a[i+1]=0
        a[i] = 0
        '''
    else:
        a[i] = a[i] + 1
        
print(a)
