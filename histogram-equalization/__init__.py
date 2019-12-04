import numpy as np
import cv2
import PIL
from spectral import *
import math
from laspy.file import File
import matplotlib.pyplot as plt
import matplotlib as mpl


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
