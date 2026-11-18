# Dieses Skript filtert die erkannten Pflanzen und bereitet die Daten für die Pflanzplanung auf.

# Importiere die notwendigen Bibliotheken
import pandas as pd

# Definiere eine Funktion, um die Daten zu filtern
def filter_data(data):
  # Erstelle einen Pandas DataFrame aus den Daten
  df = pd.DataFrame(data)

  # Filter die Daten nach der Pflanzenart
  df = df[df['art'] == 'Lavendel']

  # Gib den gefilterten DataFrame zurück
  return df

# Hauptprogramm
if __name__ == '__main__':
  # Lese die Daten aus der Datei
  data = pd.read_csv('lavendel_data.csv')

  # Filter die Daten
  filtered_data = filter_data(data)

  # Gib die gefilterten Daten aus
  print(filtered_data)
