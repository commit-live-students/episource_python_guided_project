# %load q03_remove_wordcount/build.py
import sys, os
# sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from greyatomlib.episource_python_guided_project.q02_create_dataframe.build import q02_create_dataframe
path = 'data/episource.txt'
import re
from collections import Counter
import pandas as pd
def q03_remove_wordcount(path):
    file=open(path,'rt')
    text=file.read()
    file.close()
    # text=text.split()
    words=re.split('[^a-zA-Z]',text)
    af = Counter(words)
    df = list(af)
    df = df[1:]
    keys = list(af.keys())

    values = list(af.values())
    values
    dff = pd.DataFrame({'words':keys[1:],'count':values[1:]})
    return dff[dff['count']>=5]

c=q03_remove_wordcount(path)
c


