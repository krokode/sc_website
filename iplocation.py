import requests


def get_ip_based_geolocation(ip):
    response = requests.get(f'https://ipinfo.io/{ip}/json')
    data = response.json()
    return {
        "ip": data.get("ip"),
        "hostname": data.get("hostname"),
        "city": data.get("city"),
        "region": data.get("region"),
        "country": data.get("country"),
        "loc": data.get("loc"),  # Latitude and Longitude in "lat,lon" format
        "organization": data.get("org")
    }


if __name__ == "__main__":
    location = get_ip_based_geolocation()
    print(location)
