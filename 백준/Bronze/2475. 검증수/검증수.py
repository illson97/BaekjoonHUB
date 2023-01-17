N = list(map(int, input().split()))
nums = 0
for i in N:
    nums += i*i
    
print(nums % 10)