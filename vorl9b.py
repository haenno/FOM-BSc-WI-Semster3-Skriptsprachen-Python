# 9. Vorlesung 28.11.2020, Skript Python 5 (07_Python_05.pdf) 
# Nachholtermin vom 26.11. 20 Uhr ohne Übungen
# Übung: +Bilder rotieren

import cv2

scale     = 1.0
rotation  = 0
filename  = "cube2_1.jpg"

while True:
    image = cv2.imread(filename, cv2.IMREAD_COLOR)
    image_resized = cv2.resize(image, None, fx=scale, fy=scale, interpolation=cv2.INTER_CUBIC)

    rows,cols = image_resized.shape[0:2] #get heigt and width 

    rotation_matrix = cv2.getRotationMatrix2D((cols/2,rows/2), rotation, 1)
    image_rotated = cv2.warpAffine(image_resized, rotation_matrix, (cols,rows))

    cv2.imshow(filename, image_rotated)
    
    key_pressed = cv2.waitKey()
    if key_pressed == 27: #esc
        cv2.destroyWindow(filename)
        break
    elif key_pressed == 43: #plus
        scale = scale * 1.2
    elif key_pressed == 45: #minus
        scale = scale * 0.8
    elif key_pressed == 114: #r
        rotation = rotation + 10
    elif key_pressed == 108: #l 
        rotation = rotation -10
    print ("Skalierung: %0.0f%%, Rotation: %d°" % ((scale*100), rotation))
