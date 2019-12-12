# https://www.codewars.com/kata/57ee99a16c8df7b02d00045f/

def flatten_and_sort(array):
    lol = []
    for elements in array:
        for subelements in elements:
            lol.append(subelements)
    return lol.sort()
