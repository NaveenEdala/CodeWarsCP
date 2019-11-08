# http://www.codewars.com/kata/546e2562b03326a88e000020/train/python

def square_digits(num):
    lol = ""
    for digit in str(num):
        lol += str(int(digit)**2)
    return int(lol)
