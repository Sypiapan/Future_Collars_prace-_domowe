# This Python file uses the following encoding: utf-8

import txt
import csv
import sys
import json
import pickle



in_file = sys.argv[1]
out_file = sys.argv[2]
wartosci_do_zmiany = sys.argv[3:]

def in_handler(nazwa_pliku):
    if in_file.endswith(".json"):
        handler = JsonHandler()
    elif in_file.endswith(".pickle"):
        handler = PickleHandler()
    elif in_file.endswith(".csv"):
        handler = CSVHandler()
    else:
        handler = TxtHandler()
    return handler

def out_handler(nazwa_pliku):
    if out_file.endswith(".json"):
        handler = JsonHandler()
    elif out_file.endswith(".pickle"):
        handler = PickleHandler()
    elif out_file.endswith(".csv"):
        handler = CSVHandler()
    else:
        handler = TxtHandler()
    return handler

class FileHandler:
    handler = None
    file_type = None

    def load(self, file_name):
        with open(in_file, "r" + self.file_type) as f:
            return self.handler.load(f)


    def dump(self, obj, file_name):
        with open(out_file, "w" + self.file_type) as f:
            self.handler.dump(obj, f)

class JsonHandler(FileHandler):

    handler = json
    file_type = ""

class PickleHandler(FileHandler):
    handler = pickle
    file_type = "b"


class CSVHandler(FileHandler):
    def load(self, file_name):
        _content = []
        with open(in_file, "r") as f:
            reader = csv.reader(f)
            for line in reader:
                _content.append(line)
        return _content



    def dump(self,obj,file_name):
        with open(out_file, "w") as f:
            writer = csv.writer(f)
            for row in content:
                writer.writerow(row)


class TxtHandler(FileHandler):
    def load(self, file_name):
        _content = []
        with open(in_file, "r") as f:
            reader = txt.reader(f)
            for line in reader:
                _content.append(line)
        return _content

    def dump(self, obj, file_name):
        with open(out_file, "w") as f:
            writer = txt.writer(f)
            for row in content:
                writer.writerow(row)


class ChangeHandler:
    nr_kolumny = ""
    nr_wiersza = ""
    wartosc = " "


    def change_file(self, content):

        lista_wartosci_do_zmiany = []
        for zmiana in wartosci_do_zmiany:
            zmiana_lista = zmiana.split(",")
            lista_wartosci_do_zmiany.append(zmiana_lista)

        
        for zmiana in lista_wartosci_do_zmiany:
            nr_kolumny = int(zmiana[0])
            nr_wiersza = int(zmiana[1])
            wartosc = zmiana[2]
            content[nr_wiersza][nr_kolumny] = wartosc

        return content

load_handler = in_handler(in_file)
content = load_handler.load(in_file)
print(content)
change_handler = ChangeHandler()
change_handler.change_file(content)
print(content)
dump_handler = out_handler(in_file)
dump_handler.dump(content, in_file)





#python reader2.py in.csv out.csv 0,0,gitara 3,1,kubek 1,2,17 3,3,0
#python reader2.py in.csv out.json 0,0,gitara 3,1,kubek 1,2,17 3,3,0
#python reader2.py in.json out.txt 0,0,gitara 3,1,kubek 1,2,17 3,3,0
#python reader2.py in.json out.csv 0,0,gitara 3,1,kubek 1,2,17 3,3,0






