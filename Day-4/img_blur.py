import cv2
img = cv2.imread("Sample1.jpeg")
gaussianBlurImg=cv2.GaussianBlur(img,(11,11),0) #kernel(odd),bordertype 
cv2.imshow("gaussianImg1.jpg",gaussianBlurImg)
