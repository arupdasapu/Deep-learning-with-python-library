import cv2
import numpy as np

image = cv2.imread(r"D:\project\Open CV\VIDEO FUNCTIONS\images.jpg")  # Read the image from file

sharpen_kernel = np.array([[0, -1, 0],
                           [-1, 6, -1],
                           [0, -1, 0]])  # Define a sharpening kernel
sharpened_image = cv2.filter2D(image, -1, sharpen_kernel)  # Apply the sharpening filter        

cv2.imshow("Original Image", image)  # Display the original image
cv2.imshow("Sharpened Image", sharpened_image)  # Display the sharpened
cv2.waitKey(0)  # Wait for a key press to close the windows
cv2.destroyAllWindows()  # Close all OpenCV windows