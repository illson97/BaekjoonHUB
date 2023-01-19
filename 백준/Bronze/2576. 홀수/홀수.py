import sys
list1 = []

for i in range(7):
    N = int(sys.stdin.readline())
    if N % 2 == 1:
        list1.append(N)
if list1:
    print(sum(list1))
    print(min(list1))
else:
    print(-1)