# packages
from flask import Flask

# web app instance
app = Flask(__name__)

# root route


@app.route("/")
def index():
    return "Hello from Serge webapp"


# main loop
if __name__ == "__main__":
    # start web server
    app.run(host="0.0.0.0", port=80)
