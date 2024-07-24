# packages
from flask import Flask

# web app instance
app = Flask(__name__)

# root route


@app.route("/")
def index():
    return "Hello from Flask"


# main loop
if __name__ == "__main__":
    # start web server
    app.run(debug=True, threaded=True)
