import tkinter as tk
from tkinter import ttk, messagebox
import pyperclip
from datetime import datetime
from password_generator import generate_password


class PasswordGeneratorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🔐 Advanced Password Generator")
        self.root.geometry("550x700")
        self.root.resizable(False, False)

        self.history = []

        # Variables
        self.length = tk.IntVar(value=16)

        self.uppercase = tk.BooleanVar(value=True)
        self.lowercase = tk.BooleanVar(value=True)
        self.numbers = tk.BooleanVar(value=True)
        self.symbols = tk.BooleanVar(value=True)
        self.exclude = tk.BooleanVar(value=False)

        self.password = tk.StringVar()
        self.show_password = tk.BooleanVar(value=False)

        style = ttk.Style()
        style.theme_use("clam")

        self.root.configure(bg="#1e1e1e")

        style.configure("TCheckbutton",
                        background="#1e1e1e",
                        foreground="white",
                        font=("Segoe UI", 10))

        style.configure("TLabel",
                        background="#1e1e1e",
                        foreground="white")

        style.configure("TButton",
                        font=("Segoe UI", 10))
        self.build_ui()

    def build_ui(self):

        title = tk.Label(
            self.root,
            text="🔐 Advanced Password Generator",
            font=("Arial", 18, "bold")
        )
        title.pack(pady=15)

        tk.Label(
            self.root,
            text="Password Length",
            font=("Arial", 11)
        ).pack()

        tk.Scale(
            self.root,
            from_=8,
            to=64,
            orient="horizontal",
            variable=self.length,
            length=300
        ).pack()

        ttk.Checkbutton(
            self.root,
            text="Uppercase Letters",
            variable=self.uppercase
        ).pack(anchor="w", padx=30)

        ttk.Checkbutton(
            self.root,
            text="Lowercase Letters",
            variable=self.lowercase
        ).pack(anchor="w", padx=30)

        ttk.Checkbutton(
            self.root,
            text="Numbers",
            variable=self.numbers
        ).pack(anchor="w", padx=30)

        ttk.Checkbutton(
            self.root,
            text="Symbols",
            variable=self.symbols
        ).pack(anchor="w", padx=30)

        ttk.Checkbutton(
            self.root,
            text="Exclude Similar Characters (O,0,I,l,1)",
            variable=self.exclude
        ).pack(anchor="w", padx=30)

        tk.Label(
            self.root,
            text="Generated Password",
            font=("Arial", 11, "bold")
        ).pack(pady=(20, 5))

        self.password_entry = tk.Entry(
            self.root,
            textvariable=self.password,
            width=40,
            font=("Consolas", 14),
            justify="center",
            show="*"
        )
        self.password_entry.pack()

        ttk.Checkbutton(
            self.root,
            text="Show Password",
            variable=self.show_password,
            command=self.toggle_password
        ).pack()

        tk.Label(
            self.root,
            text="Password Strength",
            font=("Arial", 11, "bold")
        ).pack(pady=(20, 5))

        self.strength_bar = ttk.Progressbar(
            self.root,
            orient="horizontal",
            length=300,
            mode="determinate",
            maximum=100
        )
        self.strength_bar.pack()

        self.strength_label = tk.Label(
            self.root,
            text="Strength: ---",
            font=("Arial", 11, "bold")
        )
        self.strength_label.pack(pady=5)

        tk.Button(
            self.root,
            text="Generate Password",
            width=20,
            command=self.generate
        ).pack(pady=5)

        tk.Button(
            self.root,
            text="Copy Password",
            width=20,
            command=self.copy_password
        ).pack(pady=5)

        tk.Button(
            self.root,
            text="Export History",
            width=20,
            command=self.export_history
        ).pack(pady=5)

        tk.Button(
            self.root,
            text="Clear History",
            width=20,
            command=self.clear_history
        ).pack(pady=5)

        tk.Button(
            self.root,
            text="Reset",
            width=20,
            command=self.reset
        ).pack(pady=5)

        tk.Label(
            self.root,
            text="Last 5 Generated Passwords",
            font=("Arial", 11, "bold")
        ).pack(pady=(20, 5))

        self.history_box = tk.Listbox(
            self.root,
            width=50,
            height=5
        )
        self.history_box.pack()

        self.status = tk.Label(
            self.root,
            text="Ready",
            bd=1,
            relief=tk.SUNKEN,
            anchor="w",
            bg="#2b2b2b",
            fg="white"
        )
 
        self.status.config(text="Password generated and copied to clipboard.")

    def generate(self):

        try:
            password = generate_password(
                self.length.get(),
                self.uppercase.get(),
                self.lowercase.get(),
                self.numbers.get(),
                self.symbols.get(),
                self.exclude.get()
            )

            self.password.set(password)

            pyperclip.copy(password)

            self.update_strength(password)

            self.update_history(password)

        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def copy_password(self):

        if self.password.get():
            pyperclip.copy(self.password.get())
            messagebox.showinfo("Copied", "Password copied to clipboard!")

    def toggle_password(self):

        if self.show_password.get():
            self.password_entry.config(show="")
        else:
            self.password_entry.config(show="*")

    def update_strength(self, password):

        score = 0

        if len(password) >= 8:
            score += 20

        if len(password) >= 12:
            score += 20

        if any(c.isupper() for c in password):
            score += 15

        if any(c.islower() for c in password):
            score += 15

        if any(c.isdigit() for c in password):
            score += 15

        if any(not c.isalnum() for c in password):
            score += 15

        self.strength_bar["value"] = score

        style = ttk.Style()

        if score < 50:
            style.configure("red.Horizontal.TProgressbar",
                            troughcolor="#444",
                            background="red")
            self.strength_bar.configure(style="red.Horizontal.TProgressbar")
            self.strength_label.config(text="Weak 🔴")

        elif score < 80:
            style.configure("yellow.Horizontal.TProgressbar",
                            troughcolor="#444",
                            background="orange")
            self.strength_bar.configure(style="yellow.Horizontal.TProgressbar")
            self.strength_label.config(text="Medium 🟡")

        else:
            style.configure("green.Horizontal.TProgressbar",
                            troughcolor="#444",
                            background="green")
            self.strength_bar.configure(style="green.Horizontal.TProgressbar")
            self.strength_label.config(text="Strong 🟢")

    def update_history(self, password):

        current_time = datetime.now().strftime("%H:%M:%S")

        entry = f"{current_time}  |  {password}"

        self.history.insert(0, entry)

        self.history = self.history[:5]

        self.history_box.delete(0, tk.END)

        for item in self.history:
            self.history_box.insert(tk.END, item)

    def export_history(self):

        if not self.history:
            messagebox.showwarning(
            "No History",
            "No passwords available."
            )
            return

        with open("password_history.txt", "w") as file:
            for item in self.history:
                file.write(item + "\n")

        messagebox.showinfo(
            "Success",
            "History exported successfully!"
        )

    def clear_history(self):

        self.history.clear()

        self.history_box.delete(0, tk.END)   

    def reset(self):

        self.length.set(16)

        self.uppercase.set(True)
        self.lowercase.set(True)
        self.numbers.set(True)
        self.symbols.set(True)
        self.exclude.set(False)

        self.show_password.set(False)

        self.password.set("")

        self.password_entry.config(show="*")

        self.strength_bar["value"] = 0

        self.strength_label.config(text="Strength: ---")

        self.history.clear()

        self.history_box.delete(0, tk.END)