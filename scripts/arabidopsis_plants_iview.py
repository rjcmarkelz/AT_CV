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
import os

root_dir = '.'

for files in os.walk(root_dir):
    for file in files:
        print file

# get some info from the user
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
    help = "Path to the image")
args = vars(ap.parse_args())
# Load the image and display it

# files_in_dir = os.listdir(inputdir)
# for file_in_dir in files_in_dir:

input_image = cv2.imread(args["image"])

hsb_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2HSV)
H_channel,S_channel,hsB_channel = cv2.split(hsb_image)
lab_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2LAB)
l_channel,a_channel,b_channel = cv2.split(lab_image)
(aT, a_thresh_image) = cv2.threshold(a_channel, 110, 130, cv2.THRESH_BINARY)
cv2.imshow("a_channel Threshold Binary", a_thresh_image)
cv2.imwrite('output.tif', a_thresh_image)

dst = cv2.inRange(a_thresh_image, 110, 130)
no_black = cv2.countNonZero(dst)
print('The number of black pixels is: ' + str(no_black))
# cv2.imshow("H",H_channel)
# cv2.imshow("S",S_channel)
# cv2.imshow("hsB",hsB_channel)

# Convert original image to the L*a*b* color space for arabidopsis detection

#cv2.imshow("L",l_channel)
cv2.imshow("a",a_channel) # focus on a channel because it provides best contrast for arabidopsis
#cv2.imshow("b",b_channel)


#########
#########
#########
# rosette detection
#########
#########
#########

# take a look at the a_channel histogram
# hist = cv2.calcHist([a_channel], [0], None, [256], [0, 256])
# # Plot the histogram
# plt.figure()
# plt.title("a Histogram")
# plt.xlabel("Bins")
# plt.ylabel("# of Pixels")
# plt.plot(hist)
# plt.xlim([0, 256])
# plt.show()
# cv2.waitKey(0)

# threshold image based on a_channel region that provides the most contrast
(aT, a_thresh_image) = cv2.threshold(a_channel, 110, 130, cv2.THRESH_BINARY)
cv2.imshow("a_channel Threshold Binary", a_thresh_image)
cv2.imwrite('output.tif', a_thresh_image)

dst = cv2.inRange(a_thresh_image, 110, 130)
no_black = cv2.countNonZero(dst)
print('The number of black pixels is: ' + str(no_black))

#a_thresh_image2 = a_thresh_image.copy()
# cv2.imshow("a_thresh_2",a_thresh_image2)
# cv2.imwrite('output.tif', a_thresh_image)
# a_thresh_image2 = cv2.imread("output.tif")
# cv2.imshow("a_channel Threshold Binary 2", a_thresh_image2)
# dst = cv2.addWeighted(a_thresh_image2,0.9, input_image,0.5,0)

# dst2 = dst.copy()
# for x1,y1,x2,y2 in linesP[0]:
#     cv2.line(dst2,(x1,y1),(x2,y2), (0,255,0) ,2)

# cv2.imshow("blended", dst)
# cv2.imshow("blended2", dst2)
cv2.waitKey(0)

# END SCRIPT
