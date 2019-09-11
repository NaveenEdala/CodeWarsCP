# https://www.codewars.com/kata/555eded1ad94b00403000071

def series_sum(n):
    x = 1
    result = 0
    for i in range(n):
        result += (1/x)
        x += 3
    return '{:.2f}'.format(result)
