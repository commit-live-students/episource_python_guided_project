# %load q03_remove_wordcount/build.py
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.curdir))))
from greyatomlib.episource_python_guided_project.q02_create_dataframe.build import q02_create_dataframe
path = 'data/episource.txt'


def q03_remove_wordcount(data):
    
    df = q02_create_dataframe(data)
    df_1 = df[df['count'] >= 5] 
    return df_1#.shape
    
q03_remove_wordcount(path)
df = q02_create_dataframe(path)
df_1 = df[df['count'] >= 5]
df_1.shape


