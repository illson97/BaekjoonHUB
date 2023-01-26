A, B = map(int, input().split())
P = list(map(int, input().split()))
K = A * B
for i in P:
    print(i - K, end=' ')