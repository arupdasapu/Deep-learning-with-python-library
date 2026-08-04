import cv2

camera = cv2.VideoCapture(0)  # Open the default camera (usually the first camera)

frame_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))  # Get the width of the video frames
frame_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))  # Get the height

codec = cv2.VideoWriter_fourcc(*'XVID')  # Define the codec for the video writer
recorder = cv2.VideoWriter("my_video.avi", codec, 20, (frame_width, frame_height))

while True:
    success, image = camera.read()  # Capture a frame from the camera

    if not success:
        break
    recorder.write(image)  # Write the captured frame to the video file
    cv2.imshow("Video Recording live", image)  # Display the captured frame

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Exit the loop when 'q' is pressed
        break

camera.release()  # Release the camera
recorder.release()  # Release the video writer  
cv2.destroyAllWindows()  # Close all windows