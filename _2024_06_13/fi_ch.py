word = input('Enter a word: ')
char_num = int(input('Enter a character number: '))
replace = input('Enter a character replacement: ')

listt = list(word)

listt[char_num - 1] = replace

for i in listt:
    print(i, end='')