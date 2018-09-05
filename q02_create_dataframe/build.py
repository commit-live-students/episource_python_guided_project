import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.curdir))))
import pandas as pd
import re
from collections import Counter
from greyatomlib.episource_python_guided_project.q01_load_data.build import q01_load_data
path = 'data/episource.txt'


def q02_create_dataframe(path):
    "write your solution here"
    data = q01_load_data(path)

    # Use regex pattern to remove the non alphanumeric characters
    regex = re.compile('[^a-zA-Z]')
    regex_data = regex.sub(' ', data[0])
    words = Counter(regex_data.split())

    # Convert dictionary to dataframe
    df = pd.DataFrame(list(words.items()), columns=['words', 'count'])
    return df

q02_create_dataframe(path)
