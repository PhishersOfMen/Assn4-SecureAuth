# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 13:58:24 2019

@author: morgg
"""
import os
import os.path
def stringConvert(words):
    reader = open(words,"r")
    maker = reader.readlines()
    if(os.path.isfile("Enhanced.txt") == True):
        os.remove("Enhanced.txt")
    counter = 1
    for wording in maker:
        word = wording.rstrip()
        print(word)
        if(counter % 2 == 0):
            twoWord = word + word 
            backWords = twoWord[::-1]
            lastCap= backWords
            newCap =""
            for i in range(len(lastCap)):
                if (i == len(lastCap)-1):
                    newCap += lastCap[i].upper()
                else:newCap += lastCap[i]
            numWord = newCap + str(counter)
            specialWord = numWord + "#"
            replaceWord = specialWord
            helperOne = replaceWord.replace("a" and "A","@")
            helperTwo = helperOne.replace("i"and "I","!")
            helperThree = helperTwo.replace("s"and "S","$")
            helperFour = helperThree.replace("o"and "O","0")
        else:
            twoWord = word+word+word
            backWords = twoWord[::-1]
            lastCap= backWords
            newCap =""
            for i in range(len(lastCap)):
                if (i == 0):
                   newCap += lastCap[i].upper()
                else:newCap += lastCap[i] 
            numWord = newCap + str(counter)
            specialWord = numWord + "*"
            replaceWord = specialWord
            helperOne = replaceWord.replace("e","3")
            helperTwo = helperOne.replace("f","|=")
            helperThree = helperTwo.replace("s","5")
            helperFour = helperThree.replace("o","0")
        print(twoWord)
        print(backWords)
        print(newCap)
        print(numWord)
        print(specialWord)
        print(helperFour)
        f = open("Enhanced.txt","a+")
        f.write(word)
        f.write(" ")
        f.write(twoWord)
        f.write(" ")
        f.write(backWords)
        f.write(" ")
        f.write(newCap)
        f.write(" ")
        f.write(numWord)
        f.write(" ")
        f.write(specialWord)
        f.write(" ")
        f.write(helperFour)
        f.write("\n")
        f.close()
        counter += 1
reader = ("words.txt")
stringConvert(reader)

