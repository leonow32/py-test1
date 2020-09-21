
# Wersja 1
#from obiect_4module_slave import Prostokat
#from obiect_4module_slave import Kolo

# Wersja 2
from object_4module_slave import *

# Wersja 3 - tu trzeba sie odnosić poprzez Figury.Prostokat lub Figury.Kolo
#import obiect_4module_slave as Figury               

def main():

    print(f"Liczba prostokatow: {Prostokat.Count}")
    Prostokat.Count
    Prostokat1 = Prostokat("P", 1, 2)
    Prostokat1.Info()
    print("Pole\t= {}".format(Prostokat1.Area()))
    print("Obwod\t= {}".format(Prostokat1.Circuit()))

    print(f"Liczba prostokatow: {Prostokat.Count}")
    Prostokat2 = Prostokat("P", 10, 20)
    Prostokat2.Info()
    print("Pole\t= {}".format(Prostokat2.Area()))
    print("Obwod\t= {}".format(Prostokat2.Circuit()))

    print(f"Liczba prostokatow: {Prostokat.Count}")
    Prostokat3 = Prostokat("P", 100, 200)
    Prostokat3.Info()
    print("Pole\t= {}".format(Prostokat2.Area()))
    print("Obwod\t= {}".format(Prostokat2.Circuit()))

    print(f"Liczba kół: {Kolo.Count}")
    Kolo1 = Kolo("K", 1)
    Kolo1.Info()
    print("Pole\t= {}".format(Kolo1.Area()))
    print("Obwod\t= {}".format(Kolo1.Circuit()))

    print(f"Liczba kół: {Kolo.Count}")
    Kolo2 = Kolo("K", 10)
    Kolo2.Info()
    print("Pole\t= {}".format(Kolo2.Area()))
    print("Obwod\t= {}".format(Kolo2.Circuit()))

    print(f"Liczba kół: {Kolo.Count}")
    Kolo3 = Kolo("K", 100)
    Kolo3.Info()
    print("Pole\t= {}".format(Kolo3.Area()))
    print("Obwod\t= {}".format(Kolo3.Circuit()))

    print(f"Liczba kół: {Kolo.Count}")

if __name__ == "__main__":
    main()
