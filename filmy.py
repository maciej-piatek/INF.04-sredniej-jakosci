import string
import os

class Film():
    def __init__(self, tytul = "", wypo = 0):
        self._tytul = tytul [:20]
        self._wypo = wypo

    def set_tytul(self, temp):

        self._tytul = temp
        while (len(temp) > 20):
            print("tytul przekracza maksymalna ilosc znakow. podaj jeszcze raz")
            if (len(temp) <= 20):
                break



    def get_tytul(self):
        return self._tytul

    def inkrementuj(self):
        pass

    def get_ilosc(self):
        self._wypo += 1
        return self._wypo

film1 = Film()

film1.set_tytul(input("podaj tytul: "))
print(f"Tytul:{film1.get_tytul()}")
print(f"Ilosc wypozyczen:{film1.get_ilosc()}")
print(f"Tytul:{film1.get_tytul()}")
print(f"Ilosc wypozyczen:{film1.get_ilosc()}")

