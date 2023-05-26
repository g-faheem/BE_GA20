
import cv2
import os as os
from flask import Flask, render_template, Response

app = Flask(__name__)

# Set the default capture status to False
capture_status = False

def gen_frames():
    # Open the video capture device (webcam)
    capture = cv2.VideoCapture(0)

    # Check if the capture device was successfully opened
    if not capture.isOpened():
        raise IOError("Cannot open webcam")



    # Create the captures directory if it doesn't already exist
    if not os.path.exists("captures"):
        os.makedirs("captures")

    while True:
        global capture_status
        if capture_status:
            # Read a frame from the webcam
            continue
        else:
            ret, frame = capture.read()

            # Check if the frame was successfully read
            if not ret:
                break

                # Set the filename to  capture index
            filename = os.path.join("capture", f"image.jpg")

            # Save the frame to the specified directory
            cv2.imwrite(filename, frame)

            # Encode the frame as JPEG
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            # Yield the frame as an HTTP response
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    # Release the video capture device and destroy any OpenCV windows
    capture.release()
    cv2.destroyAllWindows()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/start_capture', methods=['POST'])
def start_capture():
    global capture_status
    capture_status = True
    return "Capture started"


@app.route('/stop_capture', methods=['POST'])
def stop_capture():
    global capture_status
    capture_status = False
    return "Capture stopped"


if __name__ == '__main__':
    app.run(debug=True)
