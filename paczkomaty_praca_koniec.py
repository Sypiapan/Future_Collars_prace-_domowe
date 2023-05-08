MAX_PACZKI = 20
liczba_elementow = 0
waga_elementu = 0
waga_paczki = 0
waga_wyslana = 0
liczba_paczek = 0
kolejna_paczka = 0
sklad_paczki = ""

max_waga_paczki = 19
paczka_z_min_waga = 0
numer_paczki = 0


liczba_elementow = int(input("Podaj liczbe elementów do wysłania"))

for element in range(1, liczba_elementow+1):
    
    waga_elementu = int(input("Podaj wagę elementu z  zakresu od 1 do 10 kg..."))
    if (waga_elementu < 1 or waga_elementu > 10):
        print("Waga podanego elementu jest poza zakresem")

        
        break

    waga_paczki += waga_elementu
    

    waga_wyslana += waga_elementu
    sklad_paczki += "+" + str(waga_elementu)
    liczba_paczek = kolejna_paczka + 1
    
    while waga_paczki < max_waga_paczki:
        max_waga_paczki=waga_paczki
        paczka_z_min_waga=liczba_paczek

              

    if (waga_elementu > (MAX_PACZKI-waga_paczki)):
        waga_paczki = 0
        kolejna_paczka += 1


        continue
    
  


print(f"Wysłana liczba paczek to {liczba_paczek} ze składem {sklad_paczki}")
print(f"Wysłano {waga_wyslana} kg")
print(f"Suma pustych kilogramów: {(liczba_paczek * MAX_PACZKI) - waga_wyslana}")
print(f"Najwięcej pustych kilogramów ma paczka {paczka_z_min_waga} ze składem {waga_paczki}kg")


