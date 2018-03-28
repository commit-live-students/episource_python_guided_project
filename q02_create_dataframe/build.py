import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
import pandas as pd
import re
from collections import Counter
from greyatomlib.episource_python_guided_project.q01_load_data.build import q01_load_data
path = 'data/episource.txt'


def q02_create_dataframe(path):
    data, wordcount = q01_load_data(path)
    regex = re.compile('[^a-zA-Z]')
    text = regex.sub(' ', data)
    cnt = Counter(text.split())
    return pd.DataFrame(list(cnt.items()), columns=['words', 'count'])
