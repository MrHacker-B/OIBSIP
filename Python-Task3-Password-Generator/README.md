# 🔐 Advanced Password Generator

A secure desktop application built with Python and Tkinter that generates strong, customizable passwords using Python's `secrets` module.

## 📌 Features

- Secure password generation using the `secrets` module
- Adjustable password length (8–64 characters)
- Include uppercase letters
- Include lowercase letters
- Include numbers
- Include special symbols
- Exclude ambiguous characters (O, 0, I, l, 1)
- Password strength indicator
- Auto-copy password to clipboard
- Copy password button
- Show/Hide password
- Reset all settings
- Password history (last 5 generated passwords)
- Export password history to a text file

## 🛠️ Technologies Used

- Python 3
- Tkinter
- secrets
- pyperclip

## 📂 Project Structure

```
Password-Generator/
│── main.py
│── gui.py
│── password_generator.py
│── requirements.txt
│── README.md
│── password_history.txt
│── build/
│── dist/
└── assets/
```

## 🚀 Installation

1. Clone or download this repository.

2. Install the required package:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
python main.py
```

## 📦 Build Executable

To create a standalone Windows executable:

```bash
pip install pyinstaller
pyinstaller --onefile --windowed main.py
```

The executable will be created inside the `dist` folder.

## 👨‍💻 Author

Developed by **Singh Badrivishal Rananjay** as part of a Python Internship Project.

## 📄 License

This project is for educational and internship purposes.