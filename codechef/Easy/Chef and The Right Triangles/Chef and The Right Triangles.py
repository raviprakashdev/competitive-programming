def distance(x1,y1,x2,y2):
    return (x1-x2)**2 + (y1 -y2 )**2
    
count = 0
for _ in range(int(input())):
    x1,y1,x2,y2,x3,y3 = map(int,input().split())
    m1 = distance(x1,y1,x2,y2)
    m2 = distance(x2,y2,x3,y3)
    m3 = distance(x3,y3,x1,y1)
    if(m1 + m2 == m3 or m1 + m3 == m2 or m2 + m3 == m1):
        count+=1
print(count)
