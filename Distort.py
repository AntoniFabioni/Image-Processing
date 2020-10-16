# Work in progress. Plan is to distort an image in a cool way, maybe using fractals??

import numpy as np
import sys
import numba
from imageio import imread, imwrite
from scipy.ndimage.filters import convolve
from tqdm import trange

def F(x, y):
    print("F")