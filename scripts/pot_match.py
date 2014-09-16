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
template = cv2.imread('rounded_square.jpg')
# cv2.imshow("input_image", input_image)

hsb_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2HSV)
H_channel,S_channel,hsB_channel = cv2.split(hsb_image)
cv2.imshow("S",S_channel)


#template = cv2.imread('mario_coin.png',0)
template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
cv2.imshow("template", template)
blurtemplate = cv2.bilateralFilter(template,9,100,100)
cv2.imshow("blur template", blurtemplate)
# w, h = template.shape[::-1]

blur = cv2.bilateralFilter(S_channel,9,100,100)
cv2.imshow("blur", blur)

(T, thresh_image) = cv2.threshold(blur, 100, 120, cv2.THRESH_BINARY)
cv2.imshow("Threshold Binary", thresh_image)
canny_image = cv2.Canny(thresh_image, 100, 200, apertureSize = 3)
#canny_image = cv2.Canny(thresh_image, 51, 65)
cv2.imshow("Canny", canny_image)

kernel = np.ones((5,5),np.uint8)
dilation = cv2.dilate(canny_image,kernel,iterations = 2)
cv2.imshow("Canny dilation", dilation)


res = cv2.matchTemplate(dilation,blurtemplate,cv2.TM_CCOEFF_NORMED)
threshold = 0.4
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(input_image, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

cv2.imwrite('res.png',input_image)
cv2.waitKey(0)