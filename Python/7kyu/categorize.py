# https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa

def openOrSenior(data):
    outputlist = []
    for pair in data:
        if pair[0] >= 55 and pair[1] > 7:
            outputlist.append("Senior")
        else:
            outputlist.append("Open")
    return outputlist
