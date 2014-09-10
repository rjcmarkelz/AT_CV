# import the necessary packages
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
cv2.imshow("input_image", input_image)

# # Convert the image to the L*a*b* color spaces
lab_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2LAB)
# cv2.imshow("L*a*b*", lab_image)
cv2.split(lab_image)
# print cv2.split(lab_image)
l_channel,a_channel,b_channel = cv2.split(lab_image)
# cv2.imshow("L",l_channel)
# cv2.imshow("a",a_channel)
# cv2.imshow("b",b_channel)

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

# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.bilateralFilter(l_channel, 11, 17, 17)
edged = cv2.Canny(gray, 30, 200)
cv2.imshow("gray", gray)
cv2.imshow("edged", edged)

th3 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)
cv2.imshow("gaussian", th3)

# # # # #define boundry
# (T, thresh_image) = cv2.threshold(a_channel, 110, 130, cv2.THRESH_BINARY)
# cv2.imshow("Threshold Binary", thresh_image)
# print np.min(thresh_image)
# canny_image = cv2.Canny(thresh_image, 130, 130)
# cv2.imshow("Canny", canny_image)






# lab = cv2.inRange(lab, lowerb = plant_min, upperb = plant_max)
#cv2.imshow("Lab Filter", lab)
# write thresholded image
# cv2.imwrite('output.tif', thresh_image)
cv2.waitKey(0)






