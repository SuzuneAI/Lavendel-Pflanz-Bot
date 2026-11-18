import cv2
import numpy as np

# Bildpfad
img_path = '/home/ubuntu/downloads/lavendel.jpg'

# Bild laden
try:
    img = cv2.imread(img_path)
    if img is None:
        raise FileNotFoundError(f"Bild konnte nicht geladen werden von: {img_path}")
except FileNotFoundError as e:
    print(f"Fehler: {e}")
    exit()

# Bild verarbeiten
# ... (Hier kommt der Rest deines Codes)

# Beispiel: Bild in Graustufen konvertieren
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Beispiel: Graustufenbild anzeigen
cv2.imshow('Graustufenbild', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
