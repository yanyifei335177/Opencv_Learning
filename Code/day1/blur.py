import os
import cv2

img=cv2.imread(os.path.join('.','data','image1.jpg'))

k_size=7
img_blur=cv2.blur(img,(k_size,k_size))
img_medianblur=cv2.medianBlur(img,k_size)
cv2.imshow('img',img)
cv2.imshow('img_blur',img_blur)
cv2.imshow('img_medianblur',img_medianblur)
cv2.waitKey(0)