import numpy as np
import cv2
import PIL
from spectral import *
import math
from laspy.file import File
import matplotlib.pyplot as plt
import matplotlib as mpl


def histogram_matching(path):
    src = cv2.imread(path)
    gray_image = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

    w1 = np.array([1])
    w2 = np.array([[0, 1 / 5, 0], [1 / 5, 1 / 5, 1 / 5], [0, 1 / 5, 0]])
    w3 = np.array([[1 / 9, 1 / 9, 1 / 9], [1 / 9, 1 / 9, 1 / 9], [1 / 9, 1 / 9, 1 / 9]])
    convolution1 = cv2.filter2D(gray_image, -1, w1)
    convolution2 = cv2.filter2D(gray_image, -1, w2)
    convolution3 = cv2.filter2D(gray_image, -1, w3)

    width, height = gray_image.shape

    matrix = np.zeros((width, height, 3))

    for i in range(width):
        for j in range(height):
            matrix[i, j] = ([convolution1[i, j], convolution2[i, j], convolution3[i, j]])

    return np.array(matrix, dtype=np.uint8)


def histogram_():
    overexposed = histogram_matching('../ImageData/overexpose.jpg')
    img = PIL.Image.fromarray(overexposed)
    img.save('over_histogram_matching_image.png')
    underexposed = histogram_matching('../ImageData/underexpose.jpg')
    img = PIL.Image.fromarray(underexposed)
    img.save('under_histogram_matching_image.png')


histogram_()

