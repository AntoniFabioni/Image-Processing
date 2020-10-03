# Work in progress. Plan is to distort an image in a cool way.

import numpy as np
import sys
import numba
from imageio import imread, imwrite
from scipy.ndimage.filters import convolve
from tqdm import trange