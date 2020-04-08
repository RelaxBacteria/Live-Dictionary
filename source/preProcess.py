"""

"""

import cv2
import numpy as np


def createPreview(image_name, prev_image_name):
    src = cv2.imread(image_name, cv2.IMREAD_COLOR)

    prev = cv2.resize(src, dsize=(340, 240), fx=0.3, fy=0.7, interpolation=cv2.INTER_LINEAR)

    cv2.imwrite(prev_image_name, prev)

def preProcess(image_name, target_image_name, gray, threashold):
    # Check Parameters
    # print("gray: {gray}, threashold: {threashold}".format(gray=gray, threashold=threashold))

    # Import image to edit
    src = cv2.imread(image_name, cv2.IMREAD_COLOR)

    is_edited = False

    if gray:
        src = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
        is_edited = True
    
    if (gray & threashold):
        # src = cv2.adaptiveThreshold(src, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, 2)
        ret, src = cv2.threshold(src, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        is_edited = True

    # Make target.png
    cv2.imwrite(target_image_name, src)

    print('Returning: ', is_edited) 
    return is_edited

    
