import cv2
import numpy as np
from matplotlib import pyplot as plt
import argparse

# get some info from the user
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
	help = "Path to the image")
args = vars(ap.parse_args())
# Load the image and display it
input_image = cv2.imread(args["image"])

hsb_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2HSV)
H_channel,S_channel,hsB_channel = cv2.split(hsb_image)
# cv2.imshow("S",S_channel)

blur = cv2.bilateralFilter(S_channel,9,100,100)
# cv2.imshow("blur", blur)

(T, thresh_image) = cv2.threshold(blur, 100, 120, cv2.THRESH_BINARY)
# cv2.imshow("Threshold Binary", thresh_image)
canny_image = cv2.Canny(thresh_image, 100, 200, apertureSize = 3)
# cv2.imshow("Canny", canny_image)

kernel = np.ones((10,10),np.uint8)
dilation = cv2.dilate(canny_image,kernel,iterations = 1)
cv2.imshow("Canny dilation", dilation)

lines = cv2.HoughLines(dilation,1,np.pi/180,200)

# print lines
input_copy1 = input_image.copy()
input_copy2 = input_image.copy()

for rho,theta in lines[0]:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))
    cv2.line(input_copy1,(x1,y1),(x2,y2),(0,0,255),2)
cv2.imshow("input_copy1",input_copy1)

minLineLength = 10000
maxLineGap = 100
lines = cv2.HoughLinesP(dilation,1,np.pi/180,100,minLineLength,maxLineGap)
print lines
for x1,y1,x2,y2 in lines[0]:
    cv2.line(input_copy2,(x1,y1),(x2,y2),(0,255,0),2)
cv2.line(input_copy2,(5,70),(11,384),(0,0,255),2)
cv2.imshow("input_copy2",input_copy2)

# cv2.imwrite('houghlines.jpg',in)

# cv2.imwrite('houghlinesP.jpg',input_copy2)


cv2.waitKey(0)