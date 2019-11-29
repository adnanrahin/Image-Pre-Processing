import numpy as np
import cv2
import PIL
from spectral import *
import math
from laspy.file import File
import matplotlib.pyplot as plt
import matplotlib as mpl


def calculate_histogram(source, bands):
    width, height = source.shape[0:2]
    histogram = np.zeros(256)
    for i in range(height):
        for j in range(width):
            vector = source[j, i]
            if bands == 3:
                average = (int(vector[0]) + int(vector[1]) + int(vector[2])) / 3
                histogram[int(average)] += 1
            else:
                histogram[vector[bands]] += 1

    return np.array(histogram)


def plot_histogram(img_matrix, plot_title):
    color = ('r', 'g', 'b', 'k')
    for i in range(0, len(color)):
        hist = calculate_histogram(img_matrix, i)
        plt.plot(hist, color=color[i])

    plt.title(plot_title)
    plt.savefig(plot_title + ".png")
    plt.close()


def histogram():
    under_exposed = cv2.imread("under_histogram_matching_image.png")
    plot_histogram(under_exposed, "underexposed_plot")
    over_exposed = cv2.imread("over_histogram_matching_image.png")
    plot_histogram(over_exposed, "overexposed_plot")


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
    histogram()


histogram_()
