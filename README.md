# Grundlagen-Programmieren-G14
Group project for building a simple workout tracker app — logging exercises, tracking progress, and learning Git together.

# Workout Tracker with integrated Analysis

> 🚧 This is a template repository for student project in the course Programming Foundations at FHNW, BSc BIT.  
> 🚧 Do not keep this section in your final submission.

This project is intended to:

- Practice the complete process from **problem analysis to implementation**
- Apply basic **Python** programming concepts learned in the Programming Foundations module
- Demonstrate the use of **console interaction, data validation, and file processing**
- Produce clean, well-structured, and documented code
- Prepare students for **teamwork and documentation** in later modules
- Use this repository as a starting point by importing it into your own GitHub account.  
- Work only within your own copy — do not push to the original template.  
- Commit regularly to track your progress.

# 🍕 TEMPLATE for documentation
> 🚧 Please remove this paragraphs having "🚧". These are comments for preparing the documentations.
## 📝 Analysis

**Problem**
> 🚧 Describe the real-world problem your application solves. (Not HOW, but WHAT)

💡 Example: In a small local pizzeria, the staff writes orders and calculates totals by hand. This causes mistakes and inconsistent orders or discounts.

**Scenario**
> 🚧 Describe when and how a user will use your application

💡 Example: PizzaRP solves the part of the problem where orders and totals are created by letting a user select items from a menu and automatically generating a correct invoice.

**User stories:**
1. As a user, I want to see the pizza menu in the console.
2. As a user, I want to select pizzas and see the running total.
3. As a user, I want discounts to be applied automatically.
4. As a user, I want an invoice to be created and saved as a file.

**Use cases:**
- Show Menu (from `menu.txt`)
- Create Order (choose pizzas)
- Show Current Order and Total
- Print Invoice (to `invoice_xxx.txt`)

---

## ✅ Project Requirements

Each app must meet the following three criteria in order to be accepted (see also the official project guidelines PDF on Moodle):

1. Interactive app (console input)
2. Data validation (input checking)
3. File processing (read/write)

---

### 1. Interactive App (Console Input)

> 🚧 In this section, document how your project fulfills each criterion.  
---
The application interacts with the user via the console. Users can:
- View the pizza menu
- Select pizzas and quantities
- See the running total
- Receive an invoice generated as a file

---


### 2. Data Validation

The application validates all user input to ensure data integrity and a smooth user experience. This is implemented in `main-invoice.py` as follows:

- **Menu selection:** When the user enters a pizza number, the program checks if the input is a digit and within the valid menu range:
	```python
	if not choice.isdigit() or not (1 <= int(choice) <= len(menu)):
			print("⚠️ Invalid choice.")
			continue
	```
	This ensures only valid menu items can be ordered.

- **Menu file validation:** When reading the menu file, the program checks for valid price values and skips invalid lines:
	```python
	try:
			menu.append({"name": name, "size": size, "price": float(price)})
	except ValueError:
			print(f"⚠️ Skipping invalid line: {line.strip()}")
	```

- **Main menu options:** The main menu checks for valid options and handles invalid choices gracefully:
	```python
	else:
			print("⚠️ Invalid choice.")
	```

These checks prevent crashes and guide the user to provide correct input, matching the validation requirements described in the project guidelines.

---

---


### 3. File Processing

The application reads and writes data using files:

- **Input file:** `menu.txt` — Contains the pizza menu, one item per line in the format `PizzaName;Size;Price`.
	- Example:
		```
		Margherita;Medium;12.50
		Salami;Large;15.00
		Funghi;Small;9.00
		```
	- The application reads this file at startup to display available pizzas.

- **Output file:** `invoice_001.txt` (and similar) — Generated when an order is completed. Contains a summary of the order, including items, quantities, prices, discounts, and totals.
	- Example:
		```
		Invoice #001
		----------------------
		1x Margherita (Medium)   12.50


		2x Salami (Large)        30.00
		----------------------
		Total:                  42.50
		Discount:                2.50
		Amount Due:             40.00
		```
		- The output file serves as a record for both the user and the pizzeria, ensuring accuracy and transparency.

## ⚙️ Implementation

### Technology
- Python 3.x
- Environment: GitHub Codespaces
- No external libraries

### 📂 Repository Structure
```text
PizzaRP/
├── main.py             # main program logic (console application)
├── menu.txt            # pizza menu (input data file)
├── invoice_001.txt     # example of a generated invoice (output file)
├── docs/               # optional screenshots or project documentation
└── README.md           # project description and milestones
```

### How to Run
> 🚧 Adjust if needed.
1. Open the repository in **GitHub Codespaces**
2. Open the **Terminal**
3. Run:
	```bash
	python3 main.py
	```

### Libraries Used

- `os`: Used for file and path operations, such as checking if the menu file exists and creating new files.
- `glob`: Used to find all invoice files matching a pattern (e.g., `invoice_*.txt`) to determine the next invoice number.

These libraries are part of the Python standard library, so no external installation is required. They were chosen for their simplicity and effectiveness in handling file management tasks in a console application.


## 👥 Team & Contributions

> 🚧 Fill in the names of all team members and describe their individual contributions below. Each student should be responsible for at least one part of the project.

| Name       | Contribution                                 |
|------------|----------------------------------------------|
| Student A  | Menu reading (file input) and displaying menu|
| Student B  | Order logic and data validation              |
| Student C  | Invoice generation (file output) and slides  |


## 🤝 Contributing

> 🚧 This is a template repository for student projects.  
> 🚧 Do not change this section in your final submission.

- Use this repository as a starting point by importing it into your own GitHub account.  
- Work only within your own copy — do not push to the original template.  
- Commit regularly to track your progress.

## 📝 License

This project is provided for **educational use only** as part of the Programming Foundations module.  
[MIT License](LICENSE)
