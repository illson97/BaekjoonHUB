T = int(input())

for _ in range(T):
    K = input()
    list1 = list(K)
    sum = 0

    for i in list1:
        if i == "(":
            sum += 1
        elif i == ")":
            sum -= 1
        if sum < 0:
            print("NO")
            break

    if sum > 0:
        print("NO")
    elif sum == 0:
        print("YES")