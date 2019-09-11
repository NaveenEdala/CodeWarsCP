# https://www.codewars.com/kata/57eb8fcdf670e99d9b000272

def high(x):
    dct = {}
    index = 0
    for i in 'abcdefghijklmnopqrstuvwxyz':
        index += 1
        dct[i] = index
    listsource = x.split()
    highest = ''
    highscore = 0
    for word in listsource:
        score = 0
        for letter in word:
            score += dct[letter]
        if score > highscore:
            highscore = score
            highest = word
    return highest
