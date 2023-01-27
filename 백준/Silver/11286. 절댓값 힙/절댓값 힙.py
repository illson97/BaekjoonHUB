import heapq
import sys

N = int(sys.stdin.readline())
list1 = []

for N in range(N):
    x = int(sys.stdin.readline())
    if x !=0:
        heapq.heappush(list1, (abs(x), x))
    else:
        try:
            print(heapq.heappop(list1)[1])
        except:
            print(0)