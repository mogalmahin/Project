import itertools
import sys
f = open("sowpods.txt", "r")
wordlist = []
for i in f:
   wordlist.append(i.strip())
rack = input("enter a word: ")
scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, "l": 1, "o": 1, "n": 1, "q": 10,"p": 3, "s": 1, "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, "x": 8, "z": 10}
temp = rack.upper()
g_words = []


def isValid_word():
    for size in range(2, len(temp) + 1):
        for word in itertools.permutations(temp, size):
            r = "".join(word)
            if r not in g_words:
                g_words.append(r)
    return g_words
 
def score_word(word):       
    return sum([scores[c] for c in word.lower()])
 


def Sowpods():
    for word in isValid_word():
        if word in wordlist:
            s = score_word(word)
            print(s, word, end = " ")
            print()


Sowpods()

            
     
            
