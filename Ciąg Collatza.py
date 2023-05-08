

liczba = int(input("Podaj liczbe z zakresu 0d 1 do 100..."))



if liczba < 1 or liczba > 100:
    print("podana liczba jest spoza zakresu -zacznij ponownie")
    liczba = int(input("Podaj liczbe z zakresu 0d 1 do 100..."))


while liczba != 1:

    

    if liczba %2 == 0:
        liczba = liczba/2
    
      
    else:
        liczba = (liczba *3) +1

   




    print (f"{liczba}")
   

    
