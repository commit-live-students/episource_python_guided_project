# %load q01_load_data/build.py


path = 'data/episource.txt'


# def q01_load_data():
fname = path
 

def q01_load_data(path):
    num_words = 0
    with open(path, 'r') as f:
        for line in f:
            words = line.split()
            num_words += len(words)
    return f,num_words
q01_load_data(path)


