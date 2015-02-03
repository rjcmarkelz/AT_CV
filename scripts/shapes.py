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

blue = (255, 0, 0)
cv2.circle(input_image, (246, 265), 200, blue, 5)
cv2.circle(input_image, (654, 254), 200, blue, 5)
cv2.circle(input_image, (651, 637), 200, blue, 5)
cv2.circle(input_image, (267, 1129), 200, blue, 5)
cv2.circle(input_image, (631, 1175), 200, blue, 5)
cv2.circle(input_image, (665, 1514), 200, blue, 5)
cv2.imshow("l_channel line", input_image)
cv2.waitKey(0)