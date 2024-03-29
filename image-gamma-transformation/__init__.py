import numpy as np
import cv2
import PIL
from spectral import *
import math
from laspy.file import File
import matplotlib.pyplot as plt
import matplotlib as mpl


def gamma_transformation(path, gamma):
    src = cv2.imread(path)
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    gamma_transposed_img = np.array(255 * (gray / 255) ** gamma, dtype='uint8')
    img = PIL.Image.fromarray(gamma_transposed_img)
    fileName = path[13: len(path)]
    img.save('gamma_transposed_' + fileName)


def transpose():
    overexposed = '../ImageData/overexpose.jpg'
    gamma_transformation(overexposed, 5.5)
    underexposed = '../ImageData/underexpose.jpg'
    gamma_transformation(underexposed, 0.369)


transpose()
