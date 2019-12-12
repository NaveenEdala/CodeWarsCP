# https://www.codewars.com/kata/54ff3102c1bad923760001f3

def getCount(inputStr):
    num_vowels = 0
    for letter in inputStr:
        if letter in "aeiou":
            num_vowels += 1
    return num_vowels
