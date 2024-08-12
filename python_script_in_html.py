from flask import *
# Importing all the methods, classes, functions from Flask

app = Flask(__name__)

# This is the first page that comes when you
# type localhost:8080... it will have a tag
# that redirects to a page


@app.route("/")
def HomePage():
    return "<a href='/runscript'>EXECUTE SCRIPT </a>"

# Once it redirects here (to localhost:5000/runscript),
# it will run the code before the return statement


@app.route("/runscript")
def ScriptPage():
    # Type what you want to do when the user clicks on the link.
    #
    print('Python script executed')
    # Once it is done with doing that code... it will
    # redirect back to the homepage
    return redirect(url_for("HomePage"))


# Running it only if we are running it directly
# from the file... not by importing
if __name__ == "__main__":
    # app.run(host='0.0.0.0', port=5000)
    # start web server
    app.run(host="127.0.0.1", port=8080, debug=True)
