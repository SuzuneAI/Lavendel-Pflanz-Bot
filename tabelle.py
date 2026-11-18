# Eine einfache Tabelle zum Speichern von Daten

daten = []

# Funktion zum Hinzufügen einer Zeile zur Tabelle
def zeile_hinzufuegen(zeile):
  daten.append(zeile)

# Funktion zum Ausgeben der Tabelle
def tabelle_ausgeben():
  for zeile in daten:
    print(zeile)

# Beispiel:
zeile_hinzufuegen(['Standort', 'Lavendelmenge', 'Sonnenstunden'])
zeile_hinzufuegen(['Garten Nord', '5', '6'])
zeile_hinzufuegen(['Garten Süd', '3', '8'])

tabelle_ausgeben()
