N = int(input())

B = 1
C = 1

while N > B:
    B += 6*C
    C += 1

print(C)