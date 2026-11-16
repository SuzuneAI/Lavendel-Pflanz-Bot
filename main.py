# Lavendel-Pflanz-Bot

import random

# Liste der bereits gepflanzten Blumen
gepflanzte_blumen = []

def pflanze_lavendel(x, z):
    if (x, z) not in gepflanzte_blumen:
        print(f"Pflanze Lavendel an Position ({x}, {z})")
        gepflanzte_blumen.append((x, z))
    else:
        print(f"An Position ({x}, {z}) wächst schon eine Blume!")

# Beispiel:

for i in range(5):
    x = random.randint(-5, 5)
    z = random.randint(-5, 5)
    pflanze_lavendel(x, z)

print("Lavendel-Pflanz-Bot beendet, nya!")
