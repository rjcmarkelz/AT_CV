#########
# Cody Markelz
# April 26, 2016
# markelz@gmail.com
# github, twitter, bitbucket: rjcmarkelz
#########
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
lab_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2LAB)
l_channel,a_channel,b_channel = cv2.split(lab_image)
(aT, a_thresh_image) = cv2.threshold(a_channel, 110, 130, cv2.THRESH_BINARY)
# cv2.imshow("a_channel Threshold Binary", a_thresh_image)
# cv2.imwrite('output.tif', a_thresh_image)


# threshold image based on a_channel region that provides the most contrast
(aT, a_thresh_image) = cv2.threshold(a_channel, 110, 130, cv2.THRESH_BINARY)
# cv2.imshow("a_channel Threshold Binary", a_thresh_image)
# cv2.imwrite('output.tif', a_thresh_image)

dst = cv2.inRange(a_thresh_image, 110, 130)
no_black = cv2.countNonZero(dst)
black_pixels = a_thresh_image.size - no_black
# print('The number of black pixels is: ' + str(no_black))
# print(a_thresh_image.size - str(no_black))
print(args["image"] + str(black_pixels))
# cv2.waitKey(0)

# END SCRIPT
