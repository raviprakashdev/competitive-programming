for _ in range(int(input())):
    s = str(input())
    if(len(s) == 1):
        print("NO")
    else:
        rem = ""
        i = 0
        while(i < len(s)-1):
            count = 1
            j = i
            while(True):
                try:
                    if(s[j] == s[j+1] and j < (len(s) - 1)):
                        count+=1
                        j+=1
                        i = j
                    else:
                        break
                except(IndexError):
                    break
            rem = rem + s[i] + str(count)
            i+=1
        if(s[len(s)- 1] != s[len(s)- 2]):
            rem = rem + s[len(s)- 1] + "1"
        if(len(rem) < len(s)):
            print("YES")
        else:
            print("NO")
