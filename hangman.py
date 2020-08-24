import random

def create_word_list():
    # opens word list and makes into a list.
    word_list = []
    for line in open('word_list.txt','r'):
        word_list.append(line.strip())

    return word_list

def pick_word(word_list):
    #sets length of word_list
    length = len(word_list)
    # picks a random number within the amount of words in word list
    pick_number = random.randint(0,length)
    # uses pick_number to pick a random word from wordlist
    hangman_word = word_list[pick_number]
    return hangman_word

def hide_word(hangman_word):
    # hides the letters in hangman_word
    hidden_hangman_word = ''
    for letter in hangman_word:
        hidden_hangman_word += '*'
    hidden_hangman_word = list(hidden_hangman_word)

    return hidden_hangman_word


def guess(hidden_hangman_word,hangman_word,wrong_guess):
    # asks user for guess and checks against word, then replaces words.
    c = False
    while c == False:
        next_guess = input('Please enter your next guess: ').lower()
        if len(next_guess) == 1:
            c = True
        else:
            print('Incorrect input!')
    letter_no = 0
    wrong = 0
    for letter in hangman_word:
        if next_guess == letter:
            hidden_hangman_word[letter_no] = letter
            letter_no += 1
        else:
            letter_no += 1
            wrong += 1

    if wrong == len(hangman_word):
        wrong_guess += 1
        return hidden_hangman_word,wrong_guess
    else:
        return hidden_hangman_word,wrong_guess


wrong_guess = 0
word_list = create_word_list()
hidden_word = '*'
word = pick_word(word_list)
hidden_word = hide_word(word)
# allows for debugging
#print(word)
while wrong_guess < 7:
    if '*' in hidden_word:
        print(hidden_word)
        hidden_word,wrong_guess = guess(hidden_word,word,wrong_guess)
    else:
        print('congratulations you win')
        print(hidden_word)
        break
print('you lose')
