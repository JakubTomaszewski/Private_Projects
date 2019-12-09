
'''
RULES:
(for now all words are in Polish)

the user is shown 7 lines of square brackets
each pair of brackers represents one letter
your task is to guess all the words, created of the letters given
REMEMBER! letters canot be repeated
have fun :)
'''
import random
import time

def printout(to_guess, letters):
    for word in to_guess:
        print(word)
    print('Letters available:', letters)

#Importing file - i'll add this option in the future

#dict letters:[words] - will add more word sets later
d = {'REPISZP':['PISZ', 'PIEPRZ', 'PRZEPIS', 'SER', 'PIES', 'PERS', 'RZEP'], 'UABEKLT': ['BLAT', 'BUTLA', 'BUTELKA', 'BELKA', 'KLUB', 'LUBA', 'BALET']}

letters = random.choice(list(d.keys()))
words = d[letters]
words_game_end = list(words) #creating a copy of the list 'words' in order to remove every guessed word, which allows to check when the game is over
to_guess = [''.join('[ ]' for letter in word) for word in words]

while words_game_end: #continue while the list is not empty
    printout(to_guess, letters)
    print('Your word:', end=' ')
    guess = input().upper().strip()
    if guess in words: #checking if input word is in words to guess
        for i in range(len(guess)):
            to_guess[words.index(guess)] = to_guess[words.index(guess)].replace(' ', words[words.index(guess)][i], 1) #replacing every space with every letter of the guessed word
        words_game_end.remove(guess)
        print('Nice!')
        time.sleep(1.5)
    else:
        print("That's not the word we are looking for")
        time.sleep(1.5)

printout(to_guess, letters)
print('Congrats!')
print('You have won the game!')






