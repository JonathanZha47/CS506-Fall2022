from cgitb import reset
import numpy as np
from numpy.linalg import norm


def euclidean_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)

def manhattan_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])
    return res

def jaccard_dist(x, y):
    intersection = len(list(set(x).intersection(y)))
    union = (len(x) + len(y)) - intersection
    return float(intersection) / union

def cosine_sim(x, y):
    cosine = np.dot(x,y)/(norm(x)*norm(y))
    return cosine

# Feel free to add more
