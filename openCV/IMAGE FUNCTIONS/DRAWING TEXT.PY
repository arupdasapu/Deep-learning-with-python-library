import cv2

image = cv2.imread(r"D:\project\Open CV\Ball_python_lucy.jpg")

if image is None:
    print("Oops! your image is not working properly")  # Print an error message if the image is not loaded correctly

else:
    print("Image loaded successfully")  # Print a success message if the image is loaded correctly
    cv2.putText(image, "Hello python programmer Arup", (100, 800), 
                cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0, 2))  # Draw text on the image
    
    cv2.imshow("Adding text over image", image)
    cv2.waitKey(0)  # Wait for a key press
    cv2.destroyAllWindows()  # Close all windows