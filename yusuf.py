import cv2
import numpy as np
import matplotlib.pyplot as plt
png = cv2.imread("C:\\Users\\90501\\q7.jpg",cv2.IMREAD_GRAYSCALE)
if png is not None:
    hist = cv2.calcHist([png],[0],None,[256],[0,256])

    plt.hist(png.ravel(),256,[0,256])
    plt.xlabel('Piksel Değeri')
    plt.ylabel('Piksel Sayisi')
    plt.title('Gri Resim Histogrami')
    plt.show()
else:
    print("Resim bulunamadi.")