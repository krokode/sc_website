# packages
from flask import Flask, render_template

""" 
from flask import request
import base64
import cv2
import numpy as np
import threading 
"""

# web app instance
app = Flask(__name__)

# root route


@app.route("/")
def index_html():
    return render_template("index1.html")

# update remote webcam view frame


""" 
def update(frame):
    # open frame in a window
    cv2.imshow('Stalking', frame)
    cv2.waitKey()

 """
# get video on server side

""" 
@app.route('/stream', methods=['POST'])
def vc_stream():
    # extract base64 encoded string from the client (web browser)
    img_str = request.form.get('frame').split('data:image/png;base64,')[-1]

    # convert base64 encoded string to a byte string
    img_byt = base64.b64decode(img_str)

    # convert a byte string to a numpy array
    image = np.fromstring(img_byt, np.uint8)

    # convert a numpy array to an opencv compatible image
    frame = cv2.imdecode(image, cv2.IMREAD_COLOR)

    # display the frame in a window
    display_thread = threading.Thread(target=update, args=(frame,))
    display_thread.start()

    # return from the API call
    return ''

 """

# main loop
if __name__ == "__main__":
    # start web server
    app.run(host="127.0.0.1", port=8080, debug=True)
