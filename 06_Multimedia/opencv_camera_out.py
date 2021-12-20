import cv2

cam = cv2.VideoCapture(0)

if not cam.isOpened():
    print('Camera open failed')
    exit()

fourcc = cv2.VideoWriter_fourcc(*'DIVX')

out = cv2.VideoWriter('output.avi', fourcc, 30, (640,480))

while True:
    ret, frame = cam.read()
    if not ret:
        break

    cv2.imshow('frame', frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame_1',gray)
    edge1 = cv2.Canny(frame, 50, 100)
    cv2.imshow('fr',edge1)
    out.write(frame)    

    if cv2.waitKey(10) == 13:
        break

cv2.waitKey(0)

cam.release()
out.release()
cv2.destroyAllWindows()