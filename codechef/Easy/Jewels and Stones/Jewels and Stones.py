for _ in range(int(input())):
    jewels = input()
    stones = input()
    count = 0
    all_index = set()
    for i in range(len(jewels)):
        for j in range(len(stones)):
            if( jewels[i] == stones[j]):
                all_index.add(j)                
    print(len(all_index))
