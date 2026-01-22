import os
import cv2
img=cv2.imread(os.path.join('.','data','chalkboard.png'))

print(img.shape)

#line
cv2.line(img,(100,200),(300,500),(0,255,0),3)
cv2.line(img,(300,500),(400,500),(255,255,0),3)
cv2.line(img,(400,500),(100,200),(255,255,255),3)
#rectangle
cv2.rectangle(img,(500,150),(600,500),(255,0,0),3)
#circle
cv2.circle(img,(800,150),150,(0,0,0),3)
#text
cv2.putText(img,'hey you!!!',(800,450),cv2.FONT_HERSHEY_TRIPLEX,2,(255,0,255),2)

cv2.imshow('img',img)
cv2.waitKey(0)