import matplotlib.pyplot as plt

# Daten für die Tabelle
variablen = ['Temperatur', 'Bodenfeuchtigkeit', 'Lichtintensität', 'Nährstoffgehalt']
werte = [20, 60, 80, 40]  # Beispielwerte

# Erstelle das Balkendiagramm
plt.bar(variablen, werte)

# Beschrifte das Diagramm
plt.xlabel('Variablen')
plt.ylabel('Werte')
plt.title('Lavendel-Pflanz-Bot: Umweltbedingungen')

# Zeige das Diagramm
plt.show()
