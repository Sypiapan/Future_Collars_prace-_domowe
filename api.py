

import requests
from datetime import datetime, timedelta

# Z uwagi ,że aplikacja ma tylko sprawdzać datę zapytania a nie sprawdzać współrzędnych założyłem,że współrzędne są stałe.
# Aplikacja sprawdza pogodę dla Warszawy i wpisałem współrzędne Warszawy.

latitude = 52.23
longitude = 21.01

weather_history ={}

print ("Sprawdzam czy będzie padał deszcz w Warszawie.")
searched_date = input("Podaj datę w formacie (YYYY-MM-DD), kiedy chcesz sprawdzić czy będzie padał deszcz...\nJeśli nie podasz daty. Sprawdzę czy deszcz będzie padał jutro.")


presentday = datetime.now()
tomorrow = presentday + timedelta(1)
date_tomorrow_str = tomorrow.strftime('%Y-%m-%d')

if not searched_date :
    searched_date = date_tomorrow_str

with open("weather.txt", "r") as plik:
    for linia in plik:
        linia = linia.strip()
        date, weather = linia.split(",")
        weather_history[date] = {"pogoda": weather}

if searched_date in weather_history:

    print(f"Pogoda dla {searched_date} już była sprawdzana i w Warszawie {weather.lower()}.")


else:

    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=rain&daily=rain_sum&timezone=Europe%2FLondon&start_date={searched_date}&end_date={searched_date}"

    resp = requests.get(url)

    if resp.ok:
        rain = (resp.json()["daily"]["rain_sum"][0])
        if rain > 0:
            message = "Będzie padać"
            print(message)
        elif rain == 0:
            message = "Nie będzie padać"
            print(message)
        elif rain == None or rain < 0:
            message = "Nie wiem"
            print(message)


        with open ("weather.txt", "a") as file:
            file.write (f"{searched_date},{message}\n")
            file.close()


    else:
        print("Błąd w zapytaniu")
        print(f"Kod błędu - {resp.status_code} Treść błedu - {resp.text}")





