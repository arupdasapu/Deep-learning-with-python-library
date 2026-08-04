import cv2

image = cv2.imread(r"D:\project\Open CV\VIDEO FUNCTIONS\nature.jpg")

if image is None:
    print("Error: Could not load the image. Check the file path!")
else:
    blurred = cv2.GaussianBlur(image, (15, 15), 1)

    cv2.imshow("Original Image", image)
    cv2.imshow("Blurred Image", blurred)

    cv2.waitKey(0)
    cv2.destroyAllWindows()