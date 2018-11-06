import numpy as np
import cv2


lower_range_red = np.array([167, 100, 100], dtype=np.uint8)
upper_range_red = np.array([187, 255, 255], dtype=np.uint8)

cam=cv2.VideoCapture(0)

#Reduce Noise data
kernelOpen=np.ones((5,5))
kernelClose=np.ones((20,20))

font = cv2.FONT_HERSHEY_SIMPLEX


while 1:
    ret, img=cam.read()
    img=cv2.resize(img,(340,220))
    imgHSV= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(imgHSV,lower_range_red,upper_range_red)
    # Reduce Noise data
    #opening will remove all the dots randomly popping here and there and
    # closing will close the small holes that are present in the actual object
    maskOpen=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernelOpen)
    maskClose=cv2.morphologyEx(maskOpen,cv2.MORPH_CLOSE,kernelClose)

    maskFinal = maskClose
    _,conts, h = cv2.findContours(maskFinal.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    cv2.drawContours(img, conts, -1, (255, 0, 0), 3)
    for i in range(len(conts)):
        x, y, w, h = cv2.boundingRect(conts[i])
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.putText(img, str(i+1), (x, y + h), font, 1, (0, 255, 255))

    cv2.imshow("maskClose", maskClose)
    cv2.imshow("maskOpen", maskOpen)
    cv2.imshow("mask", mask)
    cv2.imshow("cam", img)
    cv2.waitKey(10)

