if __name__ == '__main__':
    n = int(input())
    integer_list = tuple(list(map(int, input().split())))
    print(hash(integer_list))
