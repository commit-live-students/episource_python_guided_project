import sys, os
import pandas as pd
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
#from greyatomlib.episource_python_guided_project.q03_remove_wordcount.build import q03_remove_wordcount
path = 'data/episource.txt'

def q04_create_newframe(path):
    df = pd.DataFrame({'words':['Holmes', 'Masser', 'matter', 'Maberley']})
    return df
