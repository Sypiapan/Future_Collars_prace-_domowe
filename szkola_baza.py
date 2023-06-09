
class Uczen:
    
    def __init__(self, dane_osoby, klasa, wychowawca, przedmiot):
        self.dane_osoby = dane_osoby
        self.klasa = klasa
        self.wychowawca = wychowawca
        self.przedmiot = przedmiot

    def dane (self):
        print("Podaj imię i nazwisko ucznia  np. Jan Kowalski")
        return input ()
         

    def klasa(self):
        print("Podaj nazwę klasy, do której naleźy uczeń  np. 3C")
        return input()
    

    def opisz(self):
        dane_osoby = input("Podaj imię i nazwisko ucznia  np. Jan Kowalski")
        lista_uczniow = szkola["Uczeń"]
        for uczen in lista_uczniow:
            if uczen["dane_osoby"] == dane_osoby:
                klasa_ucznia = uczen["klasa"]
                
                
        lista_nauczycieli =szkola["Nauczyciel"]
        for nauczyciel in lista_nauczycieli:
            if klasa_ucznia in nauczyciel["klasa"]:

                
                przedmioty_ucznia = nauczyciel["przedmioty"]
                nauczyciel_przedmiotu = nauczyciel["dane_osoby"]
                
                print(f"Przedmiot ucznia {dane_osoby} to: {przedmioty_ucznia}")
                print(f"Nauczyciel przedmiotu to: {nauczyciel_przedmiotu}")

      
class Nauczyciel:
    
    def __init__(self, dane_osoby, klasa, przedmiot):
        self.dane_osoby = dane_osoby
        self.klasa = klasa
        self.przedmiot = przedmiot

    def dane (self):
        print("Podaj imię i nazwisko nauczyciela  np. Jan Kowalski")
        return input()
    
    def przedmiot(self):
        print("Podaj nazwe przedmiot, który prowadzi nauczyciel. ")
        return input()

    def klasa(self):
        print("Podaj nazwę klasy  np. 3C, które uczy nauczyciel. Jesli chcesz zakończyć wpisz pustą linie. ")
        return input()


    def opisz(self):
        dane_osoby = input("Podaj imię i nazwisko nauczyciela  np. Jan Kowalski")
        
        lista = szkola["Nauczyciel"]
        for nauczyciel in lista:
           if nauczyciel["dane_osoby"]== dane_osoby:
               klasy = nauczyciel["klasa"]
               print(f"Nauczyciel: {dane_osoby} uczy klasy: {klasy}")
  

class Wychowawca:
    
    def __init__(self, dane_osoby, klasa ):
        self.dane_osoby = dane_osoby
        self.klasa = klasa

    def dane (self):
        print("Podaj imię i nazwisko wychowawcy  np. Jan Kowalski")
        return input()

    def klasa(self):
        print("Podaj nazwę prowadzonej klasy  np. 3C")
        return input()


    def opisz(self):
        dane_osoby = input("Podaj imię i nazwisko wychowawcy  np. Jan Kowalski")
        klasa = input ("Podaj nazwę prowadzonej klasy  np. 3C")

        uczniowie_klasy =[]
        lista_uczniow = szkola["Uczeń"]
        for uczen in lista-uczniow:
            if uczen["klasa"] == klasa:
                uczen_klasy = uczen["dane_osoby"]
                uczniowie_klasy.append(uczen_klasy)

        print(f"Wychowawca: {dane_osoby} klasy: {klasa} i jego uczniowie: {uczniowie_klasy}")

class Klasa:
    def __init__(self, dane_osoby, klasa, wychowawca ):
        self.imie_nazwisko = imie_nazwisko
        self.klasa = klasa
        self.wychowawca = wychowawca

    def opisz(self):
        
        klasa = input("Podaj nazwę klasy  np. 3C")
        uczniowie_klasy =[]
        lista_wychowawcow =szkola["Wychowawca"]
        lista_uczniow = szkola["Uczeń"]
        for uczen in lista_uczniow:
            if uczen["klasa"] == klasa:
                uczen_klasy = uczen["dane_osoby"]
                uczniowie_klasy.append(uczen_klasy)

        for wychowawca in lista_wychowawcow:
            if wychowawca["klasa"] == klasa:
                wychowawca_klasy = wychowawca["dane_osoby"]
        
        
        print(f" Klasa: {klasa} ma wychowawce: {wychowawca_klasy} i następujacych uczniów: {uczniowie_klasy}")
       
szkola ={

"Uczeń":[],
"Nauczyciel":[],
"Wychowawca":[],
}


while True:
      
    print("""Co chcesz zrobić?:
                1- Utwórz
                2- Zarzadzaj
                0- Koniec""")
    opcja = input()
    
    if opcja == "0":
        print ("Kończę działanie programu")
        break 
    if opcja == "1": 
        while True:
            print("""Co chcesz utworzyć?:
                1- Uczeń
                2- Nauczyciel
                3- Wychowawca
                0- Koniec""")

            opcja = input()
            
            if opcja == "1":
                dane_osoby = Uczen.dane("self")
                klasa = Uczen.klasa("self")
                uczen = {"dane_osoby": dane_osoby, "klasa": klasa}
                szkola["Uczeń"].append(uczen)
                
                print(f"To jest baza...{szkola}")
                
            elif opcja == "2":
                klasy = []
                dane_osoby = Nauczyciel.dane("self")
                
                while True:                 
                 klasa = Nauczyciel.klasa ("self")
                 klasy.append(klasa)
                 if not klasa:
                    break
                przedmiot = Nauczyciel.przedmiot("self")
                nauczyciel = {"dane_osoby": dane_osoby, "klasa": klasy, "przedmioty": przedmiot}
                szkola["Nauczyciel"].append(nauczyciel)
                
                
            elif opcja == "3":
                dane_osoby = Wychowawca.dane("self")
                klasa = Wychowawca.klasa("self")
                wychowawca = {"dane_osoby": dane_osoby, "klasa": klasa}
                szkola["Wychowawca"].append(wychowawca)
                print(f"To jest baza...{szkola}")

                              
            if opcja == "0":
                print ("Przechodzę do głównego Menu")
                break 
    
    if opcja == "2":
        while True:
            print("""Kim chcesz zarzadzać?:
                1- Uczeń
                2- Nauczyciel
                3- Wychowawca
                4- Klasa
                0- Koniec""")
            opcja = input()
            
            if opcja == "0":
                break
            
            if opcja == "1":
                Uczen.opisz("self")

            elif opcja == "2":
                 Nauczyciel.opisz("self")

            elif opcja == "3":
                 Wychowawca.opisz("self")
                

            elif opcja == "4":
                 Klasa.opisz("self")

   
