
import cv2

image = cv2.imread(r"D:\project\Open CV\Ball_python_lucy.jpg")

if image is None:
    print("Image not found")
else:
    print("Image loaded successfully")
    
    resize_image = cv2.resize(image, (300, 300))
    
    cv2.imshow("Original Image", image)
    cv2.imshow("Resized Image", resize_image)
    
    cv2.imwrite(r"resized_output_image.jpg", resize_image)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite(r"resized_output_image.jpg", resize_image)
