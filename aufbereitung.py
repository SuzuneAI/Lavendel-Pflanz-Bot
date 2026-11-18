def aufbereiten(daten):
    # Hier kommt die Logik zur Datenaufbereitung
    # z.B. Filtern, Berechnen von Pflanzpositionen
    ergebnisse = []
    for eintrag in daten:
        # Beispiel: Nur Einträge mit positiver Lichtintensität behalten
        if eintrag['lichtintensitaet'] > 0:
            ergebnisse.append(eintrag)
    return ergebnisse

# Beispielaufruf (wird später durch tatsächliche Daten ersetzt)
if __name__ == '__main__':
    beispieldaten = [{'x': 1, 'y': 2, 'lichtintensitaet': 5}, {'x': 3, 'y': 4, 'lichtintensitaet': -1}]
    aufbereitete_daten = aufbereiten(beispieldaten)
    print(aufbereitete_daten)
