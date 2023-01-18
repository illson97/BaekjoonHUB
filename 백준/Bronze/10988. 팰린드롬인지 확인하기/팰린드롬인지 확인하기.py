word = input()
palin = list(reversed(list(word)))

if palin == list(word):
    print(1)
else:
    print(0)
    