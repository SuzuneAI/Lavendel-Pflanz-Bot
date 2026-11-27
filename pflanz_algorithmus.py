import random

def finde_freie_stelle(garten_breite, garten_hoehe, belegte_stellen, abstand):
  """Findet eine freie Stelle im Garten, die mindestens 'abstand' von den belegten Stellen entfernt ist."""
  while True:
    x = random.randint(0, garten_breite - 1)
    z = random.randint(0, garten_hoehe - 1)
    ist_frei = True
    for belegte_x, belegte_z in belegte_stellen:
      if abs(x - belegte_x) < abstand and abs(z - belegte_z) < abstand:
        ist_frei = False
        break
    if ist_frei:
      return x, z


# Beispielwerte
garten_breite = 40
garten_hoehe = 40
belegte_stellen = [(10, 5), (20, 10), (30, 15)]
abstand = 1.5

# Finde eine freie Stelle
x, z = finde_freie_stelle(garten_breite, garten_hoehe, belegte_stellen, abstand)

print(f"Freie Stelle gefunden: x={x}, z={z}")
