# https://www.codewars.com/kata/54e6533c92449cc251001667

def unique_in_order(iterable):
    listx = ['lol']
    for element in iterable:
        if element == listx[len(listx)-1]:
            continue
        else:
            listx.append(element)
    listx.remove('lol')
    return listx
