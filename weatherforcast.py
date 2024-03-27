import tkinter as tk
import requests
import time
from PIL import Image, ImageTk


def getWeather():
    city = textField.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=06c921750b9a82d8f5d1294e1586276f"

    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))

    final_info = condition + "\n" + str(temp) + "°C"
    final_data = "\n" + "Min Temp: " + str(min_temp) + "°C" + "\n" + "Max Temp: " + str(
        max_temp) + "°C" + "\n" + "Pressure: " + str(pressure) + "\n" + "Humidity: " + str(
        humidity) + "\n" + "Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
    label1.config(text=final_info)
    label2.config(text=final_data)

    # Displaying weather icon
    icon_name = json_data['weather'][0]['icon']
    icon_url = f"http://openweathermap.org/img/wn/{icon_name}.png"
    icon_response = requests.get(icon_url, stream=True)
    if icon_response.status_code == 200:
        icon_data = icon_response.raw
        icon = Image.open(icon_data).resize((100, 100))  # Adjust size as needed
        weather_icon = ImageTk.PhotoImage(icon)
        icon_label.config(image=weather_icon)
        icon_label.image = weather_icon  # Keep a reference to prevent garbage collection


canvas = tk.Tk()
canvas.geometry("600x600")
canvas.title("Weather App")
f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textField = tk.Entry(canvas, justify='center', width=20, font=t)
textField.pack(pady=20)
textField.focus()

search_button = tk.Button(canvas, text="Search", command=getWeather)
search_button.pack()

label1 = tk.Label(canvas, font=t)
label1.pack()

icon_label = tk.Label(canvas)
icon_label.pack()

label2 = tk.Label(canvas, font=f)
label2.pack()

canvas.mainloop()
