import cv2

img = cv2.imread('winter.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('winter', gray)
cv2.imwrite('winter_Gray.jpg',gray)

while True:
    if cv2.waitKey(0) == 13:
        break

cv2.destroyAllWindows()