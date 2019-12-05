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
    gamma_over_exposed = cv2.imread('../image-gamma-transformation/gamma_transposed_overexpose.jpg')
    plot_histogram(gamma_over_exposed, 'overexpose_gamma')
    gamma_under_exposed = cv2.imread('../image-gamma-transformation/gamma_transposed_underexpose.jpg')
    plot_histogram(gamma_under_exposed, 'underexpose_gamma')
    hist_eql_over_exposed = cv2.imread('../histogram-equalization/overexposed_img_hist_eql.jpg')
    plot_histogram(hist_eql_over_exposed, 'hist_eql_overexposed')
    hist_eql_under_exposed = cv2.imread('../histogram-equalization/underexposed_img_hist_eql.jpg')
    plot_histogram(hist_eql_under_exposed, 'hist_eql_underexposed')
    original_img = cv2.imread('../ImageData/kernel_overexpose.jpg')
    plot_histogram(original_img, 'original_img_histogram_matching')
    ref_img = cv2.imread('../ImageData/kernel_underexpose.jpg')
    plot_histogram(ref_img, 'ref_img_histogram_matching')
    hist_match_img = cv2.imread('../histogram-matching-using-kernel/histogram_matching_image.jpg')
    plot_histogram(hist_match_img, 'hist_match_img')
    over_Expose_image = cv2.imread('../ImageData/overexpose')
    plot_histogram(over_Expose_image, 'overexpose_source_img')
    under_expose_image = cv2.imread('../ImageData/underexpose')
    plot_histogram(under_expose_image, 'underexpose_source')


histogram()
