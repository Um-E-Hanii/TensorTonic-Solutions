import numpy as np

def dot_product(x, y):
    c = 0
    for i in range(len(x)):
        c=c+(x[i]*y[i])
        if len(x) != len(y):
            raise ValueError
    return c 