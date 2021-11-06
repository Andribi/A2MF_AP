# create sketch images

import cv2
from pathlib import Path
import os


input_path = [Path('fairface', 'train'), Path('fairface', 'val')]
dest_path = [Path('fairface', 'train_sk'), Path('fairface', 'val_sk')]

def img2sketch(photo, k_size):

    #Read Image
    img = cv2.imread(str(Path(str(input_path[1]), photo)))

    # Convert to Grey Image
    grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Invert Image
    invert_img = cv2.bitwise_not(grey_img)
    #invert_img = 255-grey_img

    # Blur image
    blur_img = cv2.GaussianBlur(invert_img, (k_size, k_size), sigmaX=0, sigmaY=0)

    # Invert Blurred Image
    #invblur_img = cv2.bitwise_not(blur_img)
    invblur_img = 255-blur_img

    # Sketch Image
    sketch_img = cv2.divide(grey_img, invblur_img, scale=255.0)

    # Save Sketch
    cv2.imwrite(str(Path(str(dest_path[1]), photo)), sketch_img)


for pic in os.listdir(input_path[1]):
    img2sketch(photo=pic, k_size=21)
