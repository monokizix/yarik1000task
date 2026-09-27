import random

words = ['python', 'java', 'kotlin', 'javascript']
secret_word = random.choice(words)
display = list('_' * len(secret_word))
lives = 6

print('Добро пожаловать в Виселицу!')
print(' '.join(display))

while lives > 0 and '_' in display:
    guess = input('\nВведите букву: ').lower()

    if len(guess) != 1 or not guess.isalpha():
        print('Пожалуйста, введите одну букву.')
        continue

    if guess in secret_word:
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display[i] = guess
        print('Верно!')
    else:
        lives -= 1
        print(f'Нет такой буквы. Осталось жизней: {lives}')

    print(' '.join(display))

if '_' not in display:
    print('\nПоздравляю! Вы угадали слово:', secret_word)
else:
    print('\nВы проиграли. Загаданное слово было:', secret_word)