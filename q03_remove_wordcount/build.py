import sys, os
import string
import numpy as np
import pandas as pd
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
#from greyatomlib.episource_python_guided_project.q02_create_dataframe.build import q02_create_dataframe
path = 'data/episource.txt'


def q03_remove_wordcount(path):
    data = open(path, 'r')
    ans = []
    for line in data:
        for word in line.translate(None, string.punctuation).split():
            ans.append(word)

    na = np.unique(ans, return_counts=True)
    d = {'words':na[0], 'counts':na[1]}
    df = pd.DataFrame(d)
    df1 = df[df['counts'] > 3]
    df2 = df1.iloc[56:,:]
    return df2
