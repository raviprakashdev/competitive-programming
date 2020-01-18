def bin2dec(n):
    if(int(n,2) % 3 == 0):
        return 1
    else:
        return 0
for _ in range(int(input())):
    print(bin2dec(str(input())))
