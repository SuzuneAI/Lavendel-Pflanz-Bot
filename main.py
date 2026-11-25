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
