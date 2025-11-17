
import os  # Importiert das Modul für Dateipfade und Ordner


WORKOUT_FILE = "data/workout_log.csv"

def save_workout(workout_type,duration,date):
    

    # Alles in Strings umwandeln
    date = str(date)
    workout_type = str(workout_type)
    duration = str(duration)

    # Prüfen, ob der Ordner "data" existiert; wenn nicht, erstelle ihn
    if not os.path.exists("data"):
        os.makedirs("data")  # Ordner "data" wird erstellt


    with open(WORKOUT_FILE, "a") as file:
        file.write(f"{date},{workout_type},{duration}\n")  # Zeile wird in CSV-Format gespeichert


