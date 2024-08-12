import cv2

def get_available_cameras():
    available_cameras = []
    # Check for 5 cameras 
    for i in range(5):
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            available_cameras.append(i)
            cap.release()
    return available_cameras

cameras = get_available_cameras()
if cameras:
    print("Available Cameras:", cameras)
else:
    print("No cameras found.")
    
""" import cv2


def list_cameras(max_cameras=10):
    available_cameras = []

    for index in range(max_cameras):
        cap = cv2.VideoCapture(index)
        if cap.isOpened():
            available_cameras.append(index)
            cap.release()

    return available_cameras


print(list_cameras()) """
