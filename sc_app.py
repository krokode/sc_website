# packages
from flask import Flask, render_template, render_template_string

# web app instance
app = Flask(__name__)

# root route


@app.route("/")
def index():
    return render_template_string('''
    <h1 align = "center">Hello from Serge flask webapp</h1>
    ''')


""" 
    render_template("index.html")
"""

# main loop
if __name__ == "__main__":
    # start web server
    app.run(host="127.0.0.1", port=8080, debug=True)
