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
    box_filter_img = cv2.boxFilter(img, -1, (1, 1))
    img = PIL.Image.fromarray(box_filter_img)
    img.save('box_filter.jpg')


file_path = '../ImageData/overexpose.jpg'
gaussian_filter(file_path)
box_filter(file_path)
