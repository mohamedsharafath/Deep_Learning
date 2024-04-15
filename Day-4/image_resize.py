import cv2
import imutils
img = cv2.imread("Sample1.jpeg")
resizeImg = imutils.resize(img,width=20)
cv2.imwrite("resizedimg1.jpeg",resizeImg)
