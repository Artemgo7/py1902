# Python lessons

***This is Char***

<img src="https://vignette.wikia.nocookie.net/ninjago/images/0/07/%D0%96%D0%B5%D0%B7%D0%BB%D0%90%D1%84%D0%B8%D0%B3%D0%B5%D0%B7%D0%BB.jpg/revision/latest?cb=20190610091622&path-prefix=ru" width="200" height="200" />

> - ***Чар спера-змей а ты нет***

***This is python ***

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Python.svg/1024px-Python.svg.png" width="200" height="200" />

> - ***Зысыс пи'тон бат юу ноу***

#### Список зантий
> - lesson 1 - 01.01.01
> - lesson 2 - 02.02.02
> - lesson 3 - 03.03.03
> - lesson 4 - 04.04.04
> - lesson 5 - 05.05.05
> - lesson 6 - 06.06.06
> - lesson 7 - 07.07.07
> - lesson 8 - 08.08.08
> - lesson 9 - 09.09.09
> - lesson 10 - 10.10.10
> - lesson 11 - 11.11.11
> - lesson 12 - 12.12.12
> - lesson 13 - 13.13.13
> - lesson 14 - 14.14.14
> - lesson 15 - 15.15.15
> - lesson 16 - 16.16.16

#### Вставка кода

- Запуск python код
```
import random

HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''','''
  +---+
  O   |
      |
      |
     ===''','''
  +---+
  O   |
  |   |
      |
     ===''','''
  +---+
  O   |
 /|   |
      |
     ===''','''
  +---+
  O   |
 /|\  |
      |
     ===''','''
  +---+
  O   |
 /|\  |
 /    |
     ===''','''
  +---+
  O   |
 /|\  |
 / \  |
     ===''',]

words = 'аист акула бабуин баран барсук бобр бык верблюд волк воробей ворон выдра голубь гусь'.split()

def getRandomWord(wordList):
    wordIndex = random.randint(0, len(wordList)-1)
    return wordList[wordIndex]

#print(getRandomWord(words))
def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Ошибочные буквы: ', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    while True:
        print('Введите букву: ')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Пожалуйста, введите одну букву')
        elif guess in alreadyGuessed:
            print('Вы уже вводили данную букву. Введите другой символ.')
        elif guess not in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
            print('Пожалуйста, введите БУКВУ')
        else:
            return guess

def playAgain():
    print('Хотите сыграть еще? (да / нет)')
    return input().lower().startswith('д')

print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(missedLetters, correctLetters, secretWord)
    guess = getGuess(missedLetters + correctLetters)
    if guess in secretWord:
        correctLetters = correctLetters + guess
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Секрутное слово - "'+secretWord+'"! Вы угадали!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        if len(missedLetters) == len(HANGMAN_PICS)-1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('Вы исчерпали все попытки!\n Было загадано слово:"'+secretWord+'".')
            gameIsDone = True

    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            secretWord = getRandomWord(words)
            gameIsDone = False
        else:
            break
```            
            
### Git comand

- Основные команды гита 
  * инициализация репозитория на компьютере в созданной папке
    > git init

  * добавляем любой созданный файл
    > git add test.filetype

  * создаем изменение в репозитории, добавляя файл и обязательно пишем название изменения
    > git commit -m "first commit"
    
  * подключаем удаленный репозиторий с сайта называя удаленный репозиторий = origin (это пример ссылки на мой репозиторий)
    > git remote add origin https://github.com/name/123.git
    
  * заливаем на сайт (удаленный репозиторий) наш коммит с нашего локального репозитория называемого master
    > git push -u origin master

> - если вы дома хотите закачать файл в удаленный репозиторий (на сайт), вам нужно сделать следующее:
1. инициализировать гит-репозиторий на компьютере и прописать настройки имени и почты
2. скачать файлы с удаленного репозитория (если они там есть)
3. создать или скопировать файл проекта в папку внутри репозитория
4. добавить изменение в коммит
5. сделать коммит с комментарием изменений
6. закачать файлы с локального репозитория на удаленный (последняя команда в предыдущем сообщении)

   * Не забываем после инициализации репозитория на компьютере дома прописывать настройки
    > ngit config --global user.name "MyMarvel"
    > git config --global user.email "xxx@xxx.com"
    а то у вас ничего не получиться

#### Список основных ресурсов
***Git comand***
*Прочтите, у кого есть проблемы с чем-то*
> - http://nikita-petrov.com/drupal/kak-rabotat-s-github-repozitoriyami
> - https://www.markdownguide.org/basic-syntax/
