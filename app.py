from modules.ui import display_menu, get_menu_choice, get_workout_type_choice, get_duration, get_date
from modules.storage import save_workout
from modules.workout import edit_workout
from modules.history import show_history


def main():
    """Main program loop"""

    while True:
        # Show the main menu
        display_menu()

        # Get user's choice
        choice = get_menu_choice()

        # Handle different menu options
        if choice == "1":
            # Add new workout
            print("\n--- Neues Workout hinzufügen ---")
            workout_type = get_workout_type_choice()
            duration = get_duration()
            date = get_date()
            save_workout(workout_type,duration,date) # saved to database/CSV

            
            print(f"\n✅ Workout gespeichert! ({date}, {workout_type}, {duration} min)")

        elif choice == "2":
            # Mutate/Update workout
            print("\n--- Workout mutieren ---")
            edit_workout()

        elif choice == "3":
            # Delete workout
            print("\n--- Workout löschen ---")
            print("(Diese Funktion kommt später)")

        elif choice == "4":
            # View history
            print("\n--- Historie einsehen ---")
            show_history()

        elif choice == "0":
            print("\nAuf Wiedersehen!")
            break


# This runs the program
if __name__ == "__main__":
    main()
