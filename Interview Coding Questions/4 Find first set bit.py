#code
for _ in range(int(input())):
    a = int(input())
    a_bin = bin(a).replace('0b','')
    j=1
    flag = 0
    for i in range(len(a_bin)-1,-1,-1):
        if(a_bin[i] == "1"):
            flag = j
            break
        else:
            j+=1
    print(flag)
