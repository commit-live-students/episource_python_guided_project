# %load q02_create_dataframe/build.py
import sys, os
#sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
import pandas as pd
import re
from collections import Counter
from greyatomlib.episource_python_guided_project.q01_load_data.build import q01_load_data
path = 'data/episource.txt'


def q02_create_dataframe(path):
    file=open(path,'rt')
    text=file.read()
    file.close()
    words=re.split('[^a-zA-Z]',text)
    dic_result = Counter(words)
    data = list(dic_result)[1:]
    keys = list(dic_result.keys())
    values = list(dic_result.values())
    return pd.DataFrame({'name':keys[1:],'count':values[1:]})

q02_create_dataframe(path).shape


