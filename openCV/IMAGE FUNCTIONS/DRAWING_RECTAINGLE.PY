import cv2

image = cv2.imread(r"D:\project\Open CV\Ball_python_lucy.jpg")

if image is None:
    print("Oops! your image is not working properly")  # Print an error message if the image is not loaded correctly

else:
    print("Image loaded successfully")  # Print a success message if the image is loaded correctly

    #pt for point of line
    pt1 = (300, 300)  # Top-left corner of the rectangle
    pt2 = (200, 50)  # Bottom-right corner of the rectangle
    color = (0, 0,255)  # Green color in BGR
    thickness = 3  # Thickness of the rectangle border

    cv2.rectangle(image, pt1, pt2, color, thickness )  # Draw a blue line
    cv2.imshow("Drawn Line", image)
    cv2.waitKey(0)  # Wait for a key press
    cv2.destroyAllWindows()  # Close all windows