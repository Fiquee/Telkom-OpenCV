import cv2
import os.path

img = cv2.imread(os.path.join('Images', "lenna.png"))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Writes to new file
cv2.imwrite('gray.png', gray)

cv2.imshow('Grayscale Converting', gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
