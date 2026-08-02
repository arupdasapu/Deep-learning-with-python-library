import cv2

image = cv2.imread(r"D:\project\Open CV\Ball_python_lucy.jpg")

if image is not None:
    cropped = image[100:200, 50:150]  # Crop the image using array slicing
    
    cv2.imshow("Original", image)      # Display the original image
    cv2.imshow("Cropped", cropped)     # Display the cropped image
    
    cv2.waitKey(0)                     # Wait for a key press (বানান ঠিক করা হয়েছে)
    cv2.destroyAllWindows()            # Close all windows
else:
    print("Error: Image not found")