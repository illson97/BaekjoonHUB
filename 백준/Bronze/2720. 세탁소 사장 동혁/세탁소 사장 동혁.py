T = int(input())

for _ in range(T):
    C = int(input())        
    C_list = {25: 0, 10: 0, 5: 0, 1: 0}
    
    while C:
        for num in [25, 10, 5, 1]:
            while C >= num:
                C -= num
                C_list[num] += 1
                
    print(C_list[25], C_list[10], C_list[5], C_list[1]) 