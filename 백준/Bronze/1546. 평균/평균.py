n = int(input())
test_list = list(map(int, input().split()))
M = max(test_list)

new_list = []
for score in test_list:
    new_list.append(score/M*100)
test_avg = sum(new_list)/n
print(test_avg)