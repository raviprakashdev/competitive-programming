t = int(input())
for _ in range(t):
    s,w1,w2,w3 = map(int,input().split(' '))
    s_w = w1 + w2 + w3
    if(w1 == 1 and w2 == 1 and w3 == 1):
        if(s == 1):
            print(3)
        elif(s==2):
            print(2)
        else:
            print(1)
    elif(w1 == 2 and w2 == 2 and w3 == 2):
        if(s==2):
            print(3)
        elif(s==3):
            print(3)
        elif(s==4 or s==5):
            print(2)
        else:
            print(1)
    elif( s_w <= s):
        print(1)
    elif(s == 2):
        if(w2 == 2):
            print(3)
        elif(s_w == 4):
            print(2)
        else:
            print(3)
    elif(s == 3):
        print(2)
    elif(s == 4):
        print(2)    
    else:
    	print(1)
    
