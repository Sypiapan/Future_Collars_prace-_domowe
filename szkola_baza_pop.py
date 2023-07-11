
class Uczen:
    
    def __init__(self, dane_osoby=None, klasa=None):
        self.dane_osoby = dane_osoby
        self.klasa = klasa
        
    def wczytaj_ucznia(self ):
        dane_osoby = input("Podaj imię i nazwisko ucznia  np. Jan Kowalski")
        klasa = input("Podaj nazwę klasy, do której naleźy uczeń  np. 3C")
        uczen = {"dane_osoby": dane_osoby, "klasa": klasa}
        szkola["Uczeń"].append(uczen)

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
    
    def __init__(self, dane_osoby=None, klasa=None, przedmiot=None):
        self.dane_osoby = dane_osoby
        self.klasa = klasa
        self.przedmiot = przedmiot

    def wczytaj_nauczyciela(self):
        dane_osoby = input("Podaj imię i nazwisko nauczyciela  np. Jan Kowalski")
        klasy = []
        while True:
         klasa = input("Podaj nazwę klasy  np. 3C, które uczy nauczyciel. Jesli chcesz zakończyć wpisz pustą linie.")
         klasy.append(klasa)
         if not klasa:
            break
        przedmiot = input("Podaj nazwe przedmiot, który prowadzi nauczyciel.")
        nauczyciel = {"dane_osoby": dane_osoby, "klasa": klasy, "przedmioty": przedmiot}
        szkola["Nauczyciel"].append(nauczyciel)

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
    
    def __init__(self, dane_osoby=None, klasa=None ):
        self.dane_osoby = dane_osoby
        self.klasa = klasa

    def wczytaj_wychowawce(self):
        dane_osoby = input("Podaj imię i nazwisko wychowawcy  np. Jan Kowalski")
        klasa = input("Podaj nazwę prowadzonej klasy  np. 3C")
        wychowawca = {"dane_osoby": dane_osoby, "klasa": klasa}
        szkola["Wychowawca"].append(wychowawca)
     

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
    def __init__(self, klasa=None, wychowawca=None ):
        
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
                nowy_uczen = Uczen()
                nowy_uczen.wczytaj_ucznia()
                            
            elif opcja == "2":
                klasy = []
                nowy_nauczyciel = Nauczyciel()
                nowy_nauczyciel.wczytaj_nauczyciela()
                                
            elif opcja == "3":
                nowy_wychowawca = Wychowawca()
                nowy_wychowawca.wczytaj_wychowawce()
                              
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
                nowy_uczen.opisz()

            elif opcja == "2":
                 nowy_nauczyciel.opisz()

            elif opcja == "3":
                 nowy_wychowawca.opisz()
                

            elif opcja == "4":
                 nowa_klasa = Klasa()
                 nowa_klasa.opisz()
                
    

   
