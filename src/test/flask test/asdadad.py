import cv2
import numpy as np
import matplotlib.pyplot as plt


def showlmage():
    imgfile = 'images/model.png'
    img = cv2.imread(imgfile, cv2.IMREAD_GRAYSCALE)
    

    plt.imshow(img, cmap='gray', interpolation='bicubic')
    plt.xticks([])
    plt.yticks([])
    plt.title('model')
    plt.show()
   
showlmage()