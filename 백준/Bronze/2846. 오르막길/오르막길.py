N = int(input())
Pi = list(map(int, input().split()))
orm = 0

for i in range(N):
    for j in range(i + 1, N):
        if Pi[j - 1] < Pi[j]:
            orm = max(orm, Pi[j] - Pi[i])
        else:
            break
print(orm)