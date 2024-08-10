from flask import Flask, render_template, Response, request
import cv2
import requests

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


def get_location(ip):
    try:
        # Using a public API to get location details based on IP
        response = requests.get(f'http://ip-api.com/json/{ip}')
        data = response.json()
        return {
            "ip": ip,
            "country": data.get("country"),
            "region": data.get("regionName"),
            "city": data.get("city"),
            "zip": data.get("zip"),
            "lat": data.get("lat"),
            "lon": data.get("lon"),
            "isp": data.get("isp"),
        }
    except Exception as e:
        return {"error": str(e)}


@app.route('/')
def index():
    # Render the HTML template
    # user_ip = request.remote_addr  # Get the user's IP address
    # user_ip = request.headers['X-Forwarded-For']
    """  headers_list = request.headers.getlist("X-Forwarded-For")
    user_ip = headers_list[0] if headers_list else request.remote_addr """

    user_ip = request.access_route[-1]
    location_info = get_location(user_ip)  # Get the location information
    return render_template('index2.html', location=location_info)


@app.route('/video_feed')
def video_feed():
    # Return the camera feed
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    # app.run(host='0.0.0.0', port=5000)
    # start web server
    app.run(host="127.0.0.1", port=8080, debug=True)
