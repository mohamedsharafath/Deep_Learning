import cv2
img = cv2.imread("Sample1.jpeg")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#dst=cv2.threshold(src,threshold,maxvalueforThreshold,binary,type)[1] ---(0-255)
thresImg=cv2.threshold(gray,180,255,cv2.THRESH_BINARY)[1]
cv2.imwrite("ThresholdImg.jpg",thresImg)
