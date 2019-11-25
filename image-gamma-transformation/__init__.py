import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import PIL
from spectral import *
import math
from laspy.file import File
import matplotlib.pyplot as plt
import matplotlib as mpl


def gamma_transformation(path, gamma):
    src = cv.imread(path)
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    gamma_transposed_img = np.array(255 * (gray / 255) ** gamma, dtype='uint8')
    img = PIL.Image.fromarray(gamma_transposed_img)
    fileName = path[13: len(path)]
    img.save('gamma_transposed' + fileName)


overexposed = '../ImageData/overexpose.jpg'
gamma_transformation(overexposed, 5)
overexposed_img = cv.imread('gamma_transposedoverexpose.jpg')
overexposed_histogram = cv.equalizeHist(overexposed_img)
plt.plot(overexposed_histogram)
plt.show()
