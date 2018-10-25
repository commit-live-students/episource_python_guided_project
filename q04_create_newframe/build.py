# %load q04_create_newframe/build.py
import sys, os
# sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from greyatomlib.episource_python_guided_project.q03_remove_wordcount.build import q03_remove_wordcount
path = 'data/episource.txt'


df = q03_remove_wordcount(path)
def q04_create_newframe(path):
    features = df['words']
    expected =  ['Holmes', 'Masser', 'matter', 'Maberley']
    return features,expected



