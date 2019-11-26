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
    under_exposed = cv2.imread("underexposed_img_hist_eql.jpg")
    plot_histogram(under_exposed, "underexposed_plot")
    over_exposed = cv2.imread("overexposed_img_hist_eql.jpg")
    plot_histogram(over_exposed, "overexposed_plot")


def histogram_equalization(path, filename):
    src = cv2.imread(path, 0)
    img = cv2.equalizeHist(src)
    cv2.imwrite(filename + '_img_hist_eql.jpg', img)


def hist_equalizer():
    overexposed = '../image-gamma-transformation/gamma_transposed_overexpose.jpg'
    histogram_equalization(overexposed, 'overexposed')
    underexposed = '../image-gamma-transformation/gamma_transposed_underexpose.jpg'
    histogram_equalization(underexposed, 'underexposed')


hist_equalizer()
histogram()
