# https://www.codewars.com/kata/586f6741c66d18c22800010a

def sequence_sum(begin_number, end_number, step):
    sumx = [i for i in range(begin_number, end_number+1, step)]
    return sum(sumx) if begin_number <= end_number else 0
