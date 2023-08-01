import requests
import pprint
ApiKey = "7909a2f5-dd04-4c9b-b0c4-07e7a3bbe7a1"
lista=[]




url = f"https://api.um.warszawa.pl/api/action/disabled_parking_spaces/?apikey={ApiKey}"

resp = requests.get(url)
print(resp.ok)
print(resp.status_code)
if resp.ok:

    places = (resp.json()["result"])

    for  p in places:

        miejsca = {"ulica": p["street"],"numer_ulicy": p["street_number"], "liczba_miejsc": p["number_of_places"]}

        lista.append(miejsca)

pprint.pprint(lista)

for miejsce in lista:
    ulica = miejsce["ulica"]
    numer_ulicy = miejsce["numer_ulicy"]
    liczba_miejsc = miejsce["liczba_miejsc"]
    if ulica == "Hoża":
        print(ulica,numer_ulicy,liczba_miejsc)














