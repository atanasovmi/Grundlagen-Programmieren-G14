import random
from datetime import datetime

# Modul für die Trainingslogik
# Enthält Berechnungen und Datenmanipulationen

# Kalorienverbrauch pro Minute für verschiedene Übungen (Beispielwerte)
UEBUNGEN_KALORIEN = {
    "1": {"name": "Joggen", "kcal_pro_min": 10},
    "2": {"name": "Schwimmen", "kcal_pro_min": 8},
    "3": {"name": "Radfahren", "kcal_pro_min": 7},
    "4": {"name": "Krafttraining", "kcal_pro_min": 6},
    "5": {"name": "Yoga", "kcal_pro_min": 4}
}

# Monatsnamen für bessere Ausgabe
MONAT_NAMEN = {
    "01": "Januar", "02": "Februar", "03": "März", "04": "April",
    "05": "Mai", "06": "Juni", "07": "Juli", "08": "August",
    "09": "September", "10": "Oktober", "11": "November", "12": "Dezember"
}

def berechne_kalorien(dauer, faktor):
    """
    Berechnet die verbrannten Kalorien.
    """
    return dauer * faktor

def filtere_daten_nach_datum(daten, datum):
    """
    Sucht alle Einträge, die zum angegebenen Datum passen.
    Gibt eine Liste von Tupeln zurück: (Original-Index, Zeile)
    """
    treffer = []
    for index, zeile in enumerate(daten):
        # zeile[0] ist das Datum
        if len(zeile) >= 1 and zeile[0] == datum:
            treffer.append((index, zeile))
    return treffer

def loesche_eintrag(daten, index):
    """
    Löscht einen Eintrag aus der Datenliste anhand des Index.
    Gibt die aktualisierte Liste zurück.
    """
    if 0 <= index < len(daten):
        del daten[index]
    return daten

def aktualisiere_eintrag(daten, index, neuer_eintrag):
    """
    Aktualisiert einen Eintrag in der Datenliste an der angegebenen Position.
    Gibt die aktualisierte Liste zurück.
    """
    if 0 <= index < len(daten):
        daten[index] = neuer_eintrag
    return daten

def filtere_daten_nach_monat(daten, monat_jahr):
    """
    Filtert die Daten nach Monat und Jahr (Format MM.JJJJ).
    """
    gefiltert = []
    for zeile in daten:
        if len(zeile) >= 1:
            datum_str = zeile[0] # Format TT.MM.JJJJ
            try:
                # Extrahiere MM.JJJJ aus TT.MM.JJJJ
                teile = datum_str.split('.')
                if len(teile) == 3:
                    zeilen_monat_jahr = f"{teile[1]}.{teile[2]}"
                    if zeilen_monat_jahr == monat_jahr:
                        gefiltert.append(zeile)
            except IndexError:
                continue
    return gefiltert

def ermittle_jahre_fuer_monat(daten, monat):
    """
    Sucht in den Daten nach Jahren, die Einträge im angegebenen Monat haben.
    monat: String 'MM'
    Gibt eine sortierte Liste von Jahres-Strings zurück.
    """
    jahre = set()
    for zeile in daten:
        if len(zeile) >= 1:
            datum_str = zeile[0] # TT.MM.JJJJ
            try:
                teile = datum_str.split('.')
                if len(teile) == 3:
                    m = teile[1]
                    j = teile[2]
                    if m == monat:
                        jahre.add(j)
            except IndexError:
                continue
    return sorted(list(jahre))

def generiere_workout_mix(ziel_kalorien):
    """
    Generiert einen Workout-Mix basierend auf dem Kalorienziel.
    Anzahl Übungen abhängig von Kalorien:
    - <= 150 kcal: Max 1 Übung
    - <= 350 kcal: Max 2 Übungen
    - <= 500 kcal: Max 3 Übungen
    - > 500 kcal: Alle Übungen möglich
    """
    # Bestimme maximale Anzahl Übungen basierend auf Kalorienziel
    if ziel_kalorien <= 150:
        max_uebungen = 1
    elif ziel_kalorien <= 350:
        max_uebungen = 2
    elif ziel_kalorien <= 500:
        max_uebungen = 3
    else:
        max_uebungen = len(UEBUNGEN_KALORIEN)
    
    # Zufällige Anzahl Übungen wählen (mindestens 1, maximal max_uebungen)
    anzahl = random.randint(1, max_uebungen)
    
    # Zufällige Übungen auswählen
    keys = list(UEBUNGEN_KALORIEN.keys())
    selected_keys = random.sample(keys, anzahl)
    
    mix = []
    datum = datetime.now().strftime("%d.%m.%Y")
    
    # Kalorien auf Übungen verteilen
    if anzahl == 1:
        kalorien_pro_uebung = [ziel_kalorien]
    else:
        # Zufällige Gewichtung für jede Übung
        weights = [random.random() for _ in range(anzahl)]
        total_weight = sum(weights)
        kalorien_pro_uebung = [int(w / total_weight * ziel_kalorien) for w in weights]
        
        # Rundungsdifferenzen ausgleichen
        diff = ziel_kalorien - sum(kalorien_pro_uebung)
        kalorien_pro_uebung[0] += diff
    
    # Für jede ausgewählte Übung Dauer berechnen
    for i, key in enumerate(selected_keys):
        info = UEBUNGEN_KALORIEN[key]
        name = info["name"]
        faktor = info["kcal_pro_min"]
        
        soll_kcal = kalorien_pro_uebung[i]
        
        # Dauer berechnen (mindestens 1 Minute)
        dauer = max(1, int(round(soll_kcal / faktor)))
        
        # Tatsächliche Kalorien neu berechnen
        ist_kcal = dauer * faktor
        
        mix.append([datum, name, str(dauer), str(ist_kcal)])
    
    return mix
