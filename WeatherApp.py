from tkinter import *
from tkinter import messagebox;
from configparser import ConfigParser
import requests


api_url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}"

API_KEY = "9b34c29fc4e83b4bebc01b005efc59d2"

def getWeather(city):
   result = requests.get(api_url.format(city, API_KEY))
   if result:
      jsonObject = result.json()
      cityName = jsonObject['name']
      cityCountry = jsonObject['sys']['country']
      cityTempK = jsonObject['main']['temp']
      cityTempC = cityTempK - 273.15
      cityTempF = (cityTempK - 273.15)*9/5 + 32
      icon = jsonObject['weather'][0]['icon']
      weather  =jsonObject['weather'][0]['main']
      finalPattern = (cityName, cityCountry, cityTempC, cityTempF, icon, weather)
      return finalPattern
   else:
      return None
      
def searchCity():
   city = search_text.get()
   weatherResults  = getWeather(city)

   if weatherResults:
      location_label['text'] = '{} {}'.format(weatherResults[0], weatherResults[1])
      img["file"] = 'weather_icons/{}@2x.png'.format(weatherResults[4])
      temperature_label['text']  = '{:.2f}°C, {:.2f}°F'.format(weatherResults[2], weatherResults[3])
      weather_label['text'] = weatherResults[-1]
   else:
      messagebox.showerror('Error', 'Cannot find city {}'.format(city))
      



app = Tk()
app.title("Weather Around Me")
app.geometry("700x350")


search_text = StringVar()
search_entry = Entry(app, textvariable=search_text)
search_entry.pack()


search_btn = Button(app, text="Search Weather", width=12, command=searchCity)
search_btn.pack()


location_label = Label(app, text="", font=("bold", 20))
location_label.pack()

img = PhotoImage(file= "")
image = Label(app, image = img)
image.pack()


temperature_label = Label(app, text="")
temperature_label.pack()

weather_label = Label(app, text="")
weather_label.pack()

app.mainloop()