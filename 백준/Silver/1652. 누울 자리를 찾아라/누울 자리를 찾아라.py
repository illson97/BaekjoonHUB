N = int(input())
list1 = []

for i in range(N):
    list1.append(input())

horsum = 0
versum = 0

for i in range(N):
    hor = 0
    ver = 0
    for j in range(N):
        if list1[i][j] == '.':
            hor += 1
        elif list1[i][j] == 'X':
            hor = 0
        if hor == 2:
            horsum += 1
        if list1[j][i] == '.':
            ver += 1
        elif list1[j][i] == 'X':
            ver = 0
        if ver == 2:
            versum += 1

print(horsum,versum)