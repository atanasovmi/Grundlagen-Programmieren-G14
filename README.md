# Grundlagen-Programmieren-G14

Group project for building a workout tracker app with integrated analysis — logging exercises, tracking progress, calculating calories, and learning Git together.

---

## 📝 Analysis

**Problem**

Many fitness enthusiasts struggle to consistently track their workout progress and understand the caloric impact of their training. Manual tracking is cumbersome, error-prone, and doesn't provide immediate feedback on progress over time. Without structured data, it's difficult to maintain motivation and recognize achievements.

**Scenario**

The Workout Tracker app solves this problem by providing a simple, console-based interface where users can log their workouts, track different exercise types, calculate calorie consumption, and review their training history. The application stores all data persistently, allowing users to monitor their progress over weeks and months.

**User stories:**

1. As a user, I want to log a new workout with exercise type and duration so that my training is recorded.
2. As a user, I want to see my workout history to track my progress over time.
3. As a user, I want to update or delete past workout entries to correct mistakes.
4. As a user, I want to calculate calorie consumption based on exercise type and duration.
5. As a user, I want to set personal fitness goals to stay motivated.
6. As a user, I want my data saved automatically so I don't lose my progress.

**Use cases:**

- Add New Workout (select type, enter duration, automatic calorie calculation)
- View Training History (display all logged workouts with dates and statistics)
- Update Workout Data (modify existing entries by date)
- Delete Workout Entry (remove incorrect or unwanted entries)
- Calculate Calories (based on workout type and time)
- Set Personal Goals (define and track fitness targets)
- Save & Exit (persist data to CSV file)

---

## ✅ Project Requirements

Each app must meet the following three criteria in order to be accepted (see also the official project guidelines PDF on Moodle):

1. Interactive app (console input)
2. Data validation (input checking)
3. File processing (read/write)

---

### 1. Interactive App (Console Input)

The application provides a menu-driven console interface that runs in a continuous loop until the user chooses to exit. Users interact with the program through numbered menu options:

**Main Menu:**
1. Log New Workout
2. Update Workout Data
3. Delete Workout Entry
4. View Training History
5. Set Personal Goals
0. Save and Exit

For each function, users are prompted to enter relevant data (workout type, duration, date) via console input. The program validates each input and displays confirmation messages or results before returning to the main menu.

---

### 2. Data Validation

The application validates all user input to ensure data integrity and prevent crashes:

- **Menu selection:** Checks that input is numeric and within valid range (0-5)
if not choice.isdigit() or not (0 <= int(choice) <= 5):
print("⚠️ Invalid choice. Please enter a number between 0 and 5.")
continue

text

- **Workout duration:** Ensures time values are positive numbers
try:
duration = float(input("Enter duration (minutes): "))
if duration <= 0:
print("⚠️ Duration must be greater than zero.")
continue
except ValueError:
print("⚠️ Invalid input. Please enter a numeric value.")
continue

text

- **Date format:** Validates date entries and handles incorrect formats
try:
workout_date = datetime.strptime(date_input, "%Y-%m-%d")
except ValueError:
print("⚠️ Invalid date format. Please use YYYY-MM-DD.")
continue

text

- **Exercise type:** Ensures selection from predefined workout types list
- **Empty input handling:** Prevents blank entries for required fields

These validations ensure a smooth user experience and prevent data corruption.

---

### 3. File Processing

The application reads and writes workout data using CSV files:

**Input file:** `workout_log.csv`
- Contains all logged workouts with the following structure:
Date,Exercise,Duration,Calories
2024-11-15,Running,30,300
2024-11-16,Swimming,45,400
2024-11-17,Yoga,60,200

text
- The file is loaded at program startup to display existing workout history
- If the file doesn't exist, a new one is created automatically

**Output file:** `workout_log.csv` (continuously updated)
- Each new workout is immediately appended to the CSV file
- Updated or deleted entries modify the file to reflect changes
- Format: comma-separated values with headers
- Data persistence ensures no workout data is lost between sessions

**File operations:**
- `read()`: Load existing workout data at startup
- `write()`: Save new workouts immediately after entry
- `update()`: Modify existing entries based on date
- `delete()`: Remove entries and rewrite file

---

## ⚙️ Implementation

### Technology

- **Python 3.x**
- **Environment:** GitHub Codespaces
- **Standard Libraries:** `datetime`, `csv`, `pathlib`, `os`
- **Optional Enhancement Libraries:** `inquirer`, `tabulate`, `rich` (for improved UI)

### 📂 Repository Structure

Grundlagen-Programmieren-G14/
├── main.py # Main program entry point with menu loop
├── data/
│ └── workout_log.csv # Persistent workout data storage
├── models/
│ ├── workout.py # Workout class definition
│ ├── user.py # User profile and goals
│ └── exercise.py # Exercise types and calorie calculations
├── utils/
│ ├── file_handler.py # CSV read/write operations
│ ├── validation.py # Input validation functions
│ └── calculator.py # Calorie calculation logic
├── requirements.txt # Python dependencies (if external libraries used)
└── README.md # This file

text

### How to Run

1. Open the repository in **GitHub Codespaces**
2. Open the **Terminal**
3. Run the main program:
python3 main.py

text

### Libraries Used

**Standard Library (built-in):**
- `datetime`: Handles date operations for workout logging and validation
- `csv`: Reads and writes workout data to CSV files
- `os`: File system operations (checking file existence, path handling)
- `pathlib`: Modern path handling for cross-platform compatibility

**Optional Enhancement Libraries:**
- `inquirer`: Interactive command-line prompts with better UX
- `tabulate`: Formatted table display for workout history
- `rich`: Enhanced console output with colors and formatting

All standard libraries are included with Python 3.x. Optional libraries can be installed via:
pip install -r requirements.txt

text

---

## 👥 Team & Contributions

| Name               | FHNW Handle              | GitHub Handle    | Contribution                                    |
|--------------------|--------------------------|------------------|-------------------------------------------------|
| Atanasov, Mihael   | @Atanasov, Mihael WI TZT 25 | @atanasovmi     | Workout logging functionality & calorie calculator |
| Zvarych, Nataliia  | @Zvarych, Nataliia WI TZT 25 | @NataliaZV33   | Data validation & file handling operations       |
| Ada, Aydin         | @Ada, Aydin WI TZT 25     | @AydinAdaFHNW   | Menu system, history display & documentation     |

---

## 🎯 Technical Implementation

### Python Concepts Used

- **Data Types:** Strings, Floats, Integers, Lists, Dictionaries
- **Control Structures:**
  - `if/elif/else` for decision logic
  - `while` loops for menu system
  - `for` loops for data processing and history display
- **Functions:** Modular functions for each main feature (add_workout, update_workout, delete_workout, view_history, etc.)
- **File Processing:** `open()`, `read()`, `write()`, CSV handling with `csv` module
- **Exception Handling:** `try-except` blocks for input validation and file operations
- **String Operations:** Formatting, parsing dates, data validation
- **Object-Oriented Programming (OOP):** Classes like `Workout`, `User`, `Exercise` for structured data modeling
- **Version Control:** Git branching, commits, pull requests for collaborative development

---

## 🚧 Expected Challenges & Solutions

**Challenge 1: Input Validation**
- **Problem:** Users may enter invalid dates, negative durations, or non-numeric values
- **Solution:** Implement comprehensive validation with clear error messages and input retry loops

**Challenge 2: CSV Data Integrity**
- **Problem:** Risk of data corruption or loss during file operations
- **Solution:** Immediate saving after each entry, file existence checks, backup mechanisms

**Challenge 3: Date Handling**
- **Problem:** Date format inconsistencies and timezone issues
- **Solution:** Use `datetime` module with strict format enforcement (YYYY-MM-DD)

**Challenge 4: Error Handling at Multiple Points**
- **Problem:** Errors can occur during menu navigation, file I/O, calculations, or data display
- **Solution:** Strategic `try-except` blocks at each critical point with user-friendly error messages

**Challenge 5: Progress Visualization**
- **Problem:** Raw data doesn't clearly show trends and achievements
- **Solution:** Calculate statistics (total workouts, total calories, averages) and display formatted summaries

---

## 🤝 Contributing

- This is a student project repository for the Programming Foundations course at FHNW.
- Each team member works on feature branches and submits pull requests.
- Regular commits are required to track individual progress.
- Code reviews are conducted before merging to main branch.

---

## 📝 License

This project is provided for **educational use only** as part of the Programming Foundations module at FHNW.

[MIT License](LICENSE)

---

## 📞 Contact

For questions about this project, please contact the team members via their GitHub handles listed above or through the FHNW course platform.