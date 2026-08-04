"""
1- cv2.bitwise_and(imag1, imag2)
2- cv2.bitwise_or(imag1, imag2)
3- cv2.bitwise_not(imag1, imag2)


* img1 img2 height width same
** use only black and white images
***
"""

import cv2
import numpy as np

img1 = np.zeros((300, 300), dtype=np.uint8)
img2 = np.zeros((300, 300), dtype=np.uint8)

cv2.circle(img1, (150, 150), 100, 255, -1)  # Draw a filled circle on img1
cv2.rectangle(img2, (100, 100), (250, 250), 255, -1)  # Draw a filled rectangle on img2

bitwise_and = cv2.bitwise_and(img1, img2)  # Keeps only the overlapping common areas
bitwise_or = cv2.bitwise_or(img1, img2)  # Combines both shapes together
bitwise_not = cv2.bitwise_not(img1)  # Inverts black and white colors

cv2.imshow("Circle", img1)
cv2.imshow("Rectangle", img2)
cv2.imshow("Bitwise AND", bitwise_and)
cv2.imshow("Bitwise OR", bitwise_or)
cv2.imshow("Bitwise NOT", bitwise_not)

cv2.waitKey(0)
cv2.destroyAllWindows()