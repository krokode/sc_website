from flask import Flask, render_template, request

app = Flask(__name__)


@ app.route('/')
def HomePage():
    # Render the HTML template
    user_ip = request.remote_addr  # Get the user's IP address
    print(f"request.remote_addr - {user_ip}")
    user_ip1 = request.access_route[-1]
    print(f"request.access_route[-1] - {user_ip1}")
    user_ip2 = request.access_route
    print(f"request.access_route - {user_ip2}")

    return render_template('index0.html')


if __name__ == "__main__":
    # app.run(host='0.0.0.0', port=5000)
    # start web server
    app.run(host="127.0.0.1", port=8080, debug=True)
