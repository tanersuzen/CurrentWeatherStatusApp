import requests
from tkinter import *
import tkinter.messagebox

window = Tk()
window.title("Current Weather Status")
window.minsize(width=300,height=300)
window.config(padx=30,pady=30)

def buttonFunc():
    city1 = my_city.get()
    api_key1 = my_api_key.get()
    weather_status(api_key1,city1)

def weather_status(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(base_url, params=params)
    city_name.config(text="")
    city_temp.config(text="")
    city_humd.config(text="")
    city_desc.config(text="")
    city_error.config(text="")

    if response.status_code == 200:
        current_weather_status = response.json()
        city_name.config(text=f"{city} current weather status:")
        city_temp.config(text=f"Temperature: {current_weather_status['main']['temp']}°C")
        city_humd.config(text=f"Humidity: {current_weather_status['main']['humidity']}%")
        city_desc.config(text=f"Description: {current_weather_status['weather'][0]['description']}")
    else:
        tkinter.messagebox.showwarning("Error!","Weather status could not get")
        city_error.config(text="Weather status could not get!",font=("Times New Roman",20,"italic"),fg="red")


my_label = Label(text="Enter your city")
my_label.config(fg="white")
my_label.pack()

my_city = Entry(width=10)
my_city.pack()

my_api = Label(text="Enter your Api Key")
my_api.config(fg="white")
my_api.pack()

my_api_key = Entry(width=25)
my_api_key.pack()



my_button = Button(text="Submit", command=buttonFunc)
my_button.config(padx=10, pady=5)
my_button.pack()

city_name = Label()
city_name.pack()

city_temp = Label()
city_temp.pack()

city_humd = Label()
city_humd.pack()

city_desc = Label()
city_desc.pack()

city_error = Label()
city_error.pack()

window.mainloop()
