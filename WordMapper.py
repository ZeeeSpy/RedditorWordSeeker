import numpy as np

def mapwordstofile():
    d = {}
    i = 0
    with open("WordsToFind") as f:
        for line in f:
            d[line.rstrip()] = 0

    def save_obj(obj, name ):
        with open('obj/'+ name + '.pkl', 'wb') as f:
            pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)   
    np.save('WordMap.npy', d)
    print("Word Map Updated")