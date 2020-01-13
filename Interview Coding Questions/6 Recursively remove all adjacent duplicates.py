for _ in range(int(input())):
    s = input()
    j = 0
    f = 0
    while(j < len(s)-1):
        if(s[j]==s[j+1]):
            comp = s[j]
            while(s[j+1] == comp):
                j+=1
                try:
                    if(s[j+1] != comp):
                        f = 1
                        break
                except(IndexError):
                    f = 0
                    break
        else:
            print(s[j],end="")    
        j+=1
    if(s[len(s)-1] != s[len(s)-2]):
        print(s[len(s)-1])
    else:
        print('')
