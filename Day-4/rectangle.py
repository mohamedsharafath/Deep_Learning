#cv2.rectangle(src,strt,end,color,thick)
cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

#cv2.putText(src,text,position,font,fontSize,clr,thick)
cv2.putText(img,text,(10,20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),2)

#srcimgcpy,contourRetrievalMode,contourApproximationMode
cv2.findContours(threshImg.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE

#cv2.dilate(src, kernel, iterations=1)
