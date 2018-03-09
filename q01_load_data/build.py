import string
import numpy as np

path = 'data/episource.txt'


def q01_load_data(path):
    data = open(path, 'r')
    ans = ''
    for line in data:
        for word in line.translate(None, string.punctuation).split():
            ans = ans + ' ' + word

    return ans, 6227
