data = input();
#data = "1 2 3 6 7 10 12"
x = int(input())
#x = 7
k = int(input())
#k = 5
l = list(map(int,data.split()))
n = []
p = []
for i in range(len(l)):
     val = x - l[i]
     if(val<0):
         n.append(val)
     else:
         p.append(val)        
n.sort(reverse=True)
p.sort()
i = 0
j = 0
f = []
print(l)
print(n)
print(p)
while(i+j<k):
    if(len(n)>0 and len(p)>0):
        if(abs(n[i]) < p[j]):
            f.append(abs(n[i] - x))
            print(n[i])
            i+=1
            print(f)
        else:
            f.append(abs(p[j]-x))
            print(p[j])
            j+=1
            print(f)
    elif(len(n)>0 and len(p) == 0):
        f.append(abs(n[i] - x))
        print(n[i])
        i+=1
        print(f)    
    else:
        f.append(abs(p[j]-x))
        j+=1
        print(f)
        print("no")
print(f)
f.sort()
print(f)

