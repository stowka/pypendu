#!/usr/local/bin/python3.3
#-*- coding: utf-8 -*-

from settings import *
from functions import *
from os import system

system("clear")
print("######################")
print("#" + "PENDU".center(20) + "#")
print("######################\n")

playing = True
lost = True
jokers = NB_JOKERS
letters = []

words = loadWords()
word = pickWord(words)

name = input("What's your name? ").lower()
score = loadScores()
if name in score.keys():
    print("Score : {} pts".format(score[name]))
else:
    print("Score : 0 pt")

while playing and jokers >= 0:
    print("\n\n")
    string = str()
    
    letters_found = 0
    for i in word:
        if i in letters:
            string += "{} ".format(i)
            letters_found += 1
        else:
            string += "_ "
    print(string)
    
    if letters_found == len(word):
        print("Well done {}! You guessed the word {}".format(name[0].upper() + name[1:], word))
        lost = False
        break
    print(*[letter for letter in letters if letter not in word], sep = " / ")
    try:
        letter = input("Try a letter ({}) : ".format(jokers)).upper()
    except:
        pass
    system("clear")
    if letter in letters:
        print("This letter has already been tried.")
        continue
    else:
        letters.append(letter)
        if letter in word:
            print("You guessed the '{}'".format(letter))
        else:
            print("{} is not in the word...".format(letter))
            jokers -= 1

if lost:
    print("{}, you lost!".format(name[0].upper() + name[1:]))
    print("The word was {}".format(word))
else:
    try:
        score[name] += 1 + jokers
    except KeyError:
        score[name] = 1
    storeScore(**score)