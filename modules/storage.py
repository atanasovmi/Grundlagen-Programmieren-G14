# Modul für die Dateiverarbeitung
# Liest und schreibt Daten in die CSV-Datei
import os

#Meine eigenen Notizen fürs debbuging → Lokaler Error
# Pfad zur CSV-Datei relativ zu diesem Modul
# __file__ ist .../modules/storage.py
# dirname(__file__) ist .../modules
# dirname(dirname(__file__)) ist .../ (Root)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
DATA_PATH = os.path.join(DATA_DIR, 'workout_log.csv')

# Debug-Ausgabe
print(f"DEBUG storage.py: __file__ = {__file__}")
print(f"DEBUG storage.py: BASE_DIR = {BASE_DIR}")
print(f"DEBUG storage.py: DATA_DIR = {DATA_DIR}")
print(f"DEBUG storage.py: DATA_PATH = {DATA_PATH}")

HEADER = "Datum,Übung,Dauer,Kalorien\n"

def _ensure_data_dir():
    """Stellt sicher, dass das data-Verzeichnis existiert."""
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

def lade_daten(datei_name=DATA_PATH):
    """
    Lädt die Trainingsdaten aus der CSV-Datei.
    Ignoriert die Kopfzeile.
    """
    daten = []
    try:
        with open(datei_name, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            if not lines:
                return []
            
            # Prüfen ob erste Zeile Header ist
            start_index = 0
            if lines[0].strip() == HEADER.strip():
                start_index = 1
            
            for line in lines[start_index:]:
                if line.strip():
                    daten.append(line.strip().split(','))
    except FileNotFoundError:
        return []
    return daten

def speichere_daten(datei_name, daten):
    """
    Speichert die gesamte Liste von Trainingsdaten.
    """
    _ensure_data_dir()
    try:
        with open(datei_name, 'w', encoding='utf-8') as file:
            file.write(HEADER)
            for eintrag in daten:
                line = ",".join(eintrag) + "\n"
                file.write(line)
    except Exception as e:
        print(f"Fehler beim Speichern der Datei: {e}")

def speichere_eintrag(datei_name, eintrag_liste):
    """
    Fügt einen einzelnen Eintrag an.
    """
    _ensure_data_dir()
    try:
        datei_existiert = os.path.exists(datei_name)
        
        with open(datei_name, 'a', encoding='utf-8') as file:
            if not datei_existiert or os.path.getsize(datei_name) == 0:
                file.write(HEADER)
            
            line = ",".join(eintrag_liste) + "\n"
            file.write(line)
    except Exception as e:
        print(f"Fehler beim Schreiben in die Datei: {e}")
