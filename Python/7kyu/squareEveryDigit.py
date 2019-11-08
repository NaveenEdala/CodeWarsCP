def square_digits(num):
    lol = ""
    for digit in str(num):
        lol += str(int(digit)**2)
    return int(lol)
