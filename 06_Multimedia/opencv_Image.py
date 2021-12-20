import cv2

img = cv2.imread('winter.jpg')
img2 = cv2.resize(img,(400,550))

edge1 = cv2.Canny(img2, 50, 100)
edge2 = cv2.Canny(img2, 100, 150)
edge3 = cv2.Canny(img2, 150, 200)


cv2.imshow('winter', img2)
cv2.imshow('edge1', edge1)
cv2.imshow('edge2', edge2)
cv2.imshow('edge3', edge3)

cv2.waitKey(0)

cv2.destroyAllWindows()