# modules/history.py

import csv

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
        return "Daha uzun veya yoğun bir workout yapabilirsin."
    elif calories < 300:
        return f"{workout_type} çalışmalarını biraz artırabilirsin."
    else:
        return "Harika! Bugün yeterince kalori yaktın."

def show_history(csv_file="workout_log.csv"):
    try:
        with open(csv_file, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            data_found = False
            for row in reader:
                if not row:
                    continue
                data_found = True
                # Format kontrolü
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
                print(f"Tarih : {date}")
                print(f"Tür   : {workout_type}")
                print(f"Süre  : {duration} dakika")
                print(f"Kalori: {calories} kcal")
                print(f"Öneri : {advice}")
                print("---------------------\n")

            if not data_found:
                print("Henüz kayıt bulunamadı.")

    except FileNotFoundError:
        print(f"{csv_file} bulunamadı.")
    except Exception as e:
        print(f"Hata: {e}")

