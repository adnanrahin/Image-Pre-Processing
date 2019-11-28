import cv2
import numpy as np
from matplotlib import pyplot as plt
from scipy.ndimage.filters import median_filter
import PIL
from spectral import *
import math
from laspy.file import File
import matplotlib as mpl
from skimage.filters import roberts, sobel


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


def sobel_kernel(path):
    img = cv2.imread(path)
    grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    sobel_edge = sobel(grayImage)
    fig = plt.figure(frameon=True, facecolor='gray')
    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)
    ax.imshow(sobel_edge, cmap='gray')
    plt.savefig('sobel_edge.png')


def robert_kernel(path):
    img = cv2.imread(path)
    grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    robert_edge = roberts(grayImage)
    fig = plt.figure(frameon=True, facecolor='gray')
    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)
    ax.imshow(robert_edge, cmap='gray')
    plt.savefig('robert_edge.png')


def first_order_derivative(path):
    sobel_kernel(path)
    robert_kernel(path)


def second_order_derivative(path):
    img = cv2.imread(path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.GaussianBlur(img, (5, 5), 0)
    laplacian_filter_img = cv2.Laplacian(img, cv2.CV_64F)
    img = np.array(laplacian_filter_img, dtype=np.uint8)
    img = PIL.Image.fromarray(img)
    img.save('laplacian_filter.jpg')


def un_sharp(path):
    img = cv2.imread(path)
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_image_mf = median_filter(gray_image, 1)
    lap = cv2.Laplacian(gray_image_mf, cv2.CV_64F)
    sharpedImage = gray_image - 0.7 * lap
    fig = plt.figure(frameon=True, facecolor='gray')
    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)
    ax.imshow(sharpedImage, cmap='gray')
    plt.savefig('un_sharped.png')


file_path = '../image-gamma-transformation/gamma_transposed_overexpose.jpg'
gaussian_filter(file_path)
box_filter(file_path)
second_order_derivative(file_path)
first_order_derivative(file_path)
un_sharp(file_path)
