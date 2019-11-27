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
    gaussian_filter_img = cv2.GaussianBlur(img, (3, 3), 0)
    img = PIL.Image.fromarray(gaussian_filter_img)
    img.save('gaussian_filter.jpg')


def box_filter(path):
    img = cv2.imread(path)
    box_filter_img = cv2.boxFilter(img, -1, (10, 10))
    img = PIL.Image.fromarray(box_filter_img)
    img.save('box_filter.jpg')


def first_order_derivative(path):
    img = cv2.imread(path)


def second_order_derivative(path):
    img = cv2.imread(path)


file_path = '../image-gamma-transformation/gamma_transposed_overexpose.jpg'
gaussian_filter(file_path)
box_filter(file_path)
