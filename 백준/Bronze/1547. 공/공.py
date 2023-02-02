M = int(input())
cup = [0, 1, 0, 0]

for _ in range(M):
    X, Y = map(int, input().split())
    cup[X], cup[Y] = cup[Y], cup[X]

print(cup.index(1))
