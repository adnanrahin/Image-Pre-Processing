import cv2
import numpy as np

inputImage = cv2.imread('../ImageData/overexpose.jpg')
inputImageGrayLevel = cv2.cvtColor(inputImage, cv2.COLOR_BGR2GRAY)
resizeImage = cv2.resize(inputImageGrayLevel, (1080, 1080))

w1 = np.array([1])
w2 = np.array([[0, 1 / 5, 0], [1 / 5, 1 / 5, 1 / 5], [0, 1 / 5, 0]])
w3 = np.array([[1 / 9, 1 / 9, 1 / 9], [1 / 9, 1 / 9, 1 / 9], [1 / 9, 1 / 9, 1 / 9]])

convolution1 = cv2.filter2D(inputImageGrayLevel, -1, w1)
convolution2 = cv2.filter2D(inputImageGrayLevel, -1, w2)
convolution3 = cv2.filter2D(inputImageGrayLevel, -1, w3)

width, height = inputImageGrayLevel.shape
vectorList = []
vectorPosition = []

for i in range(len(convolution1)):
    for j in range(len(convolution1)):
        vectorList.append([convolution1[i, j], convolution2[i, j], convolution3[i, j]])
        vectorPosition.append([i, j])
outputImage = np.zeros((width, width))

unsortedArray = np.array(vectorList)
vectorList.sort()
sortedArray = np.array(vectorList)


def getElementIndex(list1, element):
    return list1.index(element)


cv2.imshow("image.jpg", unsortedArray)
cv2.waitKey(0)
cv2.destroyAllWindows()
