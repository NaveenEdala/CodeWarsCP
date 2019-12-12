# http://www.codewars.com/kata/54bf85e3d5b56c7a05000cf9/train/python

def number(lines):
    lol = []
    for i in range(len(lines)):
        lol.append(str(i+1) + ": " + lines[i])
    return lol
