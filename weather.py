import tkinter as tk
from tkinter import messagebox
import requests

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather App")
        
        # Entry field for location
        self.location_entry = tk.Entry(root, width=50, textvariable="Enter Zip Code")
        self.location_entry.pack(pady=10)
        
        # Button to fetch weather
        self.fetch_button = tk.Button(root, text="Fetch Weather", command=self.fetch_weather)
        self.fetch_button.pack()
        
        # Labels to display weather information
        self.weather_info_label = tk.Label(root, text="")
        self.weather_info_label.pack(pady=10)
    
    def fetch_weather(self):
        location = self.location_entry.get()
        if location:
            api_key = ""  
            url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
            
            try:
                response = requests.get(url)
                data = response.json()
                
                if data["cod"] == 200:
                    temperature = data["main"]["temp"]
                    humidity = data["main"]["humidity"]
                    description = data["weather"][0]["description"]
                    
                    weather_info = f"Temperature: {temperature}°C\nHumidity: {humidity}%\nConditions: {description}"
                    self.weather_info_label.config(text=weather_info)
                else:
                    messagebox.showerror("Error", "Unable to fetch weather information. Please check the location.")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")
        else:
            messagebox.showwarning("Location Required", "Please enter a location.")

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()
