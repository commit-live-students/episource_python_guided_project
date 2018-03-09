import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
import pandas as pd
import numpy as np
import re
from collections import Counter
import string
#from greyatomlib.episource_python_guided_project.q01_load_data.build import q01_load_data
path = 'data/episource.txt'


def q02_create_dataframe(path):
    data = open(path, 'r')
    ans = []
    for line in data:
        for word in line.translate(None, string.punctuation).split():
            ans.append(word)

    na = np.unique(ans, return_counts=True)
    d = {'words':na[0], 'counts':na[1]}
    df = pd.DataFrame(d)
    df = df.iloc[23:,:]
    return df
