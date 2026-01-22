
import cv2
import numpy as np

from util import get_limits
from PIL import  Image
yellow=[0,255,255]#BGR

cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()

    hsvImage=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lowerLimit,upperLimit=get_limits(color=yellow)

    mask=cv2.inRange(hsvImage,lowerLimit,upperLimit)
    if np.any(mask!=0):
        print(mask)
    # mask_=Image.fromarray(mask)

    # bbox=mask_.getbbox()

    # if bbox is not None:
    #     x1,y1,x2,y2=bbox
    #     frame=cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),5)

    mask = cv2.erode(mask, None, iterations=2)
    #ERODE函数解释：None默认采用opencv3*3的判断窗口，即每次判断3*3大小的像素（就是9个像素点），根据外围8个来判断中心是置为0还是1（白），
    # 只有其余全为1，中心才为1，否则就置为0.
    # iterations表示这个判断窗口在全局遍历次数，一般1-2次

    mask = cv2.dilate(mask, None, iterations=2)
    # dilate函数解释：类似于erode，其余八个只要有一个为白，中心就置为白色1
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        # 过滤掉太小的噪点（比如背景里的黄色杂色）
        if cv2.contourArea(contour) < 400:
            continue

        # 获取外接矩形 (x, y, w, h)
        x, y, w, h = cv2.boundingRect(contour)

        # 画框
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 5)
    print(frame.shape)
    cv2.putText(frame, 'this is yyf', (20, 100), cv2.FONT_HERSHEY_TRIPLEX, 2, (255, 0, 255), 2)
    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xff==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
