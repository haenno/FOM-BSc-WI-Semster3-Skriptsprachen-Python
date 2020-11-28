# 7. Vorlesung 20.11.2020, Skript Python 5 (07_Python_05.pdf)
# 

import cv2

img = cv2.imread("belarus.jpg", cv2.IMREAD_COLOR)
cv2.imshow("myimage",img)
cv2.waitKey(0)
cv2.destroyWindow("myimage")
