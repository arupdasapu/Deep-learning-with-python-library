import cv2

image = cv2.imread(r"D:\project\Open CV\Ball_python_lucy.jpg")

if image is None:  
    print("Could not load the image")
else:
    flipped_horizontal = cv2.flip(image, 1)  # Flipping the image horizontally
    flipped_vertical = cv2.flip(image, 0)    # Flipping the image vertically
    flipped_both = cv2.flip(image, -1)     # Flipping the image both horizontally and vertically

    cv2.imshow("Original", image)                  # Displaying the original image
    cv2.imshow("Flipped Horizontal", flipped_horizontal)  # Displaying the horizontally flipped image
    cv2.imshow("Flipped Vertical", flipped_vertical)    # Displaying the vertically flipped image
    cv2.imshow("Flipped Both", flipped_both)        # Displaying the image flipped both horizontally and vertically

    cv2.waitKey(0)                         # Waiting indefinitely for a key press from the user
    cv2.destroyAllWindows()                # Closing all active OpenCV display windows