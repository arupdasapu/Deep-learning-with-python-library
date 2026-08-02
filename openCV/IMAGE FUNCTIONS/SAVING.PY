import cv2

image = cv2.imread(r"D:\project\Open CV\Ball_python_lucy.jpg")

if image is not None:
    sucess = cv2.imwrite(r"output_python.jpg", image)
    if sucess:
        print("Image saved successfully as 'output_python.jpg'")
    else:
        print("Error: Image could not be saved")
else:
    print("Error: Image not found")