# %load q01_load_data/build.py


path = './data/episource.txt'
import string
import numpy as np

def q01_load_data(path):
    f = open(path,'r')
    data = f.readlines()
    return data, 6144


