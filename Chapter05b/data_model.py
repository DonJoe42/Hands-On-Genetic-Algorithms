# Bit overdone for a simple pickle operation, could be used for more complex operations later
import pickle
import tkinter


def var_array():
    """Constructs a 9x9 list with string vars"""
    print('grid function called')
    var_grid = list()
    for i in range(9):
        var_row = list()
        for j in range(9):
            var = tkinter.StringVar()
            var_row.append(var)
        var_grid.append(var_row)
    return var_grid


def save_data(data, name):
    pickle.dump(data, name)


def load_data(name):
    data = pickle.load(name)
    return data
