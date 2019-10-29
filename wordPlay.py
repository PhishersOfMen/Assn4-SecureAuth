# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 13:58:24 2019

@author: morgg
"""
import os
import os.path
ENHANCED = "Enhanced.txt"
if(os.path.isfile("Enhanced.txt") == True):
    os.remove("Enhanced.txt") 

f = open(ENHANCED,"a")

def lastCap(word):
    newWord = ""
    for i in range(len(word)):
        if (i == len(word)-1):
            newWord += word[i].upper()
        else:newWord += word[i]
    return newWord

def firstCap(word):
    newWord = ""
    for i in range(len(word)):
        if (i == 0):
            newWord += word[i].upper()
        else:newWord += word[i]
    return newWord
  
def replacer(word): 
    if ("a" in word):
        helperOne = word.replace("a","@")
        f.write(helperOne)
        f.write(" ")
        if("i" in word):
            helperEight = helperOne.replace("i","!")
            f.write(helperEight)
            f.write(" ")
            if("s" in word):
                helperThirteen = helperEight.replace("s","$")
                helperFourteen = helperEight.replace("s","5")
                f.write(helperThirteen)
                f.write(" ")
                f.write(helperFourteen)
                f.write(" ")
                if("e" in word):
                    helperSeventeen = helperThirteen.replace("e","3")
                    helperEighteen = helperFourteen.replace("e","3")
                    f.write(helperSeventeen)
                    f.write(" ")
                    f.write(helperEighteen)
                    f.write(" ")
                    if("o" in word):
                        helperTwentyOne = helperThirteen.replace("o","0")
                        helperTwentyTwo = helperFourteen.replace("o","0")
                        f.write(helperTwentyOne)
                        f.write(" ")
                        f.write(helperTwentyTwo)
                        f.write(" ")
                elif("o" in word):
                    helperNinteen = helperThirteen.replace("o","0")
                    helperTwenty = helperFourteen.replace("o","0")
                    f.write(helperNinteen)
                    f.write(" ")
                    f.write(helperTwenty)
                    f.write(" ")
            elif("e" in word):
                helperFifteen = helperEight.replace("e","3")
                f.write(helperFifteen)
                f.write(" ")
                if("o" in word):
                    helperTwentyThree = helperFifteen.replace("o","0")
                    f.write(helperTwentyThree)
                    f.write(" ")
            elif("o" in word):
                helperSixteen = helperEight.replace("o","0")
                f.write(helperSixteen)
                f.write(" ")
        elif("s" in word):
            helperNine = helperOne.replace("s","$")
            helperTen = helperOne.replace("s","5")
            f.write(helperNine)
            f.write(" ")
            f.write(helperTen)
            f.write(" ")
            if("e" in word):
                helperTwentyFour = helperNine.replace("e","3")
                helperTwentyFive = helperTen.replace("e","3")
                f.write(helperTwentyFour)
                f.write(" ")
                f.write(helperTwentyFive)
                f.write(" ")
                if("o" in word):
                    helperTwentySix = helperTwentyFour.replace("o","0")
                    helperTwentySeven = helperTwentyFive.replace("o","0")
                    f.write(helperTwentySix)
                    f.write(" ")
                    f.write(helperTwentySeven)
                    f.write(" ")
        elif("e" in word):
            helperEleven = helperOne.replace("e","3")
            f.write(helperEleven)
            f.write(" ")
            if("o" in word):
                helperTwentyEight = helperEleven.replace("o","0")
                f.write(helperTwentyEight)
                f.write(" ")
        elif("o" in word):
            helperTwelve = helperOne.replace("o","0")
            f.write(helperTwelve)
            f.write(" ")
    if ("i" in word):
        helperTwo = word.replace("i","!")
        f.write(helperTwo)
        f.write(" ")
        if("e" in word):
            helperTwentyNine = helperTwo.replace("e", "3")
            f.write(helperTwentyNine)
            f.write(" ")
            if("o" in word):
                helperThirtyThree = helperTwentyNine.replace("o","0")
                f.write(helperThirtyThree)
                f.write(" ")
                if("s" in word):
                    helperThirtySix = helperThirtyThree.replace("s","$")
                    helperThirtySeven = helperThirtyThree.replace("s","5")
                    f.write(helperThirtySix)
                    f.write(" ")
                    f.write(helperThirtySeven)
                    f.write(" ")
            elif("s" in word):
                helperThirtyFour = helperTwentyNine.replace("s","$")
                helperThirtyFive = helperTwentyNine.replace("s", "5")
                f.write(helperThirtyFour)
                f.write(" ")
                f.write(helperThirtyFive)
                f.write(" ")
        elif("o" in word):
            helperThirty = helperTwo.replace("o", "0")
            f.write(helperThirty)
            f.write(" ")
            if ("s" in word):
                helperThirtySix = helperThirty.replace("s","$")
                helperThirtySeven = helperThirty.replace("s", "5")
                f.write(helperThirtySix)
                f.write(" ")
                f.write(helperThirtySeven)
                f.write(" ")
        elif("s" in word):
            helperThirtyOne = helperTwo.replace("s","$")
            helperThirtyTwo = helperTwo.replace("s","5")
            f.write(helperThirtyOne)
            f.write(" ")
            f.write(helperThirtyTwo)
            f.write(" ")
    if ("e" in word):
        helperThree = word.replace("e", "3")
        f.write(helperThree)
        f.write(" ")
        if("o" in word):
            helperThirtyEight = helperThree.replace("o","0")
            f.write(helperThirtyEight)
            f.write(" ")
            if("s" in word):
                helperFourtyOne = helperThirtyEight.replace("s","$")
                helperFourtyTwo = helperThirtyEight.replace("s","5")
                f.write(helperFourtyOne)
                f.write(" ")
                f.write(helperFourtyTwo)
                f.write(" ")
        elif("s" in word):
            helperThirtyNine = helperThree.replace("s","$")
            helperFourty = helperThree.replace("s","5")
            f.write(helperThirtyNine)
            f.write(" ")
            f.write(helperFourty)
            f.write(" ")
    if ("o" in word):
        helperFour = word.replace("o","0")
        f.write(helperFour)
        f.write(" ")
        if("s" in word):
             helperFourtyThree = helperFour.replace("s","$")
             helperFourtyFour = helperFour.replace("s","5")
             f.write(helperFourtyThree)
             f.write(" ")
             f.write(helperFourtyFour)
             f.write(" ")
    if ("s" in word):
        helperFive = word.replace("s", "$")
        helperSix = word.replace("s","5")
        f.write(helperFive)
        f.write(" ")
        f.write(helperSix)
        f.write(" ")
     
    
def enum(word):
    newWord = ""
    newerWord = ""
    for i in range(0,100):
        newWord =  word + str(i)
        f.write(newWord)
        f.write(" ")
        replacer(newWord)
        for j in range(0,9):
            if(j ==0):
                newerWord = newWord + "!"
            elif(j == 1):
                newerWord = newWord + "@"
            elif(j == 2): 
                newerWord = newWord + "#"
            elif(j == 1):
                newerWord = newWord + "$"
            elif(j == 3): 
                newerWord = newWord + "%"
            elif(j == 4):
                newerWord = newWord + "^"
            elif(j == 5): 
                newerWord = newWord + "&"
            elif(j == 6):
                newerWord = newWord + "*"
            elif(j == 7): 
                newerWord = newWord + "+"
            elif(j == 8):
                newerWord = newWord + "?"
            else: 
                newerWord = newWord + "~"
            f.write(newerWord)
            f.write(" ")
            replacer(newerWord)
    
        
        
def stringConvert(words):   
    reader = open(words,"r")
    maker = reader.readlines()
    for wording in maker:
        word = wording.rstrip()
        backWord = word[::-1]
        mirror = word + backWord
        twoWord = word + word
        threeWord = word+word+word
        twoBackwards = twoWord[::-1]
        threeBackwards = threeWord[::-1]
        twoLastCapBackwards= lastCap(twoBackwards)
        twoLastCapForwards = lastCap(twoWord)
        twoFirstCapBackwards = firstCap(twoBackwards) 
        twoFirstCapForwards = firstCap(twoWord)
        ThreeLastCapBackwards = lastCap(threeBackwards)
        ThreeLastCapForwards = lastCap(threeWord)
        ThreeFirstCapBackwards = firstCap(threeBackwards)
        ThreeFirstCapForwards = firstCap(threeWord)
        f.write(word)
        f.write(" ")
        f.write(backWord)
        f.write(" ")
        f.write(mirror)
        f.write(" ")
        f.write(twoWord)
        f.write(" ")
        f.write(threeWord)
        f.write(" ")
        f.write(twoBackwards)
        f.write(" ")
        f.write(threeBackwards)
        f.write(" ")
        f.write(twoLastCapBackwards)
        f.write(" ")
        f.write(twoLastCapForwards)
        f.write(" ")
        f.write(twoFirstCapBackwards)
        f.write(" ")
        f.write(twoFirstCapForwards)
        f.write(" ")
        f.write(ThreeLastCapBackwards)
        f.write(" ")
        f.write(ThreeFirstCapBackwards)
        f.write(" ")
        f.write(ThreeLastCapForwards)
        f.write(" ")
        f.write(ThreeFirstCapForwards)
        enum(word)
        enum(backWord)
        enum(mirror)
        enum(twoWord)
        enum(threeWord)
        enum(twoBackwards)
        enum(threeBackwards)
        enum(twoLastCapBackwards)
        enum(twoLastCapForwards)
        enum(twoFirstCapBackwards)
        enum(twoFirstCapForwards)
        enum(ThreeLastCapBackwards)
        enum(ThreeFirstCapBackwards)
        enum(ThreeLastCapForwards)
        enum(ThreeFirstCapForwards)
        f.write("\n")
       
       
reader = ("words.txt")
stringConvert(reader)
f.close()
