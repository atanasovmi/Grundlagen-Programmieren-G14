
def display_menu():
    """
    Displays the main menu to the user.
    Shows all available options for the workout tracker.
    """
    print("\n" + "=" * 40)
    print("      WORKOUT TRACKER HAUPTMENÜ")
    print("=" * 40)
    print("1 - Neues Workout hinzufügen")
    print("2 - Workout mutieren")
    print("3 - Workout löschen")
    print("4 - Historie einsehen")
    print("0 - Programm beenden")
    print("=" * 40)


def get_menu_choice():
    """
    Gets the user's menu choice and validates it.

    Returns:
        str: The user's choice (0, 1, 2, 3, or 4)
    """
    while True:
        choice = input("\nBitte wählen Sie eine Option (0-4): ")

        # Validate that the input is a valid menu option
        if choice in ["0", "1", "2", "3", "4"]:
            return choice
        else:
            print("❌ Ungültige Eingabe! Bitte geben Sie eine Zahl zwischen 0 und 4 ein.")


def get_workout_type_choice():
    """Gets the user's workout type selection."""

    workout_types = [
        "Schwimmen", "Yoga", "Rennen",
        "Radfahren", "Krafttraining", "Wandern"
    ]

    print("\n" + "-" * 40)
    print("Verfügbare Workout-Typen:")
    print("-" * 40)

    for i, workout in enumerate(workout_types, start=1):
        print(f"{i} - {workout}")

    print("-" * 40)

    while True:
        choice = input("Bitte wählen Sie (1-6): ")

        if choice.isdigit() and 1 <= int(choice) <= len(workout_types):
            return workout_types[int(choice) - 1]

        print("❌ Ungültige Eingabe!")


def get_duration():
    """
    Gets the workout duration (in minutes) from the user and validates it.

    Returns:
        int: The duration in minutes
    """
    while True:
        duration = input("Wie lange war das Workout? (Minuten): ")

        # Validate that the input is a positive number
        if duration.isdigit():
            duration_value = int(duration)

            if duration_value > 0:
                return duration_value
            else:
                print("❌ Die Dauer muss grösser als 0 Minuten sein.")
        else:
            print("❌ Ungültige Eingabe! Bitte geben Sie eine positive Zahl ein.")


def get_date():
    """
    Gets the date from the user in our Swiss format.
    Format: DD.MM.YYYY (e.g., 10.11.2025)

    Returns:
        str: The date in DD.MM.YYYY format
    """
    while True:
        date = input("Geben Sie das Datum ein (DD.MM.YYYY): ")

        # Check if the format is correct (DD.MM.YYYY)
        if len(date) == 10 and date[2] == "." and date[5] == ".":
            try:
                # Split the date into parts
                parts = date.split(".")
                day = int(parts[0])
                month = int(parts[1])
                year = int(parts[2])

                # Simple date validation
                if 1 <= month <= 12 and 1 <= day <= 31:
                    return date
                else:
                    print("❌ Ungültiges Datum! Tag (1-31), Monat (1-12).")
            except ValueError:
                print("❌ Ungültige Eingabe! Bitte verwenden Sie das Format DD.MM.YYYY.")
        else:
            print("❌ Ungültiges Format! Bitte verwenden Sie DD.MM.YYYY (z.B. 10.11.2025).")

def show_confirmation(message):
    """
    Shows a confirmation message to the user.

    Args:
        message (str): The message to display
    """
    print("\n" + "=" * 40)
    print(f"✅ {message}")
    print("=" * 40)


def show_error(message):
    """
    Shows an error message to the user.

    Args:
        message (str): The error message to display
    """
    print("\n" + "=" * 40)
    print(f"❌ Fehler: {message}")
    print("=" * 40)


def show_info(message):
    """
    Shows an information message to the user.

    Args:
        message (str): The information message to display
    """
    print("\n" + "-" * 40)
    print(f"ℹ️ {message}")
    print("-" * 40)
