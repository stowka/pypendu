#!/usr/local/bin/python3.3
#-*- coding: utf-8 -*-

from settings import *
from random import randrange
from os import system
import pickle

scores = dict()

def loadWords():
    with open(WORDS_FILE, 'r') as file:
        content = file.read()
        
    return content
    
def pickWord(words):
    wordList = words.split("\n")
    word = ''
    while len(word) < NB_LETTERS_MIN or len(word) > NB_LETTERS_MAX:
        index = randrange(NB_WORDS)
        word = wordList[index]
    
    return word.upper()

def testLetter(letter, word):
    if letter in word:
        return True
    return False

def loadScores():
    with open(SCORE_FILE, 'rb') as file:
        unpickler = pickle.Unpickler(file)
        try:
            score = unpickler.load()
        except:
            score = {}
        return score
        
def storeScore(**score):
    with open(SCORE_FILE, 'wb') as file:
        pickler = pickle.Pickler(file)
        pickler.dump(score)