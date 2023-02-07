import sys
input = sys.stdin.readline

list1 = [int(input()) for _ in range(int(input()))]
right = list1.pop()
res = 1
for i in range(len(list1)):
    N = list1.pop()
    if N > right:
        res+=1
        right = N
print(res)