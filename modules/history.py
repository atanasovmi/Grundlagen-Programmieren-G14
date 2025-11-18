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

def show_history(csv_file="workout_log.csv"):
    """Zeigt die Trainingshistorie aus der CSV-Datei in der Konsole an."""
    try:
        with open(csv_file, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            data_found = False
            for row in reader:
                if not row:
                    continue
                data_found = True
                # Format erkennen
                # Format A → "Schwimmen,10,01.01.2025"
                # Format B → "01.01.2025,Schwimmen,10"
                if "." in row[0]:  # date, workout_type, duration
                    date = row[0]
                    workout_type = row[1]
                    duration = int(row[2])
                else:  # workout_type, duration, date
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

            if not data_found:
                print("Keine Einträge gefunden.")

    except FileNotFoundError:
        print(f"❌ CSV-Datei nicht gefunden: {csv_file}")
    except ValueError:
        print("❌ In der CSV-Datei steht eine ungültige Dauer (keine Zahl)!")
    except Exception as e:
        print(f"❌ Unbekannter Fehler: {e}")

