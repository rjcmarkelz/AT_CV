# import the necessary packages
from matplotlib import pyplot as plt
import numpy as np
import argparse
import cv2

# get some info from the user
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
	help = "Path to the image")
args = vars(ap.parse_args())

# Load the image and display it
input_image = cv2.imread(args["image"])
# cv2.imshow("input_image", input_image)

# # Convert the image to the L*a*b* color spaces
lab_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2LAB)
hsb_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2HSV)
# cv2.imshow("L*a*b*", lab_image)
# print cv2.split(lab_image)
l_channel,a_channel,b_channel = cv2.split(lab_image)
B_channel,G_channel,R_channel = cv2.split(input_image)
H_channel,S_channel,hsB_channel = cv2.split(hsb_image)
# cv2.imshow("L",l_channel)
# cv2.imshow("a",a_channel)
# cv2.imshow("b",b_channel)
# cv2.imshow("R",R_channel)
# cv2.imshow("B",B_channel)
# cv2.imshow("G",G_channel)

# cv2.imshow("H",R_channel)
cv2.imshow("S",S_channel)
# cv2.imshow("B",hsB_channel)
# Print the minimum and maximum of lightness.
# print np.min(l_channel) # 0
# print np.max(l_channel) # 244
# print np.mean(l_channel)
# print np.median(l_channel)

# Print the minimum and maximum and median of a.
# print np.min(a_channel) 
# print np.max(a_channel) 
# print np.median(a_channel)

# Print the minimum and maximum of b.
# print np.min(b_channel) # 108
# print np.max(b_channel) # 220
# print np.mean(b_channel)
# print np.median(b_channel)

# hist = cv2.calcHist([S_channel], [0], None, [256], [0, 256])
# # Plot the histogram
# plt.figure()
# plt.title("Grayscale Histogram")
# plt.xlabel("Bins")
# plt.ylabel("# of Pixels")
# plt.plot(hist)
# plt.xlim([0, 256])
# plt.show()
# cv2.waitKey(0)


# # # # #define boundry
# S_channel = cv2.GaussianBlur(S_channel,(5,5),0)
# cv2.imshow("S channel", S_channel)
# thresh = cv2.adaptiveThreshold(S_channel,255,1,1,11,2)
# cv2.imshow("S channel thresh", thresh)

blur = cv2.bilateralFilter(S_channel,9,100,100)
cv2.imshow("blur", blur)

(T, thresh_image) = cv2.threshold(blur, 100, 120, cv2.THRESH_BINARY)
cv2.imshow("Threshold Binary", thresh_image)
canny_image = cv2.Canny(thresh_image, 100, 200, apertureSize = 3)
#canny_image = cv2.Canny(thresh_image, 51, 65)
cv2.imshow("Canny", canny_image)

kernel = np.ones((5,5),np.uint8)
dilation = cv2.dilate(canny_image,kernel,iterations = 1)
cv2.imshow("Canny dilation", dilation)

minLineLength = 100
maxLineGap = 10
lines = cv2.HoughLinesP(dilation,1,np.pi/180,100,minLineLength,maxLineGap)
# print lines

lineexample = lines[0]
print lineexample
# cv2.line(dilation,(x1,y1),(x2,y2),(0,255,0),2)
# for x1,y1,x2,y2 in lines[0]:
#     cv2.line(dilation,(x1,y1),(x2,y2),(0,255,0),2)
# cv2.imwrite('houghlines5.jpg',dilation)

# contours,hierarchy = cv2.findContours(thresh, 1, 2)
# #print contours
# cnt = contours[0]
# area = cv2.contourArea(cnt)
# perimeter = cv2.arcLength(cnt,True)

# epsilon = 0.1*cv2.arcLength(cnt,True)
# approx = cv2.approxPolyDP(cnt,epsilon,True)

# find contours in the edged image, keep only the largest
# ones, and initialize our screen contour
# (cnts, _) = cv2.findContours(canny_image.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:1]
# screenCnt = None

# # loop over our contours
# for c in cnts:
# 	# approximate the contour
# 	peri = cv2.arcLength(c, False)
# 	approx = cv2.approxPolyDP(c, 0.90 * peri, False)

# 	# if our approximated contour has four points, then
# 	# we can assume that we have found our screen
# 	if len(approx) == 4:
# 		screenCnt = approx
# 		break

# # draw a rectangle around the screen
# orig = input_image.copy()
# cv2.drawContours(input_image, [screenCnt], -1, (0, 255, 0), 3)
# cv2.imshow("found countours", input_image)

# lab = cv2.inRange(lab, lowerb = plant_min, upperb = plant_max)
#cv2.imshow("Lab Filter", lab)
# write thresholded image
# cv2.imwrite('output.tif', thresh_image)
cv2.waitKey(0)