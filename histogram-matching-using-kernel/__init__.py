import numpy as np
import cv2
import PIL
from spectral import *
import math
from laspy.file import File
import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy.misc import *


def image_pixel_intensity(img):
    intensity_array = np.zeros(256)
    height, width = img.shape[0:2]

    for i in range(height):
        for j in range(width):
            intensity_array[img[i, j]] += 1

    return intensity_array


def hist_match(org_path, ref_path):
    original = cv2.imread(org_path)
    specified = cv2.imread(ref_path)

    img_shape = original.shape
    original = original.ravel()
    specified = specified.ravel()

    s_values, bin_idx, s_counts = np.unique(original, return_inverse=True, return_counts=True)
    t_values, t_counts = np.unique(specified, return_counts=True)

    s_quantiles = np.cumsum(s_counts).astype(np.float64)
    s_quantiles /= s_quantiles[-1]

    t_quantiles = np.cumsum(t_counts).astype(np.float64)
    t_quantiles /= t_quantiles[-1]

    sour = np.around(s_quantiles * 255)
    temp = np.around(t_quantiles * 255)

    b = []
    for data in sour[:]:
        b.append(find_nearest_above(temp, data))
    b = np.array(b, dtype='uint8')

    return b[bin_idx].reshape(img_shape)


def find_nearest_above(my_array, target):
    diff = my_array - target
    mask = np.ma.less_equal(diff, -1)

    if np.all(mask):
        c = np.abs(diff).argmin()
        return c
    masked_diff = np.ma.masked_array(diff, mask)
    return masked_diff.argmin()


def histogram_matching(original_img_path, ref_img_path):
    org_src = hist_match(original_img_path, ref_img_path)
    img = PIL.Image.fromarray(np.array(org_src, dtype='uint8'))
    img.save('image.jpg')
    src = cv2.imread('image.jpg')
    source_img_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    height, width = org_src.shape[0:2]

    w1 = np.array([1])
    w2 = np.array([[0, 1 / 5, 0], [1 / 5, 1 / 5, 1 / 5], [0, 1 / 5, 0]])
    w3 = np.array([[1 / 9, 1 / 9, 1 / 9], [1 / 9, 1 / 9, 1 / 9], [1 / 9, 1 / 9, 1 / 9]])

    convolution1 = cv2.filter2D(source_img_gray, -1, w1)
    convolution2 = cv2.filter2D(source_img_gray, -1, w2)
    convolution3 = cv2.filter2D(source_img_gray, -1, w3)

    matrix = np.zeros((height, width, 3))

    for i in range(height):
        for j in range(width):
            vector = ([convolution1[i, j], convolution2[i, j], convolution3[i, j]])
            vector.sort()
            matrix[i, j] = vector

    return np.array(matrix, dtype=np.uint8)


def histogram_():
    overexposed = histogram_matching('../ImageData/kernel_overexpose.jpg', '../ImageData/kernel_underexpose.jpg')
    img = PIL.Image.fromarray(overexposed)
    img.save('histogram_matching_image.jpg')


histogram_()
