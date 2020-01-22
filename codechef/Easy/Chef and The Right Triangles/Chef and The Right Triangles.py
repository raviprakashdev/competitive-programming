from math import sqrt
def distance(x1,y1,x2,y2):
    return sqrt( (x2-x1)**2 + (y2-y1)**2  )

def slope(x1,x2,y1,y2):
    if(x2 - x1 == 0):
        if(y2 - y1 == 0):
            return -1
        else:
            return 1
    else:
        m = (y2 - y1)/(x2 - x1)
        print(m)
        return m

def pyth(d1,d2):
    m = sqrt(d1**2 + d2**2)
    return m

n = int(input())
Count = 0
for i in range(n):
    x1,y1,x2,y2,x3,y3 = map(int,input().split())
    d1 = distance(x1,y1,x2,y2)
    d2 = distance(x1,y1,x3,y3)
    d3 = distance(x2,y2,x3,y3)

    p1 = pyth(d1,d2)
    p2 = pyth(d2,d3)
    p3 = pyth(d1,d3)

    if(  )
    
    

for i in range(n):
    x1,y1,x2,y2,x3,y3 = map(int,input().split())
    m1m2 = slope(x1,x2,y1,y2) * slope(x1,x2,y1,y2)  
    if(m1m2  == -1 ):
        Count+=1
    else:
        m1m2 = slope(x1,x2,y1,y2) * slope(x1,x3,y1,y3)  
        if(m1m2  == -1 ):
            Count+=1
        else:            
            m1m2 = slope(x2,x3,y2,y3) * slope(x1,x3,y1,y3)  
            if(m1m2  == -1 ):
                Count+=1

print(Count)
