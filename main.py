
from flask import Flask,render_template, request
import requests

app = Flask(__name__)


def load_parking_places ():
    lista=[]
    ApiKey = "7909a2f5-dd04-4c9b-b0c4-07e7a3bbe7a1"

    url = f"https://api.um.warszawa.pl/api/action/disabled_parking_spaces/?apikey={ApiKey}"
    resp = requests.get(url)
    print(resp.ok)
    print(resp.status_code)
    if resp.ok:

        places = (resp.json()["result"])

        for p in places:

            miejsca = {"ulica": p["street"],"numer_ulicy": p["street_number"], "liczba_miejsc": p["number_of_places"]}
            lista.append(miejsca)

    else:
        print("błąd zapytania)")

    return lista

def verified_street(veryfied_street, lista):
    print("szukana ulica",veryfied_street)
    print("fragment listy", lista[1:3])

    for miejsce in lista:

        ulica = miejsce["ulica"]
        numer_ulicy = miejsce["numer_ulicy"]
        liczba_miejsc = miejsce["liczba_miejsc"]
        if ulica  == veryfied_street:
            print(ulica, numer_ulicy, liczba_miejsc)
            return (ulica,numer_ulicy,liczba_miejsc)
        else:
            print("Na sprawdzanej ulicy nie ma miejsc parkingowych dla niepełnosprawnych")
            return ("Na sprawdzanej ulicy nie ma miejsc parkingowych dla niepełnosprawnych")






@app.route("/", methods=['POST', 'GET'])
def main_page():
    print("#################")
    print(request.form)
    print("#################")

    title = "Miejsca parkingowe dla niepełnosprawnych w Warszawie - strona główna"
    veryfied_street = request.form.get("veryfied_street")
    lista = load_parking_places ()


    context = {
        "szukana_ulica": verified_street(veryfied_street, lista),





    }
    return render_template("index.html", context = context)



@app.route("/wszystkie miejsca", methods=['POST', 'GET'])
def all_places():


    title = "Wszystkie miejsca pargingowe dla niepełnosprawnych w Warszawie"

    context = {


    }
    return render_template("places.html", context = context)
