T = int(input())
for t in range(1, T + 1):
    nums = list(map(int, input().split()))
    print('#{} {}'.format(t, round(sum(nums)/len(nums))))