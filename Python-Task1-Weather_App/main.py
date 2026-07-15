import tkinter as tk
from tkinter import messagebox
from weather_api import get_current_weather, get_forecast
import requests
from PIL import Image, ImageTk
from io import BytesIO
from datetime import datetime

current_unit = "metric"

def show_forecast(city):
    forecast = get_forecast(city, current_unit)
    if "error" in forecast:
        forecast_text.delete("1.0", tk.END)
        forecast_text.insert(tk.END, forecast["error"])
        return
    forecast_text.delete("1.0", tk.END)
    shown=set()
    symbol="°C" if current_unit=="metric" else "°F"
    for item in forecast["list"]:
        d=item["dt_txt"].split()[0]
        if d not in shown:
            shown.add(d)
            forecast_text.insert(tk.END,f"{d}  {item['main']['temp']}{symbol}  {item['weather'][0]['main']}\n")
        if len(shown)==5:
            break

def toggle_unit():
    global current_unit
    current_unit="imperial" if current_unit=="metric" else "metric"
    unit_button.config(text="Switch to °C" if current_unit=="imperial" else "Switch to °F")
    if city_entry.get().strip():
        fetch_weather()

def fetch_weather():
    city=city_entry.get().strip()
    if not city:
        messagebox.showerror("Error","Enter a city")
        return
    w=get_current_weather(city,current_unit)
    if "error" in w:
        messagebox.showerror("Error",w["error"])
        return
    icon=requests.get(f"https://openweathermap.org/img/wn/{w['weather'][0]['icon']}@2x.png")
    photo=ImageTk.PhotoImage(Image.open(BytesIO(icon.content)))
    icon_label.config(image=photo); icon_label.image=photo
    s="°C" if current_unit=="metric" else "°F"
    city_label.config(text=w["name"])
    temp_label.config(text=f"Temperature: {w['main']['temp']}{s}")
    feels_label.config(text=f"Feels Like: {w['main']['feels_like']}{s}")
    maxmin_label.config(text=f"Max/Min: {w['main']['temp_max']}/{w['main']['temp_min']}{s}")
    humidity_label.config(text=f"Humidity: {w['main']['humidity']}%")
    condition_label.config(text=f"Condition: {w['weather'][0]['description'].title()}")
    wind_label.config(text=f"Wind: {w['wind']['speed']} m/s")
    pressure_label.config(text=f"Pressure: {w['main']['pressure']} hPa")
    visibility_label.config(text=f"Visibility: {w['visibility']/1000:.1f} km")
    sunrise_label.config(text="Sunrise: "+datetime.fromtimestamp(w["sys"]["sunrise"]).strftime("%I:%M %p"))
    sunset_label.config(text="Sunset: "+datetime.fromtimestamp(w["sys"]["sunset"]).strftime("%I:%M %p"))
    show_forecast(city)

root=tk.Tk()
root.title("Advanced Weather App")
root.geometry("600x850")
root.configure(bg="#87CEEB")

tk.Label(root,text="🌤 Advanced Weather App",font=("Arial",20,"bold"),bg="#87CEEB").pack(pady=10)
city_entry=tk.Entry(root,font=("Arial",14),justify="center")
city_entry.pack()
tk.Button(root,text="Get Weather",command=fetch_weather).pack(pady=5)
unit_button=tk.Button(root,text="Switch to °F",command=toggle_unit)
unit_button.pack()

icon_label=tk.Label(root,bg="#87CEEB"); icon_label.pack()
labels=[]
for _ in range(10):
    l=tk.Label(root,bg="#87CEEB",font=("Arial",12))
    l.pack()
    labels.append(l)
(city_label,temp_label,feels_label,maxmin_label,humidity_label,condition_label,
 wind_label,pressure_label,visibility_label,sunrise_label)=labels
sunset_label=tk.Label(root,bg="#87CEEB",font=("Arial",12)); sunset_label.pack()
tk.Label(root,text="5-Day Forecast",font=("Arial",14,"bold"),bg="#87CEEB").pack(pady=5)
forecast_text=tk.Text(root,height=8,width=50)
forecast_text.pack()
root.mainloop()