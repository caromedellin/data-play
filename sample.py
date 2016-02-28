import scipy
import numpy as np

a = np.array([[1.0, 2.0], [3.0, 4.0]])

# this calls the sub package of  the numpy lib nad makes this in to the inverse array

np.linalg.inv(a)

# producto de matrices, but it's Ø of nˆ2, if you are given some input 
# length you need at least twice as much time in the worse case scenario
np.dot (a, a)
