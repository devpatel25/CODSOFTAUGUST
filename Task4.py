# Task 4 - Weather Forecast
import requests
import tkinter as tk

key="b6314e2beb0e54f6b4ded0744257d64e"

# get weather data from API
def get_weather_data(location):
    try:
        if location.isdigit():
            url = f"http://api.openweathermap.org/data/2.5/weather?zip={location}&appid={key}"
        else:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={key}"

        response= requests.get(url)
        weather_data=response.json()

        if response.status_code == 200:
            return weather_data
        else:
            return None
    except requests.exceptions.RequestException as e:
        print("Error: ", e)
        return None


# display weather data
def display_weather_data():
    location=input_entry.get()
    weather_data=get_weather_data(location)
    temperature=weather_data["main"]["temp"]
    humidity=weather_data["main"]["humidity"]
    wind_speed=weather_data["wind"]["speed"]
    weather_description=weather_data["weather"][0]["description"]
    result_label.config(text=f"Temperature: {temperature}°F\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s\nDescription: {weather_description}")




# Main
window=tk.Tk()
window.title("Weather Forecast Application")
window.geometry("400x300")
lbl_input=tk.Label(window,text="Enter the name or Zipcode of the city: ",font=("arial",15)).pack()
input_entry=tk.Entry(window)
input_entry.pack()
btn=tk.Button(window,text="Go",font=("arial",15,"bold"),command=display_weather_data).pack()
result_label = tk.Label(window, text="",font=("arial",15,"bold"))
result_label.pack()
result_label.place(x=100,y=100)
window.mainloop()