import os
import cv2
# print(cv2.__version__)

# # read image
# image_path=os.path.join('.','data','image1.jpg')
#
# img=cv2.imread(image_path)
#
# #write image
#
# cv2.imwrite(os.path.join('.','data','image1_out.jpg'),img)
#
# #visualize image
#
# cv2.imshow('image',img)
# cv2.waitKey(5000)


# #read video
# video_path=os.path.join('.','data','video1.mp4')
#
# video=cv2.VideoCapture(video_path)
#
# # #visualize VIDEO
#
# ret=True
# while ret:
#     ret,frame=video.read()
#     if ret:
#         cv2.imshow('frame',frame)
#         cv2.waitKey(25)
#
# video.release()
# cv2.destroyAllWindows()


#read webcam
webcam=cv2.VideoCapture(0)

#visualize webcam
while True:
    ret,frame=webcam.read()
    cv2.imshow('frame',frame)
    if cv2.waitKey(40) & 0xff == ord('q'):
        break

webcam.release()
cv2.destoryAllWindows()



