import json
from flask import Flask, render_template, request
import requests

app = Flask(__name__)


def get_ip_based_geolocation(ip):
    response = requests.get(f'https://ipinfo.io/{ip}/json')
    data = response.json()
    print(data)

    return {
        "ip": data.get("ip"),
        "city": data.get("city"),
        "region": data.get("region"),
        "country": data.get("country"),
        "loc": data.get("loc"),  # Latitude and Longitude in "lat,lon" format
        "organization": data.get("org"),
        "postal": data.get("postal"),
        "timezone": data.get("timezone"),
        "privacy": data.get("privacy")
    }


@ app.route('/')
def HomePage():
    # Render the HTML template
    """  user_ip1 = request.remote_addr  # Get the user's IP address
    print(f"request.remote_addr - {user_ip1}") 
    """
    """ user_ip2 = request.access_route
    print(f"request.access_route - {user_ip2}")
    """
    location_info = {}
    for i in range(len(request.access_route)):
        location_info[i] = get_ip_based_geolocation(request.access_route[i])
        i += 1
    return render_template('index0.html', location=location_info)


if __name__ == "__main__":
    # app.run(host='0.0.0.0', port=5000)
    # start web server
    app.run(host="127.0.0.1", port=8080, debug=True)
