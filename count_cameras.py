import cv2


def list_cameras(max_cameras=10):
    available_cameras = []

    for index in range(max_cameras):
        cap = cv2.VideoCapture(index)
        if cap.isOpened():
            available_cameras.append(index)
            cap.release()

    return available_cameras


print(list_cameras())
