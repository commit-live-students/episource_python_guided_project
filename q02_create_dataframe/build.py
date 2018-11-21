# %load q02_create_dataframe/build.py
import sys, os
# sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
import pandas as pd
import numpy as np
import re
from collections import Counter
from greyatomlib.episource_python_guided_project.q01_load_data.build import q01_load_data
path = 'data/episource.txt'

def q02_create_dataframe(path):
    data = q01_load_data(path)
    a = re.sub(r'[^a-zA-Z]',' ', data[0])
    b = Counter(a.split())
    df = pd.DataFrame(list(b.items()),columns=['words','count'] )
    return df
q02_create_dataframe(path)


