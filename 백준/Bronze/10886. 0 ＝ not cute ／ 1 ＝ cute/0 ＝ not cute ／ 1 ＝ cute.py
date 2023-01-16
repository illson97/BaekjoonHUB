N = int(input())
cute = 0
nocute = 0

for i in range(0,N):
    num = int(input())
    if num == 0:
        nocute += 1
    else:
        cute += 1

if nocute > cute:
    print("Junhee is not cute!")

else:
    print("Junhee is cute!")