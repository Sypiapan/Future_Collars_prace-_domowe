
import csv
import sys

#python reader.py in.csv out.csv 0,0,gitara 3,1,kubek 1,2,17 3,3,0
# ['C:\\Users\\ThinkPad T420\\Desktop\\Future Collars\\Furure Collars_Paczkomat\\reader.py', 'python', 'reader.py', 'in.csv', 'out.csv', '0,0,gitara', '3,1,kubek', '1,2,17', '3,3,0']

in_file = sys.argv[3]
out_file = sys.argv[4]
wartosci_do_zmiany =sys.argv[5:]


# otwieram plik z wartosciami wejsciowymi,
# które podlegaja zmianie i zapisuje je do listy.
content=[]

with open (in_file, "r") as f:
    reader =csv.reader(f)
    for line in reader:
       content.append(line)
     
    
# zamieniam wartosci_do_zmiany ze str na liste

lista_wartosci_do_zmiany  = []

for zmiana in wartosci_do_zmiany:
    zmiana_lista = zmiana.split(",")
    lista_wartosci_do_zmiany.append(zmiana_lista)

    
# zmiana wartosci w in-file

nr_kolumny = ""
nr_wiersza = ""
wartosc = " "

for zmiana in lista_wartosci_do_zmiany:
    nr_kolumny = int(zmiana[0])
    nr_wiersza = int(zmiana[1])
    wartosc = zmiana[2]
    content[nr_wiersza][nr_kolumny] = wartosc


# zapisuje plik wyjsciowy ze zmienionymi wartosciami
    
with open (out_file, "w") as f:
    writer =csv.writer(f)
    for row in content:
        writer.writerow(row)
        
  
