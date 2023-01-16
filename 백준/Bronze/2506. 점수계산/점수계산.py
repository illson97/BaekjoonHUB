N = int(input())
K= list(map(int, input().split()))
sum1 = 0
sum2 = 0

for i in range(N):
    if K[i] == 1:
        sum1 += 1
        sum2 += sum1
    else:
        sum1 = 0
        
print(sum2)