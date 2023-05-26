from flask import Flask
from flask import Flask, render_template, Response, request

from utils import gen

app = Flask(__name__)

@app.route('/video_feed')
def video_feed():
    return Response(gen(),mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/', methods=['GET', 'POST'])
def index():
    global capture_images

    if request.method == 'POST':
        if request.form.get('start'):
            capture_images = True
        elif request.form.get('stop'):
            capture_images = False

    return render_template('index.html')

def start_capture():
    global capture_images
    capture_images = True

def stop_capture():
    global capture_images
    capture_images = False

if __name__ == "__main__":
  app.run()
