for _ in range(int(input())):
    x,y,k,n = map(int,input().split())
    
    pages_filled = 0
    no_of_pages = []
    price = []
    
    for i in range(n):
        no_of_pages.append(int(input()))
        price.append(int(input()))
    
