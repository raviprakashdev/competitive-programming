a = list(map(int,input().split(' ')))
b = str(a[0]-a[1]);
if(int(b[len(b)-1]) == 9):
    print(int(b)-1)
else:
    print(int(b)+1)
