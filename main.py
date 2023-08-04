from flask import Flask,render_template, request
import pprint
app = Flask(__name__)



def saldo (kwota):
    with open('konto.txt') as fd:
        for line in fd:
            konto = float(line)

    # konto = 0
    konto+=kwota

    if kwota > 0:
        akcja = "wplata"
    else:
        akcja = "wyplata"


    if kwota != 0:
        with open('index.txt') as fd:
            for line in fd:
                index = int(line)
            index += 1

        fd = open('index.txt', "w")
        fd.write(str(index))
        fd.close()

        operacja = { "idx": index,"akcja": akcja, "kwota": kwota, "towar": 0, "ilosc": 0, "cena": 0}

        fd = open("historia.txt", "a")
        fd.write(f"{operacja} \n")
        fd.close()

        fd = open('konto.txt', "w")
        fd.write(str(konto))
        fd.close()

    return konto
def zakup(zakup_produkt, zakup_ilosc,zakup_cena):
    magazyn = {}
    with open("magazyn.txt", "r") as plik:
        for linia in plik:
            linia = linia.strip()
            produkt, ilosc = linia.split(";")
            ilosc = int(ilosc)
            magazyn[produkt] = {"ilosc": ilosc}


    if zakup_produkt not in magazyn:

        magazyn[zakup_produkt] = {"ilosc": 0}

    if zakup_cena < 0:
        pass
        # print("Cena nie moze byc ujemna. Wracam do glownego Menu")

        # manager.execute("menu")

    magazyn[zakup_produkt]["ilosc"] += zakup_ilosc

    with open('konto.txt') as fd:
        for line in fd:
            konto = float(line)

    if konto < zakup_ilosc * zakup_cena:
        pass
        # print(konto)
        # print("Nie ma srodkow na koncie na ten zakup. Wracam do glownego Menu")
        # #continue
        # manager.execute("menu")

    konto -= zakup_ilosc * zakup_cena
    fd = open('konto.txt', "w")
    fd.write(str(konto))
    fd.close()
    akcja = "kupno"

    if zakup_cena > 0:

        with open('index.txt') as fd:
            for line in fd:
                index = int(line)

            index += 1

        fd = open('index.txt', "w")
        fd.write(str(index))
        fd.close()

        operacja = {"idx": index, "akcja": akcja, "kwota": zakup_ilosc * zakup_cena, "towar": zakup_produkt, "ilosc": zakup_ilosc,
                    "cena": zakup_cena}

        fd = open("historia.txt", "a")
        fd.write(f"{operacja} \n")
        fd.close()

    with open("magazyn.txt", "w") as plik:
        for k, v in magazyn.items():
            ilosc = magazyn[k]["ilosc"]
            plik.write(f"{k};{ilosc}\n")

def sprzedaz(sprzedaz_produkt, sprzedaz_ilosc,sprzedaz_cena):
    magazyn = {}
    with open("magazyn.txt", "r") as plik:
        for linia in plik:
            linia = linia.strip()
            produkt, ilosc = linia.split(";")
            ilosc = int(ilosc)
            magazyn[produkt] = {"ilosc": ilosc}
    produkt = sprzedaz_produkt
    print("Magazyn", magazyn)
    print("Sprzedaż_produkt", sprzedaz_produkt)
    print("Sprzedaż_ilosc", sprzedaz_ilosc)


    if sprzedaz_produkt not in magazyn:
        return None

    if sprzedaz_cena < 0:
        return None

    magazyn[sprzedaz_produkt]["ilosc"] -= sprzedaz_ilosc

    with open('konto.txt') as fd:
        for line in fd:
            konto = float(line)
    konto -= sprzedaz_ilosc * sprzedaz_cena

    fd = open('konto.txt', "w")
    fd.write(str(konto))
    fd.close()
    akcja = "sprzedaz"

    if sprzedaz_cena!=0:

        with open('index.txt') as fd:
            for line in fd:
                index = int(line)

            index += 1

        fd = open('index.txt', "w")
        fd.write(str(index))
        fd.close()

        operacja = {"idx": index, "akcja": akcja, "kwota": sprzedaz_ilosc * sprzedaz_cena, "towar": sprzedaz_produkt, "ilosc": sprzedaz_ilosc,
                    "cena": sprzedaz_cena}

        fd = open("historia.txt", "a")
        fd.write(f"{operacja} \n")
        fd.close()

    with open("magazyn.txt", "w") as plik:
        for k, v in magazyn.items():
            ilosc = magazyn[k]["ilosc"]
            plik.write(f"{k};{ilosc}\n")


def magazyn():
    magazyn={}

    with open("magazyn.txt", "r") as plik:
        for linia in plik:
            linia = linia.strip()
            produkt, ilosc = linia.split(";")
            ilosc = int(ilosc)
            magazyn[produkt] = {"ilość": ilosc}

    return (magazyn)

def historia():
    historia=[]

    with open("historia.txt", "r") as plik:
        for linia in plik:
            linia = linia.strip()
            historia.append(linia )

    return (historia)

def przeglad(okres_od,okres_do):
    historia = []

    with open("historia.txt", "r") as plik:
        for linia in plik:
            linia = linia.strip()
            historia.append(linia)

    przeglad = historia[okres_od:okres_do]

    return (przeglad)




@app.route("/", methods=['POST', 'GET'])
def main_page():
    print("#################")
    print(request.form)
    print("#################")
    title = "System accountant - strona główna"
    context = {"title": title,
           "saldo": saldo(0),
           "magazyn": magazyn()}

    if  request.method == "POST":
        kwota = float(request.form.get("kwota",0))

        k_produkt = request.form.get("zakup_produkt")
        k_ilosc = int(request.form.get("zakup_ilosc", 0))
        k_cena = float(request.form.get("zakup_cena", 0))

        s_produkt = request.form.get("sprzedaz_produkt")
        s_ilosc = int(request.form.get("sprzedaz_ilosc", 0))
        s_cena = float(request.form.get("sprzedaz_cena", 0))





        context = {
           "title": title,
           "saldo": saldo(kwota),
           "sprzedaz": sprzedaz(s_produkt, s_ilosc,s_cena),
           "zakup": zakup(k_produkt, k_ilosc,k_cena),
           "magazyn": magazyn(),


        }
    return render_template("index.html", context = context)

@app.route("/historia", methods=['POST', 'GET'])
def history():


    title = "System accountant - historia"
    okres_od = int(request.form.get("okres_od",0))
    okres_do = int(request.form.get("okres_do",0))
    context = {
        "title": title,
        "historia": historia(),
        "przeglad": przeglad(okres_od, okres_do)

    }
    return render_template("history.html", context = context)

