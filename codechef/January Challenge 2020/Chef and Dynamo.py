import sys
import random 
def ret_perfect(n):
    a = list(range(1,10**n))
    num = random.choice(a)
    if(num>10):
        while(num%10 == 0):
            num=num%10
    if(num == 10):
        num -= 1
    return num

t = int(input())
for _ in range(t):
    n = int(input())
    a = int(input())
    s = 5*(10**n)
    print(s)
    sys.stdout.flush()
    b = int(input())
    c = 4
    print(c)
    sys.stdout.flush()
    d = int(input())
    e = s - (a+b+c+d)
    print(e)
    sys.stdout.flush()
    f = int(input())
    if(f == -1):
        break
