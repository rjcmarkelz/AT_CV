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
cv2.imshow("input_image", input_image)

# # Convert the image to the L*a*b* color spaces
lab_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2LAB)
hsb_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2HSV)
# cv2.imshow("L*a*b*", lab_image)
cv2.split(lab_image)
# print cv2.split(lab_image)
l_channel,a_channel,b_channel = cv2.split(lab_image)
B_channel,G_channel,R_channel = cv2.split(input_image)
H_channel,S_channel,hsB_channel = cv2.split(hsb_image)
# cv2.imshow("L",l_channel)
# cv2.imshow("a",a_channel)
cv2.imshow("b",b_channel)
cv2.imshow("R",R_channel)
cv2.imshow("B",B_channel)
cv2.imshow("G",G_channel)

cv2.imshow("H",R_channel)
cv2.imshow("S",S_channel)
cv2.imshow("B",hsB_channel)
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
print np.min(b_channel) # 108
print np.max(b_channel) # 220
print np.mean(b_channel)
print np.median(b_channel)

hist = cv2.calcHist([B_channel], [0], None, [256], [0, 256])
# Plot the histogram
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist)
plt.xlim([0, 256])
plt.show()
cv2.waitKey(0)


# # # # #define boundry
(T, thresh_image) = cv2.threshold(B_channel, 45, 50, cv2.THRESH_BINARY)
cv2.imshow("Threshold Binary", thresh_image)
print np.min(thresh_image)
canny_image = cv2.Canny(thresh_image, 135, 150)
cv2.imshow("Canny", canny_image)


# lab = cv2.inRange(lab, lowerb = plant_min, upperb = plant_max)
#cv2.imshow("Lab Filter", lab)
# write thresholded image
cv2.imwrite('output.tif', thresh_image)
cv2.waitKey(0)