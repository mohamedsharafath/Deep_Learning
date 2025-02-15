import imutils
import cv2

redLower = (78,50,150)
redUpper = (179,255,255)

cam=cv2.VideoCapture(0)

while True:
    _,frame=cam.read()

    frame = imutils.resize(frame,width=600)


    blur=cv2.GaussianBlur(frame,(11,11),0)

    hsv = cv2.cvtColor(blur,cv2.COLOR_BGR2HSV)

    mask=cv2.inRange(hsv,redLower,redUpper)
    mask=cv2.erode(mask,None,iterations=2)
    mask=cv2.dilate(mask,None,iterations=2)

    cnts=cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
    center=None

    if len(cnts) > 0:
        c=max(cnts,key=cv2.contourArea)
        ((x,y),radius)=cv2.minEnclosingCircle(c)        #values of circle
        M=cv2.moments(c)
        center=(int(M["m10"]/M["m00"]),int(M["m01"]/M["m00"]))  #center of object
        if radius>10:
            cv2.circle(frame,(int(x),int(y)),int(radius),(0,255,255),2)
            cv2.circle(frame,center,5,(0,0,255),-1)
            if radius>250:
                print("stop")
            else:
                if(center[0]<150):      #center(x,y)
                    print("left")
                elif(center[0]>450):
                    print("right")
                elif(radius<250):
                    print("front")
                else:
                    print("stop")
    cv2.imshow("frame",frame)
    key=cv2.waitKey(1) & 0xFF
    if key==ord("q"):
        break

cam.release()
cv2.destroyAllWindows()
                
