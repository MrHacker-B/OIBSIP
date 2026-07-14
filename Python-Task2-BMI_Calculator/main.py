import tkinter as tk
from tkinter import messagebox

from bmi_utils import calculate_bmi, classify_bmi
from database import create_database, save_record, fetch_records
import matplotlib.pyplot as plt

create_database()

window = tk.Tk()
window.title("BMI Calculator")
window.geometry("400x450")


tk.Label(window, text="Name").pack()
name_entry = tk.Entry(window)
name_entry.pack()

tk.Label(window, text="Weight (kg)").pack()
weight_entry = tk.Entry(window)
weight_entry.pack()

tk.Label(window, text="Height (m)").pack()
height_entry = tk.Entry(window)
height_entry.pack()

result = tk.Label(window, text="", font=("Arial", 14))
result.pack(pady=20)


def calculate():
    try:
        name = name_entry.get()

        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight <= 0 or height <= 0:
            messagebox.showerror("Error", "Enter positive values.")
            return

        bmi = calculate_bmi(weight, height)

        category = classify_bmi(bmi)

        colors = {
            "Underweight": "blue",
            "Normal": "green",
            "Overweight": "orange",
            "Obese": "red"
        }

        result.config(
            text=f"BMI : {bmi}\nCategory : {category}",
            fg=colors[category]
        )

        save_record(name, weight, height, bmi, category)

    except ValueError:
        messagebox.showerror("Error", "Enter valid numbers.")


def view_history():
    name = name_entry.get()

    if not name:
        messagebox.showerror("Error", "Enter a name.")
        return

    records = fetch_records(name)

    if not records:
        messagebox.showinfo("History", "No records found.")
        return

    text = ""

    for i, record in enumerate(records, start=1):
        bmi, category = record
        text += f"{i}. BMI: {bmi}   {category}\n"

    messagebox.showinfo(f"{name}'s History", text)


def show_graph():
    name = name_entry.get()

    if not name:
        messagebox.showerror("Error", "Enter a name.")
        return

    records = fetch_records(name)

    if not records:
        messagebox.showinfo("Graph", "No records found.")
        return

    bmi_values = [record[0] for record in records]

    plt.plot(range(1, len(bmi_values)+1), bmi_values, marker="o")

    plt.title(f"{name}'s BMI Trend")
    plt.xlabel("Record Number")
    plt.ylabel("BMI")

    plt.grid(True)

    plt.show()

tk.Button(window, text="Calculate BMI", command=calculate).pack()
tk.Button(window, text="View History", command=view_history).pack()
tk.Button(window, text="Show Graph", command=show_graph).pack()
window.mainloop()