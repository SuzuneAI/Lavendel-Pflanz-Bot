import random

def filter_lavendel(x, z):
  # Hier kommt die Logik, um zu prüfen, ob die Koordinaten
  # innerhalb des zulässigen Bereichs für Lavendel liegen
  # Zum Beispiel: wenn x > 5 und z > 2:
  #   return True
  # else:
  #   return False
  zufalls_x = random.uniform(-5, 5)
  zufalls_z = random.uniform(-5, 5)
  # Überprüfe, ob die Koordinaten innerhalb des Gartens liegen
  if -5 <= zufalls_x <= 5 and -5 <= zufalls_z <= 5:
    return True
  else:
    return False

# Ändere den Abstand zwischen den Lavendelpflanzen
ABSTAND = 4  # Erhöhe den Wert, um mehr Abstand zu schaffen

def pflanze_lavendel(x, z):
  if filter_lavendel(x, z):
    print(f"Lavendel gepflanzt bei x={x}, z={z}")
  else:
    print("Ungültige Koordinaten für Lavendel.")


if __name__ == "__main__":
  # Beispiel: Pflanze Lavendel in einem Raster
  for i in range(-5, 5, ABSTAND):
    for j in range(-5, 5, ABSTAND):
      pflanze_lavendel(i, j)
