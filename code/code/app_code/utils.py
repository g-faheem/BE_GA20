from logging import captureWarnings
import time
import cv2
import os as os


def gen():
    while True:
        # Capture a frame from the webcam
        capture_images = cv2.VideoCapture(0) 
        ret, frame = capture_images.read()

        # Check if image capture is enabled
        if capture_images:
            # Get the current time
            now = time.time()

            # Set the filename to include the current timestamp
            filename = os.path.join("", f"{int(now)}.jpg")

            # Save the frame to the specified directory
            cv2.imwrite(filename, frame)

        # Wait for 5 seconds before capturing the next image
        time.sleep(5)

        # Convert the frame to JPEG format
        ret, jpeg = cv2.imencode('.jpg', frame)

        # Yield the frame as an HTTP response
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n')
