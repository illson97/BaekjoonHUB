import sys

A, B = map(int, sys.stdin.readline().split())

A_list = set(map(int, input().split()))
B_list = set(map(int, input().split()))

print(len(A_list ^ B_list))