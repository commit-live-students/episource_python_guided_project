import numpy as np
import pandas as pd
path = 'data/episource.txt'
def q01_load_data(path):
    file = open(path, 'r')
    data = file.read()
    return data, len(data.split(" "))
print(q01_load_data(path))
