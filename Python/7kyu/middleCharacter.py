# https://www.codewars.com/kata/56747fd5cb988479af000028

def get_middle(s):
    x = len(s)
    a = len(s) // 2
    #b = len(s) / 2
    if x == 1:
        return s
    else:
        if x % 2 == 0:
            return s[a-1]+s[a]
        elif x % 2 != 0:
            return s[a]
