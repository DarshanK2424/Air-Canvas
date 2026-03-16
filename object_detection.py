import cv2


capture=cv2.VideoCapture(0)

cv2.namedWindow("Frame",cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("Frame",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)

prev_x,prev_y=0,0
canvas=None
while True:

   
    ret,frame=capture.read()
    if not ret:
        break
    
    frame=cv2.flip(frame,1)
    if canvas is None:
        canvas=frame.copy()*0

    key=cv2.waitKey(1)

    if key==ord('c'):
        canvas=frame.copy()*0
        prev_x,prev_y=0,0

    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lower_val=(100,150,50)
    higher_val=(140,255,255)

    mask=cv2.inRange(hsv,lower_val,higher_val)
    
    contours,_=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        largest=max(contours,key=cv2.contourArea)

        M=cv2.moments(largest)

        if M["m00"]!=0:
            cx=(int)(M["m10"]/M["m00"])
            cy=(int)(M["m01"]/ M["m00"])


            
            if prev_x==0 and prev_y==0:
                prev_x,prev_y=cx,cy

        
            cv2.circle(frame,(cx,cy),8,(0,0,255),-1)
            cv2.line(canvas,(prev_x,prev_y),(cx,cy),(0,255,255),2)

            prev_x,prev_y=cx,cy

        cv2.drawContours(frame,[largest],-1,(0,255,0),2)

    frame=cv2.add(frame,canvas)   
    
    cv2.imshow("Frame",frame)
    # cv2.imshow("Mask",mask)

    
    

    if key==ord('q'):
        break

capture.release()
cv2.destroyAllWindows()