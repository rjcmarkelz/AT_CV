#########
# Cody Markelz
# September 18, 2014
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
height, width, depth = input_image.shape

#convert image to HSV colorspace for pot detection
hsb_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2HSV)
H_channel,S_channel,hsB_channel = cv2.split(hsb_image)
# cv2.imshow("H",H_channel)
# cv2.imshow("S",S_channel)
# cv2.imshow("hsB",hsB_channel)

# Convert original image to the L*a*b* color space for arabidopsis detection
lab_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2LAB)
l_channel,a_channel,b_channel = cv2.split(lab_image)
#cv2.imshow("L",l_channel)
# cv2.imshow("a",a_channel) # focus on a channel because it provides best contrast for arabidopsis
#cv2.imshow("b",b_channel)


# canvas = np.zeros((300, 300, 3), dtype = "uint8")
# green = (0, 255, 0)
# cv2.line(canvas, (0, 0), (300, 300), green)
# cv2.line("l_channel line", canvas)
# cv2.waitKey(0)


#########
#########
#########
# Pot identification
#########
#########
#########

# take a look at the H channel histogram for pot detection, uncomment when finding correct threshold
# hist = cv2.calcHist([H_channel], [0], None, [256], [0, 256])

# Plot the histogram
# plt.figure()
# plt.title("H Histogram")
# plt.xlabel("Bins")
# plt.ylabel("# of Pixels")
# plt.plot(hist)
# plt.xlim([0, 256])
# plt.show()
# cv2.waitKey(0)

# blur image to get better edges
blur = cv2.bilateralFilter(S_channel, 9, 100, 100)
#cv2.imshow("blur", blur)

# hist = cv2.calcHist([blur], [0], None, [256], [0, 256])
# # Plot the histogram
# plt.figure()
# plt.title("blur Histogram")
# plt.xlabel("Bins")
# plt.ylabel("# of Pixels")
# plt.plot(hist)
# plt.xlim([0, 256])
# plt.show()
# cv2.waitKey(0)

# pick peaks to threshold around
(T, thresh_image) = cv2.threshold(blur, 75, 110, cv2.THRESH_BINARY)
# cv2.imshow("Threshold Binary", thresh_image)

# canny edge detection on the thresholded image
canny_image = cv2.Canny(thresh_image, 100, 200, apertureSize = 3)
# cv2.imshow("Canny", canny_image)

# set kernal to "Dilate" the lines from the canny image
# this step is necessary to bring out the edges of the pots
# play with the size of the array and the number of iterations for various results
kernel = np.ones((5,5), np.uint8)
dilation = cv2.dilate(canny_image, kernel, iterations = 2)
# cv2.imshow("Canny dilation", dilation)

# # print lines
input_copy2 = input_image.copy()

# set parameters for HoughLinesP 
# also play with these to get more or less numbers of lines
minLineLength = 100000
maxLineGap = 40
linesP = cv2.HoughLinesP(dilation, 1, np.pi/180, 100, minLineLength, maxLineGap)

# extract endpoints and draw HoughLines
for x1,y1,x2,y2 in linesP[0]:
    cv2.line(input_copy2,(x1,y1),(x2,y2), (0,255,0) ,2)

# cv2.imshow("inputcopy2", input_copy2)

canvas = np.zeros((height, width, 3), dtype = "uint8")
test = input_image.copy()
lines = cv2.HoughLines(dilation, 1, np.pi/180, 600)
for rho, theta in lines[0]:
	a = np.cos(theta)
	b = np.sin(theta)
	x0 = a*rho
	y0 = b*rho
	x1 = int(x0 + 1000*(-b))
	y1 = int(y0 + 1000*(a))
	x2 = int(x0 - 1000*(-b))
	y2 = int(y0 - 1000*(a))

	cv2.line(canvas, (x1, y1), (x2, y2), (255, 0, 0), 20)

cv2.imshow("blended6", canvas)


gray = cv2.cvtColor(canvas,cv2.COLOR_BGR2GRAY)
dst5 = cv2.cornerHarris(gray,2,3,0.04)
cv2.imshow("gray", gray)


#result is dilated for marking the corners, not important
dst5 = cv2.dilate(dst5, None)

# Threshold for an optimal value, it may vary depending on the image.
canvas[dst5>0.01*dst5.max()]=[0,0,255]

cv2.imshow('dst5',canvas)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()

(cnts, _) = cv2.findContours(gray.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:10]
screenCnt = None
# loop over our contours
for c in cnts:
	peri = cv2.arcLength(c, True)
	approx = cv2.approxPolyDP(c, 0.02 * peri, True)
	if len(approx) == 4:
		screenCnt = approx
		break

cv2.drawContours(canvas, [approx], -1, (0, 255, 0), 3)
cv2.imshow("Game Boy Screen", canvas)
cv2.waitKey(0)
 
# if our approximated contour has four points, then
# we can assume that we have found our screen



# print the lines and pick the end points of one of the lines to display in red
# this helps to see how the lines are being found, uncomment next two lines to see
# print lines
#cv2.line(input_copy2,(5,70),(11,384),(0,0,255),2)
#cv2.imshow("input_copy2",input_copy2)

# write output to file
# cv2.imwrite('houghlines.jpg',in)
# cv2.imwrite('houghlinesP.jpg',input_copy2)

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
# cv2.imshow("a_channel Threshold Binary", a_thresh_image)
# cv2.imwrite('output.tif', a_thresh_image)

#a_thresh_image2 = a_thresh_image.copy()
# cv2.imshow("a_thresh_2",a_thresh_image2)

a_thresh_image2 = cv2.imread("output.tif")
# cv2.imshow("a_channel Threshold Binary 2", a_thresh_image2)
cv2.imwrite('threshold.tif', a_thresh_image)
dst = cv2.addWeighted(a_thresh_image2,0.95, input_image,0.95,0)

dst2 = dst.copy()

for x1,y1,x2,y2 in linesP[0]:
    cv2.line(dst2,(x1,y1),(x2,y2), (255,0,0) ,2)

# cv2.imshow("blended", dst)
# cv2.imshow("blended2", dst2)

cv2.waitKey(0)

# END SCRIPT