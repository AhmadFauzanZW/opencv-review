import cv2

img = cv2.imread('orang.png', 0)
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
img = cv2.rotate(img, cv2.ROTATE_180)

cv2.imwrite("orang_kebalik.png", img)

cv2.imshow('orang', img)

cv2.waitKey(0)
cv2.destroyAllWindows()