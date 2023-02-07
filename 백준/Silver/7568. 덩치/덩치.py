N = int(input())
list1 = []

for i in range(N):
    X, Y = map(int, input().split())
    list1.append([X, Y])

for i in list1:
    rank = 1
    for j in list1:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
            
    print(rank, end = " ")