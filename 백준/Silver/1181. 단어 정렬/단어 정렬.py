import sys
N = int(sys.stdin.readline())
words = []
for i in range(N):
    K = sys.stdin.readline().strip()
    if K not in words:
        words.append(K)
words.sort()
words.sort(key=lambda x:len(x))

for i in range(len(words)):
    print(words[i])