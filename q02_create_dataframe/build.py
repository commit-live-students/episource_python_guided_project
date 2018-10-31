# %load q02_create_dataframe/build.py

import sys, os
# sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
import pandas as pd
import re
from collections import Counter
from greyatomlib.episource_python_guided_project.q01_load_data.build import q01_load_data
path = 'data/episource.txt'

def q02_create_dataframe(path):
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
    dff = pd.DataFrame({'name':keys[1:],'count':values[1:]})
    return dff




