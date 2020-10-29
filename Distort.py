# Work in progress. Plan is to distort an image according to a "shift" function.
# This program is currently in an incomplete stage.

# import numpy as np
# import sys
# import numba
# from imageio import imread, imwrite
# from scipy.ndimage.filters import convolve
# from tqdm import trange

import scipy.misc
import numpy as np
import matplotlib.pyplot as plt

img = scipy.misc.lena() # Error

A = img.shape[0] / 3.0
w = 2.0 / img.shape[1]

shift = lambda x: A * np.sin(2.5*np.pi*x * w)

for i in range(img.shape[0]):
    img[:,i] = np.roll(img[:,i], int(shift(i)))

plt.imshow(img, cmap=plt.cm.gray)
plt.show()

# This program is meant to be run from the command line.