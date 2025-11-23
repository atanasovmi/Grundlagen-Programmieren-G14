from datetime import datetime

# Modul für die Validierung von Benutzereingaben
# Enthält Funktionen zur Prüfung von Datum, Zahlen und Text

def validiere_datum(datum_text):
    """
    Prüft, ob der eingegebene Text ein gültiges Datum im Format TT.MM.JJJJ ist.
    Wirft einen ValueError, wenn das Format falsch ist.
    """
    try:
        # Versuche, den Text in ein Datum umzuwandeln
        datetime.strptime(datum_text, '%d.%m.%Y')
        return datum_text
    except ValueError:
        # Wenn das Parsen fehlschlägt, ist das Format ungültig
        raise ValueError("Ungültiges Datumsformat. Bitte TT.MM.JJJJ verwenden.")

def validiere_ganzzahl(text):
    """
    Prüft, ob der eingegebene Text eine positive ganze Zahl ist.
    Wirft einen ValueError, wenn keine gültige Zahl eingegeben wurde.
    """
    try:
        zahl = int(text)
        if zahl < 0:
             raise ValueError("Die Zahl muss positiv sein.")
        return zahl
    except ValueError:
        raise ValueError("Ungültige Eingabe. Bitte eine ganze Zahl eingeben.")

def validiere_nicht_leer(text):
    """
    Prüft, ob der eingegebene Text nicht leer ist.
    Wirft einen ValueError, wenn der Text leer ist.
    """
    if not text or text.strip() == "":
        raise ValueError("Eingabe darf nicht leer sein.")
    return text.strip()

def validiere_monat_jahr(text):
    """
    Prüft, ob der Text dem Format MM.JJJJ entspricht.
    """
    try:
        datetime.strptime(text, '%m.%Y')
        return text
    except ValueError:
        raise ValueError("Ungültiges Format. Bitte MM.JJJJ verwenden.")

def validiere_monat(text):
    """
    Prüft, ob der Text ein gültiger Monat (1-12) ist.
    Gibt den Monat als zweistelligen String zurück (z.B. '01').
    """
    try:
        monat = int(text)
        if 1 <= monat <= 12:
            return f"{monat:02d}"
        else:
            raise ValueError("Monat muss zwischen 1 und 12 liegen.")
    except ValueError:
        raise ValueError("Bitte eine Zahl zwischen 1 und 12 eingeben.")
