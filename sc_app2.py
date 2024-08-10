from flask import Flask, render_template, Response
import cv2

app = Flask(__name__)

# Initialize the camera
# print(cv2.getBuildInformation())
camera = cv2.VideoCapture(0)


def generate_frames():
    while True:
        success, frame = camera.read()  # Read the camera frame
        if not success:
            break
        else:
            # Encode the frame as JPEG
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            # Yield the frame to the browser
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/')
def index():
    # Render the HTML template
    return render_template('index2.html')


@app.route('/video_feed')
def video_feed():
    # Return the camera feed
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    # app.run(host='0.0.0.0', port=5000)
    # start web server
    app.run(host="127.0.0.1", port=8080, debug=True)
