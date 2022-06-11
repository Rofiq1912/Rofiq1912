import cv2
import numpy as np

image = cv2.imread ("F55120101.jpg")
print('Image', image)

cv2.imshow("Gambar Ori", image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale", gray)

cv2.waitKey(0)
cv2.destroyAllWindows()