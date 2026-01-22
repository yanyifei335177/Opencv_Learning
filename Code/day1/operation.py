import os
import cv2

#resize
img=cv2.imread(os.path.join('.','data','image1.jpg'))
resized_img=cv2.resize(img,(918,532))
print(resized_img.shape)
cv2.imwrite(os.path.join('.','data','image1.jpg'),resized_img)
cv2.imshow('resized_img',resized_img)
cv2.waitKey(0)

# crop
# img=cv2.imread(os.path.join('.','data','image1.jpg'))
# print(img.shape)
#
# cropped_img=img[0:133,250:459]
# cv2.imshow('cropped_img',cropped_img)
# cv2.waitKey(0)
