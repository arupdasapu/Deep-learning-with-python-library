import cv2  

image = cv2.imread(r"D:\project\Open CV\Ball_python_lucy.jpg") 

if image is None:  
    print("Could not load the image") 
else:  
    (h, w) = image.shape[:2]  # Extracting the height and width of the image

    center = (w // 2, h // 2)  # Calculating the center point of the image for rotation
    M = cv2.getRotationMatrix2D(center, 90, 1.0)  # Creating a rotation matrix to rotate the image by 90 degrees around the center
    ROTATED = cv2.warpAffine(image, M, (w, h))  # Applying the affine transformation to rotate the image

    cv2.imshow("Original", image)  # Displaying the original image in a window
    cv2.imshow("Rotated 90 Degrees", ROTATED)  # Displaying the rotated image in a separate window

    cv2.waitKey(0)  # Waiting indefinitely for a key press from the user
    cv2.destroyAllWindows()  # Closing all active OpenCV display windows