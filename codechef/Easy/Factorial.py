# cook your dish here
t = int(input())
i=0;
while(i<t):
    a = int(input())
    k = 5;
    count = 0;
    while(k<=a):
        count+=int(a/k);
        k*=5
    print(count)
    i+=1
    