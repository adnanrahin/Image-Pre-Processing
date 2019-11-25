import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import PIL
from spectral import *
import math
from laspy.file import File
import matplotlib.pyplot as plt
import matplotlib as mpl


def histogram(path, filename):
    src = cv.imread(path, 0)
    img = cv.equalizeHist(src)
    cv.imwrite(filename + '_img_hist.jpg', img)


overexposed = '../image-gamma-transformation/gamma_transposed_overexpose.jpg'
histogram(overexposed, 'overexposed')
underexposed = '../image-gamma-transformation/gamma_transposed_underexpose.jpg'
histogram(underexposed, 'underexposed')
