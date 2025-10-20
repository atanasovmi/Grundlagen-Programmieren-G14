import csv
from datetime import datetime

CSV_FILE = "workout_log.csv"
# ***Kalorienfaktoren (Beispielwerte, ca. MET bei 70kg)****
# Aktivität                        | MET-Wert |
# Sitzen, Ruhe                     | 1        |
# Leichter Spaziergang (2–3 km/h)  | 2–3      |
# Mittlerer Spaziergang (4–5 km/h) | 3–4      |
# Fahrradfahren (leicht)           | 4        |
# Hausarbeit / Reinigung           | 3–4      |
# Leichtes Joggen (8 km/h)         | 8        |
# Laufen (10 km/h)                 | 10       |
# Schwimmen (mittleres Tempo)      | 6–8      |
# Yoga                             | 2–3      |
# Aerobic / Tanz                   | 5–7      |
# Krafttraining (mittel)           | 3–6      |
# Hochintensives Training          | 8–12     |


# Kalorienverbrauch berechnen
# -----Formel:-----
# Kalorienverbrauch (kcal)= MET×Körpergewicht (kg)×Dauer (Stunden)
# Beispiel:
# . Person: 70 kg
# . Aktivität: Joggen 8 km/h (8 MET)
# . Dauer: 1 Stunde
#   8 × 70 × 1 = 560 kcal
# Hinweis: MET-Werte sind Richtwerte und können je nach Intensität und Fitnessniveau variieren.
CALORIE_FACTORS = {
    "Laufen": 10,
    "Schwimmen": 8,
    "Yoga": 3,
    "Radfahren": 7,
    "Krafttraining": 6
}
SPORT_ART = ["Laufen", "Schwimmen", "Yoga", "Radfahren", "Krafttraining"]

def workout_hinzufuegen():
    while True:
        print("\n--- Übungsauswahl ---")
        for i, sport in enumerate(SPORT_ART, 1):
            print(f"{i}. {sport}")
        print("0 = Zurück zum Hauptmenü")

        try:
            wahl = int(input("Wähle eine Sportart: "))
        except ValueError:
            print("Ungültige Eingabe!")
            continue

        if wahl == 0:
            break
        elif 1 <= wahl <= len(SPORT_ART):
            print(f"Du hast '{SPORT_ART[wahl - 1]}' ausgewählt (nur Anzeige, keine Berechnung).")
        else:
            print("Ungültige Auswahl!")
def lade_daten():
    pass

def speichere_daten(daten):
    pass
    
def workout_anzeigen():
    pass
def workout_loeschen():
    pass
def workout_mutieren():
    pass
def menue():
    while True:
        print("\n--- Workout Tracker ---")
        print("1 = Neues Workout hinzufügen")
        print("2 = Workout mutieren")
        print("3 = Workout löschen")
        print("4 = Historie anzeigen")
        print("0 = Beenden")

        wahl = input("Option wählen: ")
        if wahl == "1":
            workout_hinzufuegen()
        elif wahl == "2":
            workout_mutieren()
        elif wahl == "3":
            workout_loeschen()
        elif wahl == "4":
            workout_anzeigen()
        elif wahl == "0":
            print("Programm beendet. Daten gespeichert.")
            break
        else:
            print("Ungültige Auswahl!")


menue()

