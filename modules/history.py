# modules/history.py

import csv
# Kalorien-Verbrauch (pro Minute)
CALORIE_RATE = {
    "Schwimmen": 9,
    "Yoga": 4,
    "Rennen": 8,
    "Radfahren": 7,
    "Krafttraining": 6,
    "Wandern": 5
}

def calculate_calories(workout_type, duration):
    rate = CALORIE_RATE.get(workout_type, 5)
    return duration * rate

def suggestions(calories, workout_type):
    if calories < 100:
        return "Du könntest ein längeres oder intensiveres Workout machen."
    elif calories < 300:
        return f"Du kannst dein {workout_type}-Training ein wenig steigern."
    else:
        return "Super! Du hast heute genug Kalorien verbrannt."

def show_history(csv_file="data/workout_log.csv"):
    """Zeigt die Trainingshistorie an, optional gefiltert nach Monat oder Workout-Typ."""
    import csv

    WORKOUT_TYPES = ["Schwimmen", "Yoga", "Rennen", "Radfahren", "Krafttraining", "Wandern"]

    try:
        # Alle Daten lesen
        with open(csv_file, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            data = [row for row in reader if row]  # leere Zeilen überspringen

        if not data:
            print("Keine Einträge gefunden.")
            return

        # Filter-Optionen
        print("\nMöchten Sie die Historie filtern?")
        print("1 - Alle anzeigen")
        print("2 - Nach Monat filtern")
        print("3 - Nach Workout-Typ filtern")
        filter_choice = input("Auswahl: ")

        filtered_data = []

        if filter_choice == "1":
            filtered_data = data

        elif filter_choice == "2":
            month = input("Monat eingeben (MM): ").zfill(2)
            year = input("Jahr eingeben (YYYY): ")
            for row in data:
                if "." in row[0]:
                    date_str = row[0]
                else:
                    date_str = row[2]
                try:
                    _, row_month, row_year = date_str.split(".")
                except ValueError:
                    continue
                if row_month == month and row_year == year:
                    filtered_data.append(row)

        elif filter_choice == "3":
            #  Выводим все доступные типы с номерами
            print("\nVerfügbare Workout-Typen:")
            for i, w in enumerate(WORKOUT_TYPES, start=1):
                print(f"{i} - {w}")

            choice = input("Bitte wählen Sie den Workout-Typ (Nummer): ")
            if not choice.isdigit() or int(choice) < 1 or int(choice) > len(WORKOUT_TYPES):
                print("Ungültige Auswahl, zeige alle Daten.")
                filtered_data = data
            else:
                selected_type = WORKOUT_TYPES[int(choice)-1]
                for row in data:
                    if "." in row[0]:
                        workout_type = row[1]
                    else:
                        workout_type = row[0]
                    if workout_type == selected_type:
                        filtered_data.append(row)
        else:
            print("Ungültige Auswahl, zeige alle Daten.")
            filtered_data = data

        # Anzeige
        if not filtered_data:
            print("Keine Einträge gefunden.")
            return

        for row in filtered_data:
            if "." in row[0]:
                date = row[0]
                workout_type = row[1]
                duration = int(row[2])
            else:
                workout_type = row[0]
                duration = int(row[1])
                date = row[2]

            calories = calculate_calories(workout_type, duration)
            advice = suggestions(calories, workout_type)

            print("---------------------")
            print(f"Datum     : {date}")
            print(f"Art       : {workout_type}")
            print(f"Dauer     : {duration} Minuten")
            print(f"Kalorien  : {calories} kcal")
            print(f"Empfehlung: {advice}")
            print("---------------------\n")

    except FileNotFoundError:
        print(f"❌ CSV-Datei nicht gefunden: {csv_file}")
    except ValueError:
        print("❌ In der CSV-Datei steht eine ungültige Dauer (keine Zahl)!")
    except Exception as e:
        print(f"❌ Unbekannter Fehler: {e}")
