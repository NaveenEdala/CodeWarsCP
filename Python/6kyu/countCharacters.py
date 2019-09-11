#https://www.codewars.com/kata/52efefcbcdf57161d4000091

def count(string):
    dictout = {}
    for letter in string:
        if (letter == " "):
            continue
        elif letter in dictout.keys():
            dictout[letter] += 1
        else:
            dictout[letter] = 1
            
    return dictout
