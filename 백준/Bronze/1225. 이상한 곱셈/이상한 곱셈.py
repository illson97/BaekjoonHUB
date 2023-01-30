import sys
input = sys.stdin.readline

A, B = input().split()

list1 = list(map(int, A))
list2 = list(map(int, B))

print(sum(list1) * sum(list2))