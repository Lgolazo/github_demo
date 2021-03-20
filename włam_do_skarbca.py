from sys import exit
imie = input("Jak masz na imię? ")
print("Czesc " + imie.title())
print("Chciałbym Cię zaprosić do gry Włam się do Skarbca. \nSterowanie w grze za pomocą klawiatury numerycznej")
print("Przed Tobą pierwsze drzwi. \nMasz 3 możliwosci do wyboru: ")
print("1. Otwierasz drzwi wytrychem \n2. Próbujesz wyłamać drzwi łomem \n3. Kopiesz je z buta.")

# Pierwszy droga wybór pierwszej opcji
wybor1 = input("Wpisz co wybierasz: ")
if wybor1 == "1":
    print("Po kilku minutach udaje Ci się otworzyć drzwi \nGratulacje!!! \nIdziesz dalej")
    print("Po wejsciu masz dwie drogi wyboru: \n1. Drzwi po lewej stronie \n2. Drzwi po prawej stronie ")
elif wybor1 == "2":
    print("Udało Ci się wywarzyć drzwi łomem \nGratulacje!!! \nIdziesz dalej")
    print("Po wejsciu masz dwie drogi wyboru: \n1. Drzwi po lewej stronie \n2. Drzwi po prawej stronie ")
elif wybor1 ==  '3':
    print("Drzwi okazały się za mocne. \nZłamałes nogę \nNiestety na tym Twoja przygoda się kończy.")
    exit()
def kuchnia():
    # Drugi poziom
    drzwi = input("Które drzwi wybierasz? ")
    if drzwi == "1":
        print("Przekręcasz klamkę, okazuje się że drzwi są otwarte. \nTrafiłes do kuchnii, ze stołu kradniesz kawałek kiełbasy")
        print("Wracasz z powrotem")
        print("2. Drzwi po prawej stronie")
        while True:
            drzwi_lvl2 = input("Drzwi po prawej wcisnij klawisz '2': ")
            if drzwi_lvl2 == "2":
                break
        print("Znalazłes się w wielkim holu, przed sobą widzisz drzwi do skarbca.")
        print("Niestety żeby się tam dostać musisz złamać kod")
        print("Żeby złamać kod musisz rozwiązać zadanie matematyczne: Ile to jest 2+2")
        while True:
            wejscie = input("Podaj poprawny wynik: ")
            if wejscie == "4":
                print("Uzyskałes dostęp. \nBrawo udało Ci się dostać do skarbca. \nKoniec Gry!!!")
                break
            print("Zły kod spróbuj jeszcze raz.")
    elif drzwi == "2": 
        print("Znalazłes się w wielkim holu, przed sobą widzisz drzwi do skarbca.")       
        print("Niestety żeby się tam dostać musisz złamać kod")
        print("Żeby złamać kod musisz rozwiązać zadanie matematyczne: Ile to jest 2+2")
        while True:
            wejscie = input("Podaj poprawny wynik: ")
            if wejscie == "4":
                print("Uzyskałes dostęp. \nBrawo udało Ci się dostać do skarbca. \nKoniec Gry!!!")
                break
            print("Zły kod spróbuj jeszcze raz.")
kuchnia()