W = input()
word = ''

for i in W:
    if i not in 'CAMBRIDGE':
        word += i
        
print(word)