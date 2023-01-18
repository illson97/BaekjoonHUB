W = list(map(int, input().split()))
ans = [1, 2, 3, 4, 5]
while W != ans:
    for j in range(4):
        if W[j] > W[j+1]:
            arr = W[j]
            W[j] = W[j+1]
            W[j+1] = arr
            print(*W)