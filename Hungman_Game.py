import random
hungman = ["o",
           "/", "|", "\\",
           "/", "\\"]


def choose_word():
    words = ["apple", "banana", "grapes"]
    word = random.choice(words)
    return word


word = choose_word()
wrong_turn = 0
size = 0
while wrong_turn < 6 and size < len(word):
    guess = input("Enter a letter: ")
    if guess in word:
        size += 1
        continue
    else:
        print(hungman[0:wrong_turn+1])
        wrong_turn += 1

if wrong_turn == 5:
    print("You lost")
elif size == len(word):
    print("Hey you did incredible")
    print("Actual word was: "+word)
