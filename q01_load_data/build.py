# %load q01_load_data/build.py

path = 'data/episource.txt'

def q01_load_data(path):
    file = open(path, 'r')
    data = file.read()
    length = len(data.split())
    return data, length

# q01_load_data(path)



