def rev(s):
    ret_s = ""
    for i in range(len(s)-1,-1,-1):
        ret_s += s[i]
    return ret_s

for _ in range(int(input())):
    s = input()
    ss = rev(s)
    s_list = ss.split(".")
    for i in range(len(s_list)):
        print(rev(s_list[i]),end="")
        if(i != len(s_list) - 1):
            print(".",end="")
    print('')
