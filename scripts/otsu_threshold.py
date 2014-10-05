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

kernel = np.ones((5,5),np.uint8)
dilation = cv2.dilate(canny_image,kernel,iterations = 2)
cv2.imshow("Canny dilation", dilation)

# Otsu's thresholding after Gaussian filtering
(ret3,th3) = cv2.threshold(dilation,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow("OTSU", th3)
cv2.waitKey(0)