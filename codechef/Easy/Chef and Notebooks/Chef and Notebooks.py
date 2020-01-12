for _ in range(int(input())):
    x,y,k,n = map(int,input().split())
    
    flag = 0
    rem = x - y
    for i in range(n):
        no_of_pages,price = map(int,input().split())
        if( no_of_pages >= rem and price<= k ):
            print("LuckyChef")
            flag = 1        
    if(flag == 0):
        print("UnluckyChef")
