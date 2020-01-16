def check_feed(s):
    sa = s.split("010")
    if(len(sa) == 1):
        sa = s.split("101")
    if(len(sa) == 1):
        return "Bad"
    else:
        return "Good"
    
for _ in range(int(input())):
    s = input()
    print(check_feed(s))
