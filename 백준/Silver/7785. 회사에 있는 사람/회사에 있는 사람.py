import sys
input = sys.stdin.readline

ch_list = dict()
N = int(input())

for i in range(N):
    A, B = map(str, input().split())
    if B == 'enter':
        ch_list[A] = 1
    else:
        del ch_list[A]
        
ch_list = sorted(ch_list.keys(), reverse = True)

for j in ch_list:
    print(j)