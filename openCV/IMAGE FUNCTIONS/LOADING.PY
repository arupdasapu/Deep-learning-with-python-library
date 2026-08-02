import cv2

image = cv2.imread(r"D:\project\Open CV\Ball_python_lucy.jpg")

if image is None:
    print("Error: Image not found")
else:
    print("Image loaded successfully")