def count_substrings(s):
    s_l = list(map(int,s))
    n = sum(s_l)
    return int(n*(n+1)/2)

for _ in range(int(input())):
    n = int(input())
    print(count_substrings(input()))
