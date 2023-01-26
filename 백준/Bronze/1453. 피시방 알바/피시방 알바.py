N = int(input())
list = []
num = 0
cus = input().split()
for i in range(N):
    if cus[i] not in list:
        list.append(cus[i])
    else:
        num += 1
print(num)