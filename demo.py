import cv2
from videocaptureasync import VideoCaptureAsync

def init_cameras():
    #capture thermic frame
    cap_thermal = VideoCaptureAsync(thermal=True)
    cap_thermal.start()
    #capture normal frame
    cap_normal = VideoCaptureAsync(thermal=False)
    cap_normal.start()
    return cap_normal, cap_thermal

def stop_cameras(cap_normal, cap_thermal):
    cap_thermal.stop()
    cap_normal.stop()


cap_normal, cap_thermal = init_cameras()
while True:
    _, thermal_frame = cap_thermal.read()
    _, normal_frame  = cap_normal.read()
    cv2.imshow('thermal', thermal_frame)
    cv2.imshow('normal', normal_frame)

    #end keys, press 'q' key for exit the program
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#closing conection for thermal camera and normal camera¿
stop_cameras(cap_normal, cap_thermal)
cv2.destroyAllWindows()