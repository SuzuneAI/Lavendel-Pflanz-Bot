# -*- coding: utf-8 -*-

import cv2
import numpy as np

# TODO: Kalibrierung der Kameraperspektive
# TODO: Pflanzalgorithmus implementieren

# Dummy-Funktion für die Pflanzung
def pflanze_lavendel(x, y):
    print(f"Lavendel gepflanzt an Position ({x}, {y})")

if __name__ == '__main__':
    print("Lavendel-Pflanz-Bot startet...")
    
    # Bild aufnehmen (Dummy)
    img = np.zeros((480, 640, 3), dtype=np.uint8)
    
    # Pflanzpositionen (Dummy)
    pflanzpositionen = [(100, 100), (200, 150), (300, 200)]

    # TODO: Hier die Kamerakalibrierung einfügen
    # TODO: Hier den Pflanzalgorithmus implementieren

    # Testpflanzungen
    for x, y in pflanzpositionen:
        pflanze_lavendel(x, y)
