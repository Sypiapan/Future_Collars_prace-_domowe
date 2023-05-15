

konto = 0
kwota = 0
magazyn = { "hulajnoga": {"ilość": 10}, "rower": {"ilość": 8},  "piłka": {"ilość": 50}, "skakanka": {"ilość": 20} }
historia = []
produkt = ""
cena = 0
liczba = 0
konto = 0
kwota = 0
index = 0
akcja =""
operacja = {}

import pprint

while True:

    
    opcja = input("WYBIERZ Z MENU: \n Saldo - 1\n Sprzedaż - 2 \n Zakup - 3 \n Konto - 4\n Lista - 5 \n Magazyn - 6 \n Przegląd - 7\n Koniec - q \n")
    
        
    if opcja == "1":

        print("Wybrano opcje - Saldo")
    
        kwota = float(input("Podaj kwotę..."))

        if kwota == 0:
            print("Kwota musi być różna od zera. Spróbuj ponownie")
            kwota = float(input(print("Podaj kwotę...")))
            
            konto +=kwota
            print(f"Zmieniono stan konta o kwote: {kwota}")
            
            continue
        
        if kwota > 0:
            akcja = "wpłata"
        else:
            akcja = "wypłata"

        konto +=kwota
        index+=1
        
        operacja = {"idx": index, "akcja": akcja, "kwota": kwota, "towar": 0, "ilość": 0,  "cena": 0}
        historia.append(operacja)
        
        print(f"Zmieniono stan konta o kwote: {kwota}")
        
        continue      

    elif opcja == "2":

        print("Wybrano opcje - Sprzedaż")
        
        produkt = input("Podaj produkt do sprzedaży...")
        
        if produkt not in magazyn:
            print ("Tego produktu nie ma w magazynie i nie mozna go sprzedać")
            continue
            
        liczba = int(input("Podaj liczbe produktu do sprzedaży..."))
        cena = float(input("Podaj cene produktu do sprzedaży..."))
        if cena < 0:
            print ("Cena nie może byc ujemna. Wracam do głownego Menu")
            continue

        magazyn[produkt]["ilość"]-=liczba
        konto+=liczba*cena
        akcja = "sprzedaż"
        index+=1

        operacja = {"idx": index, "akcja": akcja, "kwota": liczba * cena, "towar": produkt, "ilość": liczba,  "cena": cena} 
        historia.append(operacja)
        
        continue
    
    elif opcja == "3":

        print("Wybrano opcje - Kupno")

        produkt = input("Podaj produkt do kupna...")
        if produkt not in magazyn:
            print ("Tego produktu nie ma w magazynie i dodaje go do magazynu")
            magazyn[produkt]={"ilość": liczba}
            
       
        liczba = int(input("Podaj liczbe produktu do kupna..."))
        cena = float(input("Podaj cene produktu do kupna..."))

        if cena < 0:
            print ("Cena nie może byc ujemna. Wracam do głownego Menu")
            continue

        magazyn[produkt]["ilość"]+=liczba
        
        if konto < liczba * cena:
            print ("Nie ma środków na koncie na ten zakup. Wracam do głownego Menu")
            continue
               
        konto-=liczba*cena
        akcja = "kupno"
        index+=1
        operacja = {"idx": index, "akcja": akcja, "kwota": liczba * cena, "towar": produkt, "ilość": liczba,  "cena": cena} 
        historia.append(operacja)
        continue
    
    elif opcja == "4":
        
        print("Wybrano opcje - Saldo")
        print(f"Stan konta wynosi: {konto}")
        continue
         
    elif opcja == "5":

        print("Wybrano opcje - Lista")
        pprint.pprint(magazyn)
        continue
        
        
    elif opcja == "6":

        print("Wybrano opcje - Magazyn")
        produkt = input(print("Podaj produkt do sprawdzenia..."))

        ilosc_magazyn = magazyn[produkt]["ilość"]

        print(f"Liczba sztuk w magazynie dla {produkt} to: {ilosc_magazyn} sztuk" )
        continue

    elif opcja == "7":

        print("Wybrano opcje - Przegląd")
        okres_od = int(input("Podaj nr id akcji od którego chcesz przejrzec zapisane akcje. Nr id z zakresu od 0 do -2, gdzie pierwszy element ma indeks 0 a przedostatni to -2"))
        okres_do = int(input("Podaj nr id akcji do którego chcesz przejrzec zapisane akcje. Nr id z zakresu od 1 do n,  gdzie ostatni element  ma indeks -2"))

        pprint.pprint(historia[okres_od:okres_do+1])
        continue

    elif opcja == "q" or opcja == "Q":
        print("Wybrano opcje - Koniec. Kończę prace programu.")

    break
