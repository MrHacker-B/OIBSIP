# Advanced BMI Calculator

## Project Overview

The Advanced BMI Calculator is a Python desktop application developed using Tkinter. It calculates a user's Body Mass Index (BMI), classifies the result into standard health categories, stores records in an SQLite database, and displays BMI history and trend graphs.

This project satisfies the Advanced Tier requirements by combining GUI development, database management, data validation, and data visualization.

---

## Features

- Graphical User Interface (GUI) using Tkinter
- BMI calculation using the standard formula
- BMI classification:
  - Underweight
  - Normal
  - Overweight
  - Obese
- Color-coded BMI results
- Input validation
- Multi-user support
- SQLite database for storing BMI records
- View historical BMI records
- BMI trend graph using Matplotlib

---

## Technologies Used

- Python 3.x
- Tkinter
- SQLite3
- Matplotlib

---

## Project Structure

BMI_Calculator/

├── main.py

├── bmi_utils.py

├── database.py

├── bmi_records.db (created automatically)

├── requirements.txt

└── README.md

---

## Installation

1. Clone or download the project.

2. Install the required package:

pip install -r requirements.txt

3. Run the application:

python main.py

---

## BMI Formula

BMI = Weight (kg) / Height² (m²)

---

## BMI Categories

| BMI Range | Category |
|-----------|-----------|
| Less than 18.5 | Underweight |
| 18.5 – 24.9 | Normal |
| 25.0 – 29.9 | Overweight |
| 30.0 and above | Obese |

---

## Author

Name: Harsh

Python Advanced BMI Calculator Project