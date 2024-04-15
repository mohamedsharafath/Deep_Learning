import cv2
vs = cv2.VideoCapture(0)

while True:
    _,img=vs.read() #status,frame
    cv2.imshow("VideoStream",img)
    key=cv2.waitKey(1) & 0xFF
    if key == ord("q"):
               break
vs.release()
cv2.destroyAllWindows()
