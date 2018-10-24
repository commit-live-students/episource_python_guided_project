

path = 'data/episource.txt'

def q01_load_data(path):
    with open(path, mode='r') as f:
        data = f.read()

    return data, len(data.split())
