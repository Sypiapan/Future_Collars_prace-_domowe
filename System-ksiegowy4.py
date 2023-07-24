# This Python file uses the following encoding: utf-8
import pprint
import sys

class Manager:

    def __init__(self):
        self.actions = {}
        self.magazyn = {}
        self.historia = []
        self.operacja = {}
        self.produkt = ""
        self.cena = 0
        self.liczba = 0
        self.konto = 0
        self.kwota = 0
        self.index = 0
        self.akcja = ""

    def assign(self, name):
        def decorate(func):
            self.actions[name] = func
        return decorate

    def execute(self, name, *args, **kwargs):
        if name not in self.actions:
            print("Action not defined")
        else:
            self.actions[name](*args, **kwargs)(self)
            # return self.actions[name](*args, **kwargs)

manager = Manager()

@manager.assign("menu")
def menu(manager = manager):


    opcja = input("WYBIERZ Z MENU: \n Saldo - 1\n Sprzedaz - 2 \n Zakup - 3 \n Konto - 4\n Lista - 5 \n Magazyn - 6 \n Przeglad - 7\n Koniec - q \n")

    if opcja == "1":
        manager.execute("saldo")

    elif opcja == "2":
        manager.execute("sale")

    elif opcja == "3":
        manager.execute("buy")

    elif opcja == "4":
        manager.execute("konto")

    elif opcja == "5":
        manager.execute("lista")

    elif opcja == "6":
        manager.execute("magaz")

    elif opcja == "7":
        manager.execute("przeg")

    elif opcja == "q" or opcja == "Q":
        manager.execute("end")




@manager.assign("saldo")
def saldo (manager = manager, konto = manager.konto, kwota = manager.kwota, akcja = manager.akcja, operacja = manager.operacja, historia = manager.historia, index = manager.index):
    print("Wybrano opcje - Saldo")

    kwota = float(input("Podaj kwote..."))

    while konto + kwota < 0:
        print(f"Nie moge wyplacic kwoty wyzzszej ni� stan konta. Stan konta to: {konto}")
        print("Kwota musi byc mniejsza lub rowna stanowi konta. Sprobuj ponownie")
        kwota = float(input("Podaj kwote..."))
    if kwota == 0:
        print("Kwota musi by� r�na od zera. Sprobuj ponownie")
        kwota = float(input("Podaj kwote..."))

        while konto + kwota < 0:
            print(f"Nie moge wyplacic kwoty wyzszej niz stan konta. Stan konta to: {konto}")
            print("Kwota musi byc mniejsza lub rowna stanowi konta. Sprobuj ponownie")
            kwota = float(input("Podaj kwote..."))

        with open('konto.txt') as fd:
            for line in fd:
                konto = float(line)

        konto += kwota
        fd = open('konto.txt', "w")
        fd.write(str(konto))
        fd.close()

        print(f"Zmieniono stan konta o kwote: {kwota}")
        #continue

    if kwota > 0:
        akcja = "wplata"
    else:
        akcja = "wyplata"

    with open('konto.txt') as fd:
        for line in fd:
            konto = float(line)

    konto += kwota
    fd = open('konto.txt', "w")
    fd.write(str(konto))
    fd.close()

    index += 1

    operacja = {"idx": index, "akcja": akcja, "kwota": kwota, "towar": 0, "ilosc": 0, "cena": 0}
    historia.append(operacja)

    fd = open("historia.txt", "a")
    fd.write(f"{operacja} \n")
    fd.close()

    print(f"Zmieniono stan konta o kwote: {kwota}")

    #continue
    manager.execute("menu")

@manager.assign("sale")
def sprzedaz(manager =manager, konto = manager.konto, index = manager.index, historia = manager.historia, magazyn = manager.magazyn):
    print("Wybrano opcje - Sprzedaz")

    with open("magazyn.txt", "r") as plik:
        for linia in plik:
            linia = linia.strip()
            produkt, ilosc = linia.split(";")
            ilosc = int(ilosc)
            magazyn[produkt] = {"ilosc": ilosc}

    produkt = input("Podaj produkt do sprzedazy...")

    if produkt not in magazyn:
        print("Tego produktu nie ma w magazynie i nie mozna go sprzedac")
        #continue
        manager.execute("menu")

    liczba = int(input("Podaj liczbe produktu do sprzedazy..."))
    cena = float(input("Podaj cene produktu do sprzedazy..."))
    if cena < 0:
        print("Cena nie moze byc ujemna. Wracam do goownego Menu")
        #continue
        manager.execute("menu")

    magazyn[produkt]["ilosc"] -= liczba
    konto += liczba * cena

    fd = open('konto.txt', "w")
    fd.write(str(konto))
    fd.close()
    akcja = "sprzedaz"
    index += 1

    operacja = {"idx": index, "akcja": akcja, "kwota": liczba * cena, "towar": produkt, "ilosc": liczba,
                "cena": cena}
    historia.append(operacja)
    fd = open('historia.txt', "a")
    fd.write(f"{operacja} \n")
    fd.close()

    with open("magazyn.txt", "w") as plik:
        for k, v in magazyn.items():
            ilosc = magazyn[k]["ilosc"]
            plik.write(f"{k};{ilosc}\n")

        #continue
    manager.execute("menu")

@manager.assign("buy")
def zakup(manager = manager, magazyn = manager.magazyn, konto = manager.konto, cena = manager.cena, liczba = manager.liczba, index = manager.index, historia = manager.historia):


    print("Wybrano opcje - Kupno")

    with open("magazyn.txt", "r") as plik:
        for linia in plik:
            linia = linia.strip()
            produkt, ilosc = linia.split(";")
            ilosc = int(ilosc)
            magazyn[produkt] = {"ilosc": ilosc}

    produkt = input("Podaj produkt do kupna...")
    if produkt not in magazyn:
        print("Tego produktu nie ma w magazynie i dodaje go do magazynu")
        magazyn[produkt] = {"ilosc": liczba}

    liczba = int(input("Podaj liczbe produktu do kupna..."))
    cena = float(input("Podaj cene produktu do kupna..."))

    if cena < 0:
        print("Cena nie moze byc ujemna. Wracam do glownego Menu")
        #continue
        manager.execute("menu")

    magazyn[produkt]["ilosc"] += liczba

    with open('konto.txt') as fd:
        for line in fd:
            konto = float(line)

    if konto < liczba * cena:
        print(konto)
        print("Nie ma srodkow na koncie na ten zakup. Wracam do glownego Menu")
        #continue
        manager.execute("menu")

    konto -= liczba * cena
    fd = open('konto.txt', "w")
    fd.write(str(konto))
    fd.close()
    akcja = "kupno"
    index += 1
    operacja = {"idx": index, "akcja": akcja, "kwota": liczba * cena, "towar": produkt, "ilosc": liczba,
                    "cena": cena}
    historia.append("operacja\n")
    fd = open('historia.txt', "a")
    fd.write(f"{operacja} \n")
    fd.close()

    with open("magazyn.txt", "w") as plik:
        for k, v in magazyn.items():
            ilosc = magazyn[k]["ilosc"]
            plik.write(f"{k};{ilosc}\n")
    #continue

    manager.execute("menu")

@manager.assign("konto")
def konto(manager = manager):

    print("Wybrano opcje - Konto")
    with open('konto.txt') as fd:
        for line in fd:
            konto = float(line)

    print(f"Stan konta wynosi: {konto}")
    #continue
    manager.execute("menu")

@manager.assign("lista")
def lista(manager = manager, magazyn = manager.magazyn):
    print("Wybrano opcje - Lista")
    with open("magazyn.txt", "r") as plik:
        for linia in plik:
            linia = linia.strip()
            produkt, ilosc = linia.split(";")
            ilosc = int(ilosc)
            magazyn[produkt] = {"ilość": ilosc}
    print("Stan magazynu:")
    pprint.pprint(magazyn)
    #continue
    manager.execute("menu")

@manager.assign("magaz")
def magazyn(manager = manager, magazyn = manager.magazyn, ):
    print("Wybrano opcje - Magazyn")
    print("Wczytuje magazyn...")
    with open("magazyn.txt", "r") as plik:
        for linia in plik:
            linia = linia.strip()
            produkt, ilosc = linia.split(";")
            ilosc = int(ilosc)
            magazyn[produkt] = {"ilosc": ilosc}

    produkt = input("Podaj produkt do sprawdzenia...")
    if produkt not in magazyn:
        print("Tego produktu nie ma w magazynie i nie mozna go sprawdzic. Przechodze do glownego menu.")
        #continue
        manager.execute("menu")
    ilosc_magazyn = magazyn[produkt]["ilosc"]

    with open("magazyn.txt", "w") as plik:
        for k, v in magazyn.items():
            ilosc = magazyn[k]["ilosc"]
            plik.write(f"{k};{ilosc}\n")

    print(f"Liczba sztuk w magazynie dla {produkt} to: {ilosc_magazyn} sztuk")
    #continue
    manager.execute("menu")

@manager.assign("przeg")
def przeglad(manager = manager, historia = manager.historia):
    print("Wybrano opcje - Przeglad")
    okres_od = int(input("Podaj nr id akcji od ktorego chcesz przejrzec zapisane akcje. Nr id z zakresu od 0 do -2, gdzie pierwszy element ma indeks 0 a przedostatni to -2"))
    okres_do = int(input("Podaj nr id akcji do ktorego chcesz przejrzec zapisane akcje. Nr id z zakresu od 1 do n,  gdzie ostatni element  ma indeks -1"))

    with open("historia.txt", "r") as plik:
        for linia in plik:
            linia = linia.strip()
            historia.append(linia)

    pprint.pprint(historia[okres_od:okres_do ])
    # continue
    manager.execute("menu")

@manager.assign("end")
def koniec(manager=manager, magazyn = manager.magazyn):
    print("Wybrano opcje - Koniec.")
    print("Kończę prace programu.")

    sys.exit()



while True:
    opcja = input("WYBIERZ Z MENU: \n Saldo - 1\n Sprzedaz - 2 \n Zakup - 3 \n Konto - 4\n Lista - 5 \n Magazyn - 6 \n Przeglad - 7\n Koniec - q \n")

    if opcja == "1":
        manager.execute("saldo")

    elif opcja == "2":
        manager.execute("sale")

    elif opcja == "3":
        manager.execute("buy")

    elif opcja == "4":
        manager.execute("konto")

    elif opcja == "5":
        manager.execute("lista")

    elif opcja == "6":
        manager.execute("magaz")

    elif opcja == "7":
        manager.execute("przeg")

    elif opcja == "q" or opcja == "Q":
        manager.execute("end")


