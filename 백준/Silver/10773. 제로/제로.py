K = int(input())
list = []
for i in range(K):
    num = int(input())
    if num == 0:
        list.pop()
    else:
        list.append(num)
print(sum(list))