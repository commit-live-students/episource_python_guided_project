# %load q01_load_data/build.py


path = 'data/episource.txt'


def q01_load_data(path):
    file=open(path,'rt')
    text=file.read()
    file.close()
    length = len((text.split()))
    return text,length
q01_load_data(path)


