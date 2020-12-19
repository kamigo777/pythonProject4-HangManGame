import random
HANGMAN_PICS = ['''
 +---+
     |
     |
     |
    ===''','''
 +---+
 *   |
     |
     |
    ===''','''
 +---+
 *   |
 |   |
     |
    ===''','''
 +---+
 *   |
/|   |
     |
    ===''','''  
 +---+
 *   |
/|\  |
     |
    ===''',''' 
 +---+
 *   |
/|\  |
/    |
    ===''','''
 +---+
 *   |
/|\  |
/ \  |
    ===''']
words = 'аист акула бабуин бобр ' .split()

def getRandomWord(wordList):
    # Эта функция возвращает случаную строку из переданого списка
    wordIndex = random.randint(0, len(wordList) -1)
    return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Ошибочные буквы:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):  # Заменяет пропуски отгаданными буквами
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

        for letter in blanks:   # Показывает секретное слово с пробелами между буквами
            print(letter, end=' ')
        print()

def getGuess(alreadyGuessed):
        # Возвращает букву введеную игроком.Эта функция проверет что игрок ввел только одну букву и ничего больше
    while True:
        print('Введите букву')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Пожалуста, введите одну букву!')
        elif guess in alreadyGuessed:
            print('Вы уже называли эту букву, введите другую')
        elif guess not in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
            print('Введите пожалуйста БУКВУ!')
        else:
            return guess

def playAgain():
    # Эта функция фозращает значение True если игрок хочет сыграть заново
    # в противном случае False
    print('Хотите сыграть еще?(да или нет)')
    return input().lower().startswith('д')

print('В И С Е Л И Ц А')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(missedLetters, correctLetters, secretWord)

    # Позволяет игроку ввести букву
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # Проверяем выиграл ли игрок
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
            if foundAllLetters:
                print('ДА! Секретное слово - "' + secretWord + '" ! Вы угадали! ')
                gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        # Проверяет превысил ли игрок лимит попыток, и проиграл
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
        print('Вы исчерпали все попытки! Не угаданно букв: ' + str(len(missedLetters)) + ' и угаданно букв: ' + str(len(correctLetters)) + '. Было загадано слово "' + secretWord + '" . ')
        gameIsDone = True
        # Запрашивает хочет ли игрок сыграать заново
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)

        else:
            break
