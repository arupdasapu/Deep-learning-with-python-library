import cv2

cap = cv2.VideoCapture(0)  # Open the default camera (usually the first camera)

while True:
    ret, frame = cap.read()  # Capture a frame from the camera

    if not ret:
        print("Failed to capture video frame")
        break

    cv2.imshow('Video Feed', frame)  # Display the captured frame

    if cv2.waitKey(1) & 0xFF == ord('q'):  #113 ==113 Trup// Exit the loop when 'q' is pressed
        print("Exiting video capture")
        break

cap.release()
cv2.destroyAllWindows()
