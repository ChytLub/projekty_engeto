print()

"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie - piškvorky
author:  Lubomír Chytil
email:   lubomir.chytil@lionscz.cz
mobil:   777 101 245
discord: Luboš Ch.#4345
"""

print("Welcome to Tic Tac Toe")
print("========================================")
print("GAME RULES:")
print("The game is played by two players - a player with X mark and a Y mark player.")
print("The players first choose the size of the playing field.")
print("Each player can place one token (or stone) per turn.")
print("The winner is the one who manages to place 5 of his brands in:")
print("* horizontal")
print("* vertical or")
print("* diagonal row")

print("========================================")
print("Ending the game - to exit the game at any time, type the word: exit")

print("========================================")
print("Let's start the game")
print("----------------------------------------")
print()


# 1. DEFINUJE FUNKCE
def vytvor_tabulku(pocet_radku, pocet_sloupcu):
    tabulka = [["" for _ in range(pocet_sloupcu)] for _ in range(pocet_radku)]
    return tabulka

def tiskni_tabulku(tabulka):
    horizontalni_carra ="   " + "+---" * (len(tabulka[0])) + "+"
    cisla_sloupcu = "     " + "   ".join(str(i + 1) for i in range(len(tabulka[0])))
    print(cisla_sloupcu)
    print(horizontalni_carra)
    for i, radek in enumerate(tabulka):
        print(f"{i + 1:2} |", end="")
        for buňka in radek:
            print(f" {buňka.center(2)}|", end="")
        print("\n" + horizontalni_carra)

def vloz_text(tabulka, radek, sloupec, text):
    tabulka[radek][sloupec] = text

def zkontroluj_vodorovne(a, b): # 'a' představuje index_radku, 'b' představuje index_sloupce
    try:
        # c = -2 zkontroluje: vodorovnou řadu 5-ti znaků, střed lajny je 2 body doleva od aktuální polohy znaku
        # c = -1 zkontroluje: vodorovnou řadu 5-ti znaků, střed lajny je 1 bod doleva od aktuální polohy znaku
        # c =  0 zkontroluje: vodorovnou řadu 5-ti znaků, střed lajny je vycentrovaný na aktuální polohu znaku
        # c = +1 zkontroluje: vodorovnou řadu 5-ti znaků, střed lajny je 1 bod doprava od aktuální polohy znaku
        # c = +2 zkontroluje: vodorovnou řadu 5-ti znaků, střed lajny je 2 body doprava od aktuální polohy znaku

        for c in range (-2,3):
            if tabulka[a][b-3+c] == tabulka[a][b-2+c] == tabulka[a][b-1+c] == tabulka[a][b+c] == tabulka[a][b+1+c]:
                return True

    except IndexError:
        return False


def zkontroluj_svisle(a, b): # 'a' představuje index_radku, 'b' představuje index_sloupce
    try:
        # c = -2 zkontroluje svislou řadu 5-ti znaků, střed lajny je 2 body nahoru od aktuální polohy znaku
        # c = -1 zkontroluje svislou řadu 5-ti znaků, střed lajny je 1 bod nahoru od aktuální polohy znaku
        # c =  0 zkontroluje svislou řadu 5-ti znaků, střed lajny je vycentrovaný na aktuální polohu znaku
        # c = +1 zkontroluje svislou řadu 5-ti znaků, střed lajny je 1 bod dolů od aktuální polohy znaku
        # c = +2 zkontroluje svislou řadu 5-ti znaků, střed lajny je 2 body dolů od aktuální polohy znaku

        for c in range (-2,3):
            if tabulka[a+2+c][b-1] == tabulka[a+1+c][b-1] == tabulka[a+0+c][b-1] == tabulka[a-1+c][b-1] == tabulka[a-2+c][b-1]:
                return True

    except IndexError:
        return False


def zkontroluj_šikmo_doprava_nahoru(a, b): # 'a' představuje index_radku, 'b' představuje index_sloupce
    try:
        # c = -2 zkontroluje šikmou řadu 5-ti znaků, střed lajny je 2 body nahoru doprava od aktuální polohy znaku
        # c = -1 zkontroluje šikmou řadu 5-ti znaků, střed lajny je 1 bod nahoru doprava od aktuální polohy znaku
        # c =  0 zkontroluje šikmou řadu 5-ti znaků, střed lajny je vycentrovaný na aktuální polohu znaku
        # c = +1 zkontroluje šikmou řadu 5-ti znaků, střed lajny je 1 bod dolů doleva od aktuální polohy znaku
        # c = +2 zkontroluje šikmou řadu 5-ti znaků, střed lajny je 2 body dolů doleva od aktuální polohy znaku

        for c in range (-2,3):
            if tabulka[a+2+c][b-3-c] == tabulka[a+1+c][b-2-c] == tabulka[a+0+c][b-1-c] == tabulka[a-1+c][b+0-c] == tabulka[a-2+c][b+1-c]:
                return True

    except IndexError:
        return False


def zkontroluj_šikmo_doleva_nahoru(a, b): # 'a' představuje index_radku, 'b' představuje index_sloupce
    try:
        # c = -2 zkontroluje šikmou řadu 5-ti znaků, střed lajny je 2 body nahoru doleva od aktuální polohy znaku
        # c = -1 zkontroluje šikmou řadu 5-ti znaků, střed lajny je 1 bod nahoru doleva od aktuální polohy znaku
        # c =  0 zkontroluje šikmou řadu 5-ti znaků, střed lajny je vycentrovaný na aktuální polohu znaku
        # c = +1 zkontroluje šikmou řadu 5-ti znaků, střed lajny je 1 bod dolů doprava od aktuální polohy znaku
        # c = +2 zkontroluje šikmou řadu 5-ti znaků, střed lajny je 2 body dolů doprava od aktuální polohy znaku

        for c in range (-2,3):
            if tabulka[a-2+c][b-3+c] == tabulka[a-1+c][b-2+c] == tabulka[a+0+c][b-1+c] == tabulka[a+1+c][b+0+c] == tabulka[a+2+c][b+1+c]:
                return True

    except IndexError:
        return False


# 2. VYTVOŘÍ PRÁZDNOU TABULKU
# zadá a zkontroluje počet řádků
while True:
    pocet_radku = input("Napiš, kolik řádků má mít hrací plocha (celé číslo), maximálně 30: ")
    print()
    try:
        pocet_radku = int(pocet_radku)
        if pocet_radku in range(1, 31):
            break
        else:
            print("Chyba - nezadal jsi kladné celé číslo, například: 5, 7, 12, maximálně 30.")
    except:
        print(f"Chyba - nezadal jsi číslo.")
        
# zadá a zkontroluje počet sloupců
while True:
    pocet_sloupcu = input("Napiš, kolik sloupců má mít hrací plocha (celé číslo), maximálně 50: ")
    print()
    try:
        pocet_sloupcu = int(pocet_sloupcu)
        if pocet_sloupcu in range(1, 51):
            break
        else:
            print("Chyba - nezadal jsi kladné celé číslo, například: 5, 7, 12, maximálně 50.")
    except:
        print(f"Chyba - nezadal jsi číslo.")

# vytvoří a vypíše prázdnou tabulku
tabulka = vytvor_tabulku(pocet_radku, pocet_sloupcu)
tiskni_tabulku(tabulka)


# 3. NAČTE ZNAK, KTERÝM SE ZAČNE HRA (X NEBO O), A ZKONTROLUJE JEJ
print()
while True:
    znak = input("Napiš znak, kterým chceš začít hru. Znakem může být x nebo o: ").upper()
    # zkontroluje, zda zadaný znam, ke 'x' nebo 'o'
    if znak == "EXIT":                  # ukončí program podle požadavku uživatele exit
        print()
        print("Program byl ukončený.")
        exit()                              
    if znak == "X" or znak == "O":      # zkontroluje, zda uživatele zadal x nebo o
        print()
        break
    else:                               # pokud uživatele nezadal x, o ani exit
        print()
        print("Špatně zadaný znak.")


# 4. SPUSTÍ HRU, HRA SE HRAJE
konec_hry = False
while True:         # spustí hru
    while True:
        # zadá číslo řádku a zkontroluje jej
        # první řádek tabulky s číslováním sloupců Python nepovažuje za první řádek tabulky
        cislo_radku = input(f"Hráč {znak} - zadej celé číslo řádku, do kterého chceš vložit {znak}:   ")
        print()
        if cislo_radku == "exit":
            print("Program byl ukončený.")
            exit()
        try:
            index_radku = int(cislo_radku) - 1
            if index_radku in range(0, pocet_radku):    # Císlo řádku je ve správném rozsahu
                break
            else:
                print(f"Chyba - nezadal jsi celé číslo řádku v rozsahu 1 až {pocet_radku}.")
        except:
            print(f"Chyba - nezadal jsi číslo řádku.")

    # zadá číslo sloupce a zkontroluje jej
    # první sloupec tabulky s číslováním řádků program považuje za první sloupec tabulky
    while True:
        cislo_sloupce = input(f"Hráč {znak} - zadej celé číslo sloupce, do kterého chceš vložit {znak}: ")
        print()
        if cislo_sloupce == "exit":
            print("Program byl ukončený.")
            exit()
        try:
            index_sloupce = int(cislo_sloupce)
            if index_sloupce in range(1, pocet_sloupcu + 1):    # Císlo řádku je ve správném rozsahu
                break
            else:
                print(f"Chyba - nezadal jsi celé číslo sloupce v rozsahu 1 až {pocet_sloupcu}.")
        except:
            print(f"Chyba - nezadal jsi číslo sloupce.")

    # vloží znak podle zadaného čísla řádku a čísla sloupce do tabulky a tabulku vypíše
    vloz_text(tabulka, index_radku, index_sloupce - 1, znak)
    tiskni_tabulku(tabulka)


    # 5. ZKONTROLUJE ŘADU 5-TI ZNAKŮ A UKONČÍ HRU
    # zkontroluje vodorovnou řadu 5-ti znaků (tabulka[index_radku][index_sloupce-1]) a případně ukončí hru
    konec_hry = zkontroluj_vodorovne(index_radku, index_sloupce)
    if konec_hry == True:
        print(f"Výhra. Hru vyhrál znak {znak}. Řada 5-ti znaků je vodorovně. Konec hry.")
        print()
        break

    # zkontroluje svislou řadu 5-ti znaků (tabulka[index_radku][index_sloupce-1]) a případně ukončí hru
    konec_hry = zkontroluj_svisle(index_radku, index_sloupce)
    if konec_hry == True:
        print(f"Výhra. Hru vyhrál znak {znak}. Řada 5-ti znaků je svisle. Konec hry.")
        print()
        break
    
    # zkontroluje řadu 5-ti znaků šikmo doprava nahoru (tabulka[index_radku][index_sloupce-1]) a případně ukončí hru
    konec_hry = zkontroluj_šikmo_doprava_nahoru(index_radku, index_sloupce)
    if konec_hry == True:
        print(f"Výhra. Hru vyhrál znak {znak}. Řada 5-ti znaků je šikmo doprava nahoru. Konec hry.")
        print()
        break

    # zkontroluje řadu 5-ti znaků šikmo doleva nahoru (tabulka[index_radku][index_sloupce-1]) a případně ukončí hru
    konec_hry = zkontroluj_šikmo_doleva_nahoru(index_radku, index_sloupce)
    if konec_hry == True:
        print(f"Výhra. Hru vyhrál znak {znak}. Řada 5-ti znaků je šikmo doleva nahoru. Konec hry.")
        print()
        break

    # pro další kolo změní znak X na O (nebo O na X)
    if znak == "X":
        znak = "O"
    else:
        znak = "X"

'''
5. PŘEBYTKY PRO LEPŠÍ POROZUMĚNÍ PROGRAMU
DEFINICE FUNKCE zkontroluj_vodorovne(a, b):
def zkontroluj_vodorovne(a, b): # 'a' představuje index_radku, 'b' představuje index_sloupce
    try:
        # první řádek zkontroluje:  vodorovnou řadu 5-ti znaků, střed lajny je 2 body doleva od aktuální polohy znaku
        # druhý řádek zkontroluje:  vodorovnou řadu 5-ti znaků, střed lajny je 1 bod doleva od aktuální polohy znaku
        # třetí řádek zkontroluje:  vodorovnou řadu 5-ti znaků, střed lajny je vycentrovaný na aktuální polohu znaku
        # čtvrtý řádek zkontroluje: vodorovnou řadu 5-ti znaků, střed lajny je 1 bod doprava od aktuální polohy znaku
        # pátý řádek zkontroluje:   vodorovnou lařadujnu 5-ti znaků, střed lajny je 2 body doprava od aktuální polohy znaku

        if (
               tabulka[a][b-5] == tabulka[a][b-4] == tabulka[a][b-3] == tabulka[a][b-2] == tabulka[a][b-1] # 5
            or tabulka[a][b-4] == tabulka[a][b-3] == tabulka[a][b-2] == tabulka[a][b-1] == tabulka[a][b]  # 4
            or tabulka[a][b-3] == tabulka[a][b-2] == tabulka[a][b-1] == tabulka[a][b] == tabulka[a][b+1]  # 3
            or tabulka[a][b-2] == tabulka[a][b-1] == tabulka[a][b] == tabulka[a][b+1] == tabulka[a][b+2]  # 2
            or tabulka[a][b-1] == tabulka[a][b] == tabulka[a][b+1] == tabulka[a][b+2] == tabulka[a][b+3]  # 1
        ):
            return True
    except IndexError:
        return False

        
DEFINICE FUNKCE zkontroluj_svisle(a, b):
def zkontroluj_svisle(a, b): # 'a' představuje index_radku, 'b' představuje index_sloupce
    try:
        # zkontroluje svislou řadu 5-ti znaků, střed lajny je 2 body nahoru od aktuální polohy znaku
        # zkontroluje svislou řadu 5-ti znaků, střed lajny je 1 bod nahoru od aktuální polohy znaku
        # zkontroluje svislou řadu 5-ti znaků, střed lajny je vycentrovaný na aktuální polohu znaku
        # zkontroluje svislou řadu 5-ti znaků, střed lajny je 1 bod dolů od aktuální polohy znaku
        # zkontroluje svislou řadu 5-ti znaků, střed lajny je 2 body dolů od aktuální polohy znaku

        if (
               tabulka[a+0][b-1] == tabulka[a-1][b-1] == tabulka[a-2][b-1] == tabulka[a-3][b-1] == tabulka[a-4][b-1]
            or tabulka[a+1][b-1] == tabulka[a+0][b-1] == tabulka[a-1][b-1] == tabulka[a-2][b-1] == tabulka[a-3][b-1]
            or tabulka[a+2][b-1] == tabulka[a+1][b-1] == tabulka[a+0][b-1] == tabulka[a-1][b-1] == tabulka[a-2][b-1]
            or tabulka[a+3][b-1] == tabulka[a+2][b-1] == tabulka[a+1][b-1] == tabulka[a+0][b-1] == tabulka[a-1][b-1]
            or tabulka[a+4][b-1] == tabulka[a+3][b-1] == tabulka[a+2][b-1] == tabulka[a+1][b-1] == tabulka[a-0][b-1]
        ):
            return True
    except IndexError:
        return False        

        
DEFINICE FUNKCE zkontroluj_šikmo_doprava_nahoru(a, b):
def zkontroluj_šikmo_doprava_nahoru(a, b): # 'a' představuje index_radku, 'b' představuje index_sloupce
    try:
        # zkontroluje svislou řadu 5-ti znaků, střed lajny je 2 body nahoru doprava od aktuální polohy znaku
        # zkontroluje svislou řadu 5-ti znaků, střed lajny je 1 bod nahoru doprava od aktuální polohy znaku
        # zkontroluje svislou řadu 5-ti znaků, střed lajny je vycentrovaný na aktuální polohu znaku
        # zkontroluje svislou řadu 5-ti znaků, střed lajny je 1 bod dolů doleva od aktuální polohy znaku
        # zkontroluje svislou řadu 5-ti znaků, střed lajny je 2 body dolů doleva od aktuální polohy znaku

        if (
               tabulka[a+0][b-1] == tabulka[a-1][b+0] == tabulka[a-2][b+1] == tabulka[a-3][b+2] == tabulka[a-4][b+3]
            or tabulka[a+1][b-2] == tabulka[a+0][b-1] == tabulka[a-1][b+0] == tabulka[a-2][b+1] == tabulka[a-3][b+2]
            or tabulka[a+2][b-3] == tabulka[a+1][b-2] == tabulka[a+0][b-1] == tabulka[a-1][b+0] == tabulka[a-2][b+1]
            or tabulka[a+3][b-4] == tabulka[a+2][b-3] == tabulka[a+1][b-2] == tabulka[a+0][b-1] == tabulka[a-1][b+0]
            or tabulka[a+4][b-5] == tabulka[a+3][b-4] == tabulka[a+2][b-3] == tabulka[a+1][b-2] == tabulka[a-0][b-1]
        ):
            return True
    except IndexError:
        return False


DEFINICE FUNKCE zkontroluj_šikmo_doleva_nahoru(a, b):
def zkontroluj_šikmo_doleva_nahoru(a, b): # 'a' představuje index_radku, 'b' představuje index_sloupce
    try:
        # zkontroluje svislou řadu 5-ti znaků, střed lajny je 2 body nahoru doleva od aktuální polohy znaku
        # zkontroluje svislou řadu 5-ti znaků, střed lajny je 1 bod nahoru doleva od aktuální polohy znaku
        # zkontroluje svislou řadu 5-ti znaků, střed lajny je vycentrovaný na aktuální polohu znaku
        # zkontroluje svislou řadu 5-ti znaků, střed lajny je 1 bod dolů doprava od aktuální polohy znaku
        # zkontroluje svislou řadu 5-ti znaků, střed lajny je 2 body dolů doprava od aktuální polohy znaku

        if (
               tabulka[a-4][b-5] == tabulka[a-3][b-4] == tabulka[a-2][b-3] == tabulka[a-1][b-2] == tabulka[a+0][b-1]
            or tabulka[a-3][b-4] == tabulka[a-2][b-3] == tabulka[a-1][b-2] == tabulka[a+0][b-1] == tabulka[a+1][b+0]
            or tabulka[a-2][b-3] == tabulka[a-1][b-2] == tabulka[a+0][b-1] == tabulka[a+1][b+0] == tabulka[a+2][b+1]
            or tabulka[a-1][b-2] == tabulka[a+0][b-1] == tabulka[a+1][b+0] == tabulka[a+2][b+1] == tabulka[a+3][b+2]
            or tabulka[a+0][b-1] == tabulka[a+1][b-0] == tabulka[a+2][b+1] == tabulka[a+3][b+2] == tabulka[a+4][b+3]
        ):
            return True
    except IndexError:
        return False
'''





