import cv2

def take_snapshot():
    # Initialize the VideoCapture class from cv2
    videoCaptureObject = cv2.VideoCapture(0)

    result = True

    while result:
        # read the frames while the camera is on
        ret, frame = videoCaptureObject.read()
        # cv2.imwrite() method is used to save an image to any storage device
        cv2.imwrite("NewImage2.png", frame)
        # print("Ret:", ret)
        # print("Frame:", frame)
        result = False
    
    print("Successfully captures snapshot!")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

take_snapshot()