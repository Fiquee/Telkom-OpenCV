import cv2
import os.path

# Exercise 1: Reads Image that is in the Library
img = cv2.imread(os.path.join('Images', "lenna.png"))

# Exercise 4: Resize Image
h, w = img.shape[:2]
new_H, new_W = int(h/2), int(w/2)
resized_img = cv2.resize(img, (new_H, new_W))

cv2.imshow('Displaying Image', img)
cv2.imshow('Resized Image', resized_img)

# Exercise 5: Cropping Image
croppedImg = img[440:512, 440:512]
cv2.imshow('Cropped Image', croppedImg)

# Exercise 6: Rotating Image
center = (h/2, w/2)
rotate = cv2.getRotationMatrix2D(center, 180, 1)
rotatedImg = cv2.warpAffine(img, rotate, (w, h))
cv2.imshow('Rotated Image', rotatedImg)

# Waits for a key press (enables showing of the window as it waits)
cv2.waitKey(0)
cv2.destroyAllWindows()
