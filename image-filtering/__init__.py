import cv2
import numpy as np
from matplotlib import pyplot as plt
from scipy.ndimage.filters import median_filter
import PIL
from spectral import *
import math
from laspy.file import File
import matplotlib as mpl


def gaussian_filter(path):
    img = cv2.imread(path)
    gaussian_filter_img = cv2.GaussianBlur(img, (5, 5), 0)
    img = PIL.Image.fromarray(gaussian_filter_img)
    img.save('gaussian_filter.jpg')


def box_filter(path):
    img = cv2.imread(path)
    box_filter_img = cv2.boxFilter(img, -1, (4, 4))
    img = PIL.Image.fromarray(box_filter_img)
    img.save('box_filter.jpg')


def first_order_derivative(path):
    img = cv2.imread(path)


def second_order_derivative(path):
    img = cv2.imread(path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.GaussianBlur(img, (5, 5), 0)
    laplacian_filter_img = cv2.Laplacian(img, cv2.CV_64F)
    img = np.array(laplacian_filter_img, dtype=np.uint8)
    img = PIL.Image.fromarray(img)
    img.save('laplacian_filter.jpg')


file_path = '../image-gamma-transformation/gamma_transposed_overexpose.jpg'
gaussian_filter(file_path)
box_filter(file_path)
second_order_derivative(file_path)
