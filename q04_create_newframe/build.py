# %load q04_create_newframe/build.py
import sys, os
from greyatomlib.episource_python_guided_project.q03_remove_wordcount.build import q03_remove_wordcount
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
path = 'data/episource.txt'

def q04_create_newframe(path):
    df = q03_remove_wordcount(path)
    condition = (df['words'].str.len() > 5) & (df['count'] > 10)
    condition_df = df.loc[condition]
    # print (condition_df)
    return condition_df



