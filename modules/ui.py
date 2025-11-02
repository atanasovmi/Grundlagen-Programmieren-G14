from rich.console import Console
from rich.table import Table
import inquirer

console = Console()


def show_main_menu():
    """Interaktives Hauptmenü durch inquirer Modul"""
    questions = [
        inquirer.List(
            'action',
            message='Hauptmenü - Was möchtest du tun?',
            choices=[
                '1. Training hinzufügen',
                '2. Training bearbeiten',
                '3. Training löschen',
                '4. Historie anzeigen',
                '0. Beenden',
            ],
        ),
    ]
    answer = inquirer.prompt(questions)
    return answer['action'][0]  # Gibt '1', '2', '3', etc zurück


def display_workouts_table(workouts):
    """Workouts als fertige Tabelle anzeigen"""
    table = Table(title='Trainingshistorie')
    table.add_column('Datum', style='cyan')
    table.add_column('Übung', style='magenta')
    table.add_column('Dauer (min)', style='green')

    for w in workouts:
        table.add_row(w.date, w.exercise_type, str(w.duration_minutes))

    console.print(table)
show_main_menu()
display_workouts_table()