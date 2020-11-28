# 9. Vorlesung 28.11.2020, Skript Python 5 (07_Python_05.pdf) 
# Nachholtermin vom 26.11. 20 Uhr ohne Übungen
# Übung: Bilder skalieren

import cv2

scale = 1.0
filename  = "gleisdreieck.jpg"

while True:
    image = cv2.imread(filename, cv2.IMREAD_COLOR)
    image_resized = cv2.resize(image, None, fx=scale, fy=scale, interpolation=cv2.INTER_CUBIC)
    cv2.imshow(filename, image_resized)
    
    key_pressed = cv2.waitKey()

    if key_pressed == 27: #esc
        cv2.destroyWindow(filename)
        break
    elif key_pressed == 43: #plus
        scale = scale * 1.2
    elif key_pressed == 45: #minus
        scale = scale * 0.8
    
    print ("Aktuelle Skalierung: %0.2f" % scale)
