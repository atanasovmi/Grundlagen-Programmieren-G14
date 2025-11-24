import modules.validation as v
from datetime import datetime

# Modul für die Benutzeroberfläche
# Enthält Menüs und Eingabeaufforderungen

def zeige_hauptmenue():
    """Zeigt das Hauptmenü an."""
    logo = r""" 
                                                          
                                                     ▄ ▄  
██  ██  ▄▄▄  ▄▄ ▄▄ ▄▄▄▄ ▄▄▄▄▄▄ ▄▄   ▄▄ ▄▄▄▄▄ ▄▄  ▄▄ ▄▄ ▄▄ 
██████ ██▀██ ██ ██ ██▄█▀  ██   ██▀▄▀██ ██▄▄  ███▄██ ██ ██ 
██  ██ ██▀██ ▀███▀ ██     ██   ██   ██ ██▄▄▄ ██ ▀██ ▀███▀
"""
    print(f"\n {logo}")
    print("1. Training eintragen")
    print("2. Training bearbeiten")
    print("3. Training löschen")
    print("4. Historie einsehen")
    print("5. Assistent starten")
    print("0. Beenden")

def frage_datum():
    """Fragt ein Datum ab und validiert es."""
    while True:
        datum_input = input("Datum (TT.MM.JJJJ) [Leer für heute]: ")
        if not datum_input:
            return datetime.now().strftime("%d.%m.%Y")
        try:
            return v.validiere_datum(datum_input)
        except ValueError as e:
            print(f"Fehler: {e}")
        except Exception as e:
            print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")

def frage_datum_oder_abbruch():
    """Fragt ein Datum ab und validiert es. Gibt None zurück bei 0 (Abbruch)."""
    while True:
        datum_input = input("Datum (TT.MM.JJJJ) [Leer für heute, 0 für Abbruch]: ")
        if datum_input == "0":
            return None
        if not datum_input:
            return datetime.now().strftime("%d.%m.%Y")
        try:
            return v.validiere_datum(datum_input)
        except ValueError as e:
            print(f"Fehler: {e}")
        except Exception as e:
            print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")

def frage_uebung(uebungen_dict):
    """
    Zeigt verfügbare Übungen und lässt den Benutzer wählen.
    Gibt (Name, Kcal-Faktor) zurück.
    """
    print("\nVerfügbare Übungen:")
    for key, info in uebungen_dict.items():
        print(f"{key}. {info['name']} ({info['kcal_pro_min']} kcal/min)")
    
    while True:
        auswahl = input("Bitte Nummer der Übung wählen: ")
        if auswahl in uebungen_dict:
            return uebungen_dict[auswahl]["name"], uebungen_dict[auswahl]["kcal_pro_min"]
        else:
            print("Ungültige Auswahl. Bitte eine Nummer aus der Liste wählen.")

def frage_dauer():
    """Fragt die Dauer ab und validiert sie."""
    while True:
        dauer_input = input("Dauer in Minuten: ")
        try:
            return v.validiere_ganzzahl(dauer_input)
        except ValueError as e:
            print(f"Fehler: {e}")
        except Exception as e:
            print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")

def zeige_historie(daten):
    """Gibt die Trainingsdaten tabellarisch aus."""
    print("\n--- Historie ---")
    if not daten:
        print("Noch keine Trainings eingetragen.")
        return

    print(f"{'Datum':<12} | {'Übung':<15} | {'Dauer':<6} | {'Kcal':<6}")
    print("-" * 45)
    for zeile in daten:
        if len(zeile) == 4:
            print(f"{zeile[0]:<12} | {zeile[1]:<15} | {zeile[2]:<6} | {zeile[3]:<6}")
        else:
            print(f"Ungültige Zeile: {zeile}")

def zeige_loesch_menue(treffer):
    """
    Zeigt gefundene Einträge an und lässt den Benutzer einen zum Löschen auswählen.
    Gibt die Nummer der Auswahl zurück (1-basiert) oder 0 für Abbruch.
    """
    print(f"\nGefundene Einträge:")
    for i, (original_index, zeile) in enumerate(treffer):
        print(f"{i + 1}. {zeile[1]} - {zeile[2]} Min - {zeile[3]} kcal")

    while True:
        auswahl_input = input("\nWelchen Eintrag löschen? (Nummer eingeben, 0 für Abbrechen): ")
        try:
            auswahl = v.validiere_ganzzahl(auswahl_input)
            if auswahl == 0:
                return 0
            if 1 <= auswahl <= len(treffer):
                return auswahl
            else:
                print("Ungültige Nummer.")
        except ValueError as e:
            print(f"Fehler: {e}")
        except Exception as e:
            print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")

def zeige_bearbeitungs_menue(treffer):
    """
    Zeigt gefundene Einträge an und lässt den Benutzer einen zum Bearbeiten auswählen.
    Gibt die Nummer der Auswahl zurück (1-basiert) oder 0 für Abbruch.
    """
    print(f"\nGefundene Einträge:")
    for i, (original_index, zeile) in enumerate(treffer):
        print(f"{i + 1}. {zeile[1]} - {zeile[2]} Min - {zeile[3]} kcal")

    while True:
        auswahl_input = input("\nWelchen Eintrag bearbeiten? (Nummer eingeben, 0 für Abbrechen): ")
        try:
            auswahl = v.validiere_ganzzahl(auswahl_input)
            if auswahl == 0:
                return 0
            if 1 <= auswahl <= len(treffer):
                return auswahl
            else:
                print("Ungültige Nummer.")
        except ValueError as e:
            print(f"Fehler: {e}")
        except Exception as e:
            print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")

def frage_monat():
    """
    Fragt nach einem Monat (1-12).
    Gibt den Monat als String 'MM' zurück oder None, wenn leer.
    """
    while True:
        eingabe = input("Filter nach Monat (1-12) [Leer für alle]: ")
        if not eingabe:
            return None
        try:
            return v.validiere_monat(eingabe)
        except ValueError as e:
            print(f"Fehler: {e}")
        except Exception as e:
            print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")

def frage_monat_oder_abbruch():
    """
    Fragt nach einem Monat (1-12).
    Gibt den Monat als String 'MM' zurück, None bei leer, oder False bei 0 (Abbruch).
    """
    while True:
        eingabe = input("Filtriere nach Monat (1-12) [Leer für alle, 0 für Abbruch]: ")
        if eingabe == "0":
            return False
        if not eingabe:
            return None
        try:
            return v.validiere_monat(eingabe)
        except ValueError as e:
            print(f"Fehler: {e}")
        except Exception as e:
            print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")

def frage_jahr(verfuegbare_jahre):
    """
    Lässt den Benutzer ein Jahr aus der Liste auswählen.
    """
    print(f"Einträge gefunden in folgenden Jahren: {', '.join(verfuegbare_jahre)}")
    while True:
        eingabe = input("Bitte Jahr wählen: ")
        if eingabe in verfuegbare_jahre:
            return eingabe
        print("Ungültiges Jahr. Bitte eines der angezeigten Jahre wählen.")

def frage_kalorien_ziel():
    """Fragt das Kalorienziel ab."""
    while True:
        try:
            ziel_input = input("Mein Ziel sind heute (kcal): ")
            ziel = int(ziel_input)
            if ziel > 0:
                return ziel
            print("Bitte eine positive Zahl eingeben.")
        except ValueError:
            print("Ungültige Eingabe. Bitte eine ganze Zahl eingeben.")
        except Exception as e:
            print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")

def zeige_empfehlung_menue():
    """
    Fragt den User nach der Aktion für die Empfehlung.
    """
    print("\nMöchten Sie diese Empfehlung übernehmen?")
    print("1. Workout speichern (Viel Spass!)")
    print("2. Neue Empfehlung generieren")
    print("0. Zurück zum Hauptmenü")
    
    while True:
        wahl = input("Ihre Wahl: ")
        if wahl in ['0', '1', '2']:
            return wahl
        print("Ungültige Wahl.")

def zeige_feld_auswahl_menue(eintrag):
    """
    Zeigt die Felder eines Eintrags und lässt den Benutzer wählen, was bearbeitet werden soll.
    eintrag: [Datum, Übung, Dauer, Kalorien]
    Gibt die Nummer der Auswahl (1-3) zurück oder 0 für Fertig.
    """
    print("\nAktueller Eintrag:")
    print(f"Datum: {eintrag[0]}")
    print(f"Übung: {eintrag[1]}")
    print(f"Dauer: {eintrag[2]} Min")
    print(f"Kalorien: {eintrag[3]} kcal (wird automatisch neu berechnet)")
    
    print("\nWas möchten Sie bearbeiten?")
    print("1. Datum")
    print("2. Übung")
    print("3. Dauer")
    print("0. Fertig / Speichern")
    
    while True:
        auswahl_input = input("Ihre Wahl: ")
        try:
            auswahl = v.validiere_ganzzahl(auswahl_input)
            if 0 <= auswahl <= 3:
                return auswahl
            else:
                print("Bitte 0-3 wählen.")
        except ValueError as e:
            print(f"Fehler: {e}")
        except Exception as e:
            print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")