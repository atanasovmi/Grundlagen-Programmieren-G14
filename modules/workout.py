def edit_workout(csv_file="data/workout_log.csv"):
    """Erlaubt das Bearbeiten von Workouts nach Monat/Jahr."""
    import csv

    try:
        # 1️⃣ Datei öffnen und alle Daten lesen
        with open(csv_file, "r", newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            data = list(reader)  # Alle Zeilen in eine Liste speichern

        if not data:
            print("Keine Einträge zum Bearbeiten.")
            return

        # 2️⃣ Benutzer gibt Monat und Jahr ein
        month = input("Geben Sie den Monat ein (MM): ").zfill(2)  # z.B. "1" → "01"
        year = input("Geben Sie das Jahr ein (YYYY): ")

        # 3️⃣ Filter: nur Einträge für diesen Monat und Jahr
        filtered = []
        for i, row in enumerate(data):
            if not row:  # Leere Zeilen überspringen
                continue

            date_str = row[0]  # Immer das erste Feld ist das Datum
            try:
                day, row_month, row_year = date_str.split(".")
            except ValueError:
                continue  # Wenn Datum falsch formatiert, überspringen

            if row_month == month and row_year == year:
                filtered.append((i, row))  # Index und Zeile merken

        if not filtered:
            print(f"Keine Einträge für {month}.{year} gefunden.")
            return

        # 4️⃣ Gefilterte Einträge anzeigen
        print(f"\n--- Workouts im {month}.{year} ---")
        for idx, (i, row) in enumerate(filtered, start=1):
            date = row[0]
            workout_type = row[1]
            duration = row[2]
            print(f"{idx}: {date}, {workout_type}, {duration} min")

        # 5️⃣ Benutzer wählt die Zeile
        choice = input("Welche Zeile möchten Sie ändern? (Nummer): ")
        if not choice.isdigit() or int(choice) < 1 or int(choice) > len(filtered):
            print("Ungültige Auswahl.")
            return
        choice = int(choice) - 1
        data_index, selected_row = filtered[choice]

        # 6️⃣ Benutzer wählt, was geändert werden soll
        field = input("Was möchten Sie ändern? (datum/art/dauer): ").lower()
        if field == "datum":
            new_value = input("Neues Datum (dd.mm.yyyy): ")
            data[data_index][0] = new_value
        elif field == "art":
            new_value = input("Neuer Workout-Typ: ")
            data[data_index][1] = new_value
        elif field == "dauer":
            new_value = input("Neue Dauer in Minuten: ")
            if not new_value.isdigit():
                print("Ungültige Eingabe. Dauer muss eine Zahl sein.")
                return
            data[data_index][2] = new_value
        else:
            print("Ungültige Auswahl.")
            return

        # 7️⃣ Daten wieder in die CSV-Datei speichern
        with open(csv_file, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(data)

        print("✅ Eintrag wurde aktualisiert.")

    except FileNotFoundError:
        print(f"❌ CSV-Datei nicht gefunden: {csv_file}")
    except Exception as e:
        print(f"❌ Unbekannter Fehler: {e}")
