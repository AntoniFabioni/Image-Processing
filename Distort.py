'''
Work in progress. Distorts an image (e.g. jpg, png) according to a "shift" function.
'''

# import sys
# import numba
# from imageio import imread, imwrite
# from scipy.ndimage.filters import convolve
# from tqdm import trange

import scipy.misc
import numpy as np
import matplotlib.pyplot as plt

img = scipy.misc.lena() # Error...no attribute 'lena'??
# Replace with another image?vs

A = img.shape[0] / 3.0
w = 2.0 / img.shape[1]

k = 6

shift = lambda x: A * np.sin(k*np.pi*x * w)

for i in range(img.shape[0]):
    img[:,i] = np.roll(img[:,i], int(shift(i)))

def modify(image, function):
    pass

plt.imshow(img, cmap=plt.cm.gray)
plt.show() # Maybe make file instead of showing image??

# def main():
#     scale = float(sys.argv[1])   # This should be 'k'.
#     in_filename = sys.argv[2]
#     out_filename = sys.argv[3]

#     img = imread(in_filename)
#     out = crop_c(img, scale)
#     imwrite(out_filename, out)

# if __name__ == '__main__':
#     main()