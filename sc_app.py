# packages
from flask import Flask

# web app instance
app = Flask(__name__)

# root route


@app.route("/")
def index():
    return "Hello from Serge flask webapp"


# main loop
if __name__ == "__main__":
    # start web server
    app.run(host="127.0.0.1", port=8080, debug=True)
