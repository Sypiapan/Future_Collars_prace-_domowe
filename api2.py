# This Python file uses the following encoding: utf-8

import requests
from datetime import datetime, timedelta

latitude = 52.23
longitude = 21.01

class WeatherForecast:

    def __init__(self, ):
        self.weather_history ={}

    def __getitem__(self, date):
        return self.weather_history[date]

    def __setitem__(self, searched_date, weather):
        self.weather_history[searched_date] = weather

    def read_data(self, file):
        with open(file) as fp:
            for line in fp:
                yield line.strip()

    def __iter__(self):
        return iter(self.weather_history)

    def searched_date_for_forecast(self):
        print("Sprawdzam czy będzie padał deszcz w Warszawie.")
        searched_date = input(
            "Podaj datę w formacie (YYYY-MM-DD), kiedy chcesz sprawdzić czy będzie padał deszcz...\nJeśli nie podasz daty. Sprawdzę czy deszcz będzie padał jutro.")

        presentday = datetime.now()
        tomorrow = presentday + timedelta(1)
        date_tomorrow_str = tomorrow.strftime('%Y-%m-%d')

        if not searched_date:
            searched_date = date_tomorrow_str

        with open("weather2.txt", "r") as plik:
            for linia in plik:
                linia = linia.strip()
                date, weather = linia.split(",")
                self.weather_history[date] = weather

        if searched_date in self.weather_history:
            print("x" * 30)
            print(f"Pogoda dla {searched_date} już była sprawdzana i w Warszawie {weather.lower()}.")
            print("x" * 30)

        else:
            url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=rain&daily=rain_sum&timezone=Europe%2FLondon&start_date={searched_date}&end_date={searched_date}"

            resp = requests.get(url)

            if resp.ok:
                rain = (resp.json()["daily"]["rain_sum"][0])

            if rain > 0:
                weather = "Będzie padać"
                weather_forecast.__setitem__(searched_date=searched_date, weather=weather)
            elif rain == 0:
                weather = "Nie będzie padać"
                weather_forecast. __setitem__(searched_date=searched_date, weather=weather)
            elif rain == None or rain < 0:
                weather = "Nie wiem"
                weather_forecast.__setitem__(searched_date=searched_date, weather=weather)

            with open("weather2.txt", "a") as file:
                file.write(f"{searched_date},{weather}\n")
                file.close()

            print("x" * 30)
            print(f"Pogoda w Warszawie w dniu {searched_date} -", weather_forecast.__getitem__(searched_date))
            print("x" * 30)


weather_forecast = WeatherForecast()
weather_forecast.searched_date_for_forecast()

print(f"Pogoda była już sprawdzana dla nastepujących dni:")
for weather_history in weather_forecast:
     print( weather_history)

print("x"*30)
print("Wcześniej zapisane rezultaty zapytań:")

for k,  v in enumerate(weather_forecast.read_data("weather2.txt")):
    print("{} {}".format(k, v))









