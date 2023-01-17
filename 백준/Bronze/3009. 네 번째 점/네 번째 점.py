X = []
Y = []

for _ in range(3):
    num1, num2 = map(int, input().split())
    if num1 in X:
        X.remove(num1)
    else:
        X.append(num1)
    if num2 in Y:
        Y.remove(num2)
    else:
        Y.append(num2)
        
print(X[0], Y[0])