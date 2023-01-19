word = ["a", "e", "i", "o", "u"]
while True:
    cnt = 0
    S = input().lower()
    if S == "#":
        break
    for i in(S):
        if i in word:
            cnt += 1
    print(cnt)