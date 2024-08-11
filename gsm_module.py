# pip install pyserial

import serial


def read_gps(serial_port='/dev/ttyUSB0', baud_rate=9600):
    with serial.Serial(serial_port, baud_rate, timeout=1) as ser:
        while True:
            line = ser.readline().decode('utf-8')
            if line.startswith('$GPGGA'):
                parts = line.split(',')
                if len(parts) > 2:
                    latitude = parts[2]
                    longitude = parts[4]
                    return latitude, longitude


if __name__ == "__main__":
    latitude, longitude = read_gps()
    print(f"Latitude: {latitude}, Longitude: {longitude}")
