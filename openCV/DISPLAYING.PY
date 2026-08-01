import cv2

image = cv2.imread(r"D:\project\Open CV\Ball_python_lucy.jpg")

if image is not None:
    cv2.imshow("Image showing", image) # open the window
    cv2.waitKey(0) #wait for a key
    cv2.destroyAllWindows() #Close the window

else:
    print("Error: Image not found")