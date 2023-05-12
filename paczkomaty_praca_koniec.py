max_waga_paczki = 20
waga_paczki = 0
waga_wyslana = 0
numer_elementu = 0
liczba_paczek = 0
numer_paczki = 0
sklad_paczki = ""
najlzejsza_paczka = 20
numer_najlzejszej_paczki =0



liczba_elementow = int(input("Podaj liczbe elementów do wysłania.."))

for element in range(1, liczba_elementow+1):
    
    waga_elementu = int(input("Podaj wagę elementu z  zakresu od 1 do 10 kg..."))
    if (waga_elementu < 1 or waga_elementu > 10):
        print("Waga podanego elementu jest poza zakresem. Dodawanie paczek zostaje zakończone i wszystkie paczki są wysłane")

               
        # Wysłanie paczek i wczesniejszych elementów przy podaniu kolejnego elementu spoza zakresu 1-10 kg
        numer_paczki+=1
        liczba_paczek+=1

        # test najlzejszej paczki
        if waga_paczki < najlzejsza_paczka:
            najlzejsza_paczka = waga_paczki
            numer_najlzejszej_paczki = numer_paczki
        
        # Sprawdzenie czy kolejny  element jest spoza zakresu i zabezpieczenie przed wyslaniem paczki
        if waga_paczki == 0 :
            numer_paczki = numer_paczki-1
            liczba_paczek = liczba_paczek-1

        # Sprawdzenie czy pierwszy element jest spoza zakresu i zabezpieczenie przed wyslaniem paczki
        if numer_elementu == 0 :
            numer_paczki = 0
            liczba_paczek = 0      
        
        break

    waga_paczki += waga_elementu
    waga_wyslana += waga_elementu
    sklad_paczki += "+" + str(waga_elementu)
    numer_elementu += 1
     
     # wysyłanie ostatniej paczki
    if numer_elementu == liczba_elementow and waga_elementu <= max_waga_paczki-waga_paczki:
        numer_paczki+=1
        liczba_paczek+=1
        
        if waga_paczki < najlzejsza_paczka:
            najlzejsza_paczka = waga_paczki
            numer_najlzejszej_paczki = numer_paczki
            
        waga_paczki = 0
        
    elif waga_elementu > max_waga_paczki-waga_paczki:
        liczba_paczek +=1
        numer_paczki+=1
        
        if waga_paczki < najlzejsza_paczka:
            najlzejsza_paczka = waga_paczki
            numer_najlzejszej_paczki = numer_paczki
            
        waga_paczki = 0
        continue

print(f"Wysłana liczba paczek to {liczba_paczek} ze składem {sklad_paczki}")
print(f"Wysłano {waga_wyslana} kg")
print(f"Suma pustych kilogramów: {(liczba_paczek * max_waga_paczki) - waga_wyslana}")
print(f"Najwięcej pustych kilogramów ma paczka {numer_najlzejszej_paczki} ze składem {najlzejsza_paczka}kg")

