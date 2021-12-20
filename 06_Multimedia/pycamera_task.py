import picamera
import time

path = '/home/pi/src3/06_Multimedia'

camera = picamera.PiCamera()

try:
    while True:
        now_str = time.strftime("%Y%m%d_%H%M%S")
        camera.resolution = (640,480)
        user_input = int(input('photo:1, video:2, exit:9 '))
        if user_input == 1:
            camera.start_preview()
            time.sleep(2)                       
            camera.capture('%s/photo_%s.jpg' % (path , now_str))
            camera.stop_preview()
        elif user_input == 2:
            camera.start_recording('%s/video_%s.h264' % (path , now_str))
            input('press enter to stop recording')
            camera.stop_recording()
        elif user_input == 9:
            break        
finally:
    camera.stop_preview()