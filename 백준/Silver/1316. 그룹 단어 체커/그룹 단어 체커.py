n = int(input())

word_list = 0
for _ in range(n):
    word = input()
    error = 0
    for index in range(len(word)-1):
        if word[index] != word[index+1]:
            new_word = word[index+1:]
            if new_word.count(word[index]) > 0:
                error += 1
    if error == 0:
        word_list += 1
print(word_list)