import cv2

image = cv2.imread(r"D:\project\Open CV\Ball_python_lucy.jpg")

if image is None:
    print("Oops! your image is not working properly")  # Print an error message if the image is not loaded correctly

else:
    print("Image loaded successfully")  # Print a success message if the image is loaded correctly
    cv2.circle(image, (75, 171), 150, (0, 0, 255), -1)  # Draw a red circle with center at (200, 200) and radius of 100 pixels
    
    cv2.imshow("Drawn circle", image)
    cv2.waitKey(0)  # Wait for a key press
    cv2.destroyAllWindows()  # Close all windows