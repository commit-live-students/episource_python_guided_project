# %load q01_load_data/build.py
import pandas as pd
import numpy as np

path = 'data/episource.txt'


def q01_load_data(path):
    num_words = 0
    with open(path, 'r') as f:
        data = f.read()
    with open(path, 'r') as f:
        for line in f:
            words = line.split()
            num_words += len(words)
    return data,num_words
