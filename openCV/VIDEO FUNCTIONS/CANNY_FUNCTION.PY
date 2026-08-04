import cv2

img = cv2.imread(r"D:\project\Open CV\VIDEO FUNCTIONS\flower.jpg")

edges = cv2.Canny(img, 50, 150)

cv2.imshow("Original Image", img)
cv2.imshow("Canny Edge Detection", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()