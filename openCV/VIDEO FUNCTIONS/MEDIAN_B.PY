import cv2

image = cv2.imread(r"D:\project\Open cv\VIDEO FUNCTIONS\nature.jpg")


blurred = cv2.GaussianBlur(image, (11, 11), 0)

cv2.imshow("Original Image", image)
cv2.imshow("Blurred Image", blurred)

cv2.waitKey(0)  
cv2.destroyAllWindows()