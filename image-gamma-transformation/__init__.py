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
    img = PIL.Image.open(plot_title + '.png')
    img.show()


def histogram():
    under_exposed = cv2.imread("gamma_transposed_overexpose.jpg")
    plot_histogram(under_exposed, "underexposed_plot")
    over_exposed = cv2.imread("gamma_transposed_underexpose.jpg")
    plot_histogram(over_exposed, "overexposed_plot")


def gamma_transformation(path, gamma):
    src = cv2.imread(path)
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    gamma_transposed_img = np.array(255 * (gray / 255) ** gamma, dtype='uint8')
    img = PIL.Image.fromarray(gamma_transposed_img)
    fileName = path[13: len(path)]
    img.save('gamma_transposed_' + fileName)
    histogram()


def transpose():
    overexposed = '../ImageData/overexpose.jpg'
    gamma_transformation(overexposed, 5.5)
    underexposed = '../ImageData/underexpose.jpg'
    gamma_transformation(underexposed, 0.369)


transpose()
