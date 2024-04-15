import cv2
img = cv2.imread("resume.png")
cv2.imwrite("resume.jpg",img)
cv2.imshow("image",img)     #image is name
cv2.waitKey(0)
cv2.destroyAllWindows()
