import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from greyatomlib.episource_python_guided_project.q02_create_dataframe.build import q02_create_dataframe
path = 'data/episource.txt'


def q03_remove_wordcount(path):
    df =q02_create_dataframe(path)
    return df[df['count'] >= 5]
