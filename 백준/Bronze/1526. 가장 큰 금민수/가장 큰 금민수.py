import sys

N = int(sys.stdin.readline().rstrip())

for i in range(N):
    cnt = 0
    for j in str(N - i):
        if j == "7" or j == "4":
            pass
        else:
            cnt = 1
            break
    if cnt == 0:
        break
print(N - i)