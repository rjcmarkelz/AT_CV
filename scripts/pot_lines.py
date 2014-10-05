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
cv2.imshow("H",H_channel)
# cv2.imshow("hsB",hsB_channel)



# hist = cv2.calcHist([H_channel], [0], None, [256], [0, 256])
# # Plot the histogram
# plt.figure()
# plt.title("S Histogram")
# plt.xlabel("Bins")
# plt.ylabel("# of Pixels")
# plt.plot(hist)
# plt.xlim([0, 256])
# plt.show()
# cv2.waitKey(0)

blur = cv2.bilateralFilter(H_channel,9,100,100)
cv2.imshow("blur", blur)

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

(T, thresh_image) = cv2.threshold(blur, 75, 110, cv2.THRESH_BINARY)
cv2.imshow("Threshold Binary", thresh_image)

canny_image = cv2.Canny(thresh_image, 100, 200, apertureSize = 3)
cv2.imshow("Canny", canny_image)

kernel = np.ones((5,5),np.uint8)
dilation = cv2.dilate(canny_image,kernel,iterations = 2)
cv2.imshow("Canny dilation", dilation)

# lines = cv2.HoughLines(dilation,1,np.pi/180, 150)

# # print lines
input_copy1 = input_image.copy()
input_copy2 = input_image.copy()

# # for rho,theta in lines[0]:
# #     a = np.cos(theta)
# #     b = np.sin(theta)
# #     x0 = a*rho
# #     y0 = b*rho
# #     x1 = int(x0 + 1000*(-b))
# #     y1 = int(y0 + 1000*(a))
# #     x2 = int(x0 - 1000*(-b))
# #     y2 = int(y0 - 1000*(a))
# #     cv2.line(input_copy1,(x1,y1),(x2,y2),(0,0,255),2)
#     # print a, b, x1, y1, x2, y2
# #cv2.imshow("input_copy1",input_copy1)

minLineLength = 10000
maxLineGap = 40
linesP = cv2.HoughLinesP(dilation,1,np.pi/180,100,minLineLength,maxLineGap)
# print lines
for x1,y1,x2,y2 in linesP[0]:
    cv2.line(input_copy2,(x1,y1),(x2,y2),(0,255,0),2)
#cv2.line(input_copy2,(5,70),(11,384),(0,0,255),2)
cv2.imshow("input_copy2",input_copy2)

# cv2.imwrite('houghlines.jpg',in)

# cv2.imwrite('houghlinesP.jpg',input_copy2)

# # print lines
# input_copy1 = input_image.copy()
# input_copy2 = input_image.copy()
# print type(lines)
# print lines[0]
# for rho,theta in lines[0]:
#     a = np.cos(theta)
#     b = np.sin(theta)
#     x0 = a*rho
#     y0 = b*rho
#     x1 = int(x0 + 1000*(-b))
#     y1 = int(y0 + 1000*(a))
#     x2 = int(x0 - 1000*(-b))
#     y2 = int(y0 - 1000*(a))
#     cv2.line(input_copy1,(x1,y1),(x2,y2),(0,0,255),2)
#     # print a, b, x1, y1, x2, y2
# cv2.imshow("input_copy1",input_copy1)

# img = cv2.imread("C:/temp/1.png")
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# edges = cv2.Canny(gray, 80, 120)
# lines = cv2.HoughLinesP(edges, 1, math.pi/2, 2, None, 30, 1);
# for line in lines[0]:
#     pt1 = (line[0],line[1])
#     pt2 = (line[2],line[3])
#     cv2.line(img, pt1, pt2, (0,0,255), 3)
# cv2.imwrite("C:/temp/2.png", img)

# pseudo code
# gradient1 = (line1.pt1.y-line1.pt2.y)/(line1.pt1.x-line1.pt2.x) 
# gradient2 = (line2.pt1.y-line2.pt2.y)/(line1.pt1.x-line2.pt2.x)
# if gradient1 == gradient2
#     average_pt1.x = (line1.pt1.x+line2.pt1.x)/2
#     average_pt2.x = (line1.pt2.x+line2.pt2.x)/2

#     average_pt1.y = (line1.pt1.y+line2.pt1.y)/2
#     average_pt2.x = (line1.pt2.y+line2.pt2.y)/2
# cvLine(image, average_pt1, average_pt2, CV_RGB(255,0,0), 3, 8) 

cv2.waitKey(0)