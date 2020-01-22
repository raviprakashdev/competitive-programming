def slope(x1,x2,y1,y2):
    if(x2 - x1 == 0):
        return 0
    else:
        m = (y2 - y1)/(x2 - x1)
        return m

n = int(input())
Count = 0

for i in range(n):
    x1,y1,x2,y2,x3,y3 = map(int,input().split())
    m1 = slope(x1,x2,y1,y2)
    m2 = slope(x1,x3,y1,y3)
    m3 = slope(x2,x3,y2,y3)
    m1m2 = m1*m2  
    if(m1m2  == -1 or  (m1 == 0 and m2 == 0)):
        Count+=1
    else:
        m1m2 = m2*m3  
        if(m1m2  == -1 or  (m2 == 0 and m3 == 0)):
            Count+=1
        else:
            m1m2 = m1*m3  
            if(m1m2  == -1 or  (m1 == 0 and m3 == 0)):
                Count+=1
print(Count)
