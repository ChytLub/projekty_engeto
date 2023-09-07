print()

"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie - piškvorky
author:  Lubomír Chytil
email:   lubomir.chytil@lionscz.cz
mobil:   777 101 245
discord: Luboš Ch.#4345

Ochrana před automatickým doplňováním znaků X a O do pozic mimo tabulku
1. Program má tendenci automaticky kopírovat znaky X a O z tabulky do pozic mimo tabulku
2. Program automaticky tyto nakopírované znaky započítává do kontrolované řady 5-ti znaků směrem doleva nahoru
3. Program by díky nakopírovaným znakům hlásil výhru s řadou 5-ti znaků i v případě, že řada neexistuje
2. Jako ochrana před tímto automatickým kopírováním slouží jeden prázdný řádek pod tabulkou a prázdný sloupec za tabulkou
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
    print()
    # vytvoří čísla sloupců nad tabulkou  a vypíše je
    sloupce = list(range(1, len(tabulka[0]) + 1 - 1))
    sloupce_str = "  " + "  ".join("{: ^2}".format(i) for i in sloupce)
    print("   " + sloupce_str)

    # vytvoří oddělovací čáru pod čísly sloupců a vytiskne ji
    oddelovaci_cara = "+" + "---+" * (len(tabulka[0]) - 1)
    print("   " + oddelovaci_cara)

    # vytvoří tabulku s čísly řádků
    for i, radek in enumerate(tabulka):
        radek_str = " " + "| ".join("{: ^2}".format(cell) for cell in radek)
        if i == (len(tabulka)) - 1:
            break
        print(f"{i + 1:2} |{radek_str}")

        # vypíše oddělovací čáru mezi řádky a pod tabulkou
        if i < (len(tabulka)) - 1:
            print("   " + oddelovaci_cara)
    print()                             # vloží pod tabulku prázdný řádek


def vloz_text(tabulka, radek, sloupec, text):
    tabulka[radek][sloupec] = text


def zkontroluj_vodorovne(a, b): # zkontroluje vodorovnou řadu, a = index řádku, b = index sloupce
    try:
        # c = -2 zkontroluje: vodorovnou řadu 5-ti znaků, střed lajny je 2 body doleva od aktuální polohy znaku
        # c = -1 zkontroluje: vodorovnou řadu 5-ti znaků, střed lajny je 1 bod doleva od aktuální polohy znaku
        # c =  0 zkontroluje: vodorovnou řadu 5-ti znaků, střed lajny je vycentrovaný na aktuální polohu znaku
        # c = +1 zkontroluje: vodorovnou řadu 5-ti znaků, střed lajny je 1 bod doprava od aktuální polohy znaku
        # c = +2 zkontroluje: vodorovnou řadu 5-ti znaků, střed lajny je 2 body doprava od aktuální polohy znaku

        for c in range(-2,3):
            if tabulka[a][b-2+c] == tabulka[a][b-1+c] == tabulka[a][b+c] == tabulka[a][b+1+c] == tabulka[a][b+2+c]:
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

        for c in range(-2,3):
            if tabulka[a+2+c][b] == tabulka[a+1+c][b] == tabulka[a+0+c][b] == tabulka[a-1+c][b] == tabulka[a-2+c][b]:
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

        for c in range(-2,3):
            if tabulka[a+2+c][b-2-c] == tabulka[a+1+c][b-1-c] == tabulka[a+0+c][b-c] == tabulka[a-1+c][b+1-c] == tabulka[a-2+c][b+2-c]:
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

        for c in range(-2,3):
            if tabulka[a-2+c][b-2+c] == tabulka[a-1+c][b-1+c] == tabulka[a+c][b+c] == tabulka[a+1+c][b+1+c] == tabulka[a+2+c][b+2+c] == znak:
                return True

    except IndexError:
        return False


# 2. VYTVOŘÍ PRÁZDNOU TABULKU
# zadá a zkontroluje počet řádků
while True:
    pocet_radku = input("Write how many lines the playing area should have (whole number), minimum 5, maximum 30: ")
    try:
        pocet_radku = int(pocet_radku)
        if pocet_radku in range(5, 31):
            break
        else:
            print()
            print("Error - you did not enter a positive integer from 5 to 30, for example: 5, 7, 12.")
    except:
        print()
        print("Error - you did not enter a positive integer from 5 to 30, for example: 5, 7, 12.")
        
# zadá a zkontroluje počet sloupců
while True:
    pocet_sloupcu = input("Write how many columns the playing area should have (whole number), minimum 5, maximum 50: ")
    try:
        pocet_sloupcu = int(pocet_sloupcu)
        if pocet_sloupcu in range(5, 51):
            break
        else:
            print()
            print("Error - you did not enter a positive integer from 5 to 50, for example: 5, 7, 12.")
    except:
        print()
        print("Error - you did not enter a positive integer from 5 to 50, for example: 5, 7, 12.")

# vytvoří a vypíše prázdnou tabulku
tabulka = vytvor_tabulku((pocet_radku) + 1, (pocet_sloupcu) + 1)
tiskni_tabulku(tabulka)


# 3. NAČTE ZNAK, KTERÝM SE ZAČNE HRA (X NEBO O), A ZKONTROLUJE JEJ
while True:
    znak = input("Write the character you want to start the game with. The character can be x or o: ").upper()
    # zkontroluje, zda zadaný znam, ke 'x' nebo 'o'
    if znak == "EXIT":                  # ukončí program podle požadavku uživatele exit
        print()
        print("The program has been terminated.")
        exit()                              
    if znak == "X" or znak == "O":      # zkontroluje, zda uživatele zadal x nebo o
        print()
        break
    else:                               # pokud uživatele nezadal x, o ani exit
        print()
        print("Error - you did not enter the character x or o.")


# 4. SPUSTÍ HRU, HRA SE HRAJE
konec_hry = False                       # pomocná proměnná na ukončení hry pro vyhodnocování doposud volných buněk
pocet_zadanych_znaku = 0                # počet všech zadaných znaků X a O pro vyhodnocování doposud volných buněk
while True:         # spustí hru
    # zkontroluje, zda je ještě nějaká volná buňka pro zadávání znaků X a O
    pocet_bunek = pocet_radku * pocet_sloupcu
    if pocet_zadanych_znaku < pocet_bunek:
        pass
    else:
        print("Draw. All cells are occupied. Game Over.")
        exit()
    
    # zadá číslo řádku a zkontroluje jej
    while True:
        cislo_radku = input(f"Player {znak} - write the entire LINE NUMBER you want to insert {znak}:   ")
        if cislo_radku == "exit":
            print()
            print("The program has been terminated.")
            exit()
        try:
            if int(cislo_radku) in range(1, pocet_radku + 1):   # zda je číslo řádku celé číslo v rozsahu tabulky
                cislo_radku = int(cislo_radku)
                break                                           # číslo je zadané správně, ukončí se cyklus while
            else:
                print()
                print(f"Error - you did not enter a whole number, but not in the range 1 to {pocet_radku}.")
        except:
            print()
            print(f"Error - you did not enter an integer in the range 1 to {pocet_radku}.")

    # zadá číslo sloupce a zkontroluje jej
    while True:
        # zadá číslo sloupce a zkontroluje jej
        cislo_sloupce = input(f"Player {znak} - write the entire NUMBER of the COLUMN you want to insert into {znak}: ")
        if cislo_sloupce == "exit":
            print()
            print("The program has been terminated.")
            exit()
        try:
            if int(cislo_sloupce) in range(1, pocet_sloupcu + 1):   # zda je číslo řádku celé číslo v rozsahu tabulky
                cislo_sloupce = int(cislo_sloupce)
                break                                           # číslo je zadané správně, ukončí se cyklus while
            else:
                print()
                print(f"Error - you did not enter a whole number, but not in the range 1 to {pocet_sloupcu}.")
        except:
            print()
            print(f"Error - you did not enter an integer in the range 1 to {pocet_sloupcu}.")

    # zkontroluje, zda je navolená pozice ještě volná nebo zda je již obsazená
    index_radku = cislo_radku - 1
    index_sloupce = cislo_sloupce - 1
    
    if tabulka[index_radku][index_sloupce] == "X" or tabulka[index_radku][index_sloupce] == "O":
        print(f"Row position = {index_radku + 1} column = {index_sloupce + 1} is already occupied.")
        print("Place your character in another position.")    # pokud je pozice již obsazená
        continue                                        # program se vrátí se na začátek a hráč zadá jinou pozici
    else:                                           # pokud je pozice ještě volná
        vloz_text(tabulka, index_radku, index_sloupce, znak)    # vloží do tabulky zadaný znak
        tiskni_tabulku(tabulka)                      # vypíše tabulku
        pocet_zadanych_znaku += 1


    # 5. ZKONTROLUJE ŘADU 5-TI ZNAKŮ A UKONČÍ HRU
    # zkontroluje vodorovnou řadu 5-ti znaků (tabulka[index_radku][index_sloupce-1]) a případně ukončí hru
    konec_hry = zkontroluj_vodorovne(index_radku, index_sloupce)
    if konec_hry == True:
        print(f"Win. The player {znak} won the game. A row of 5 characters is horizontal. Game Over.")
        print()
        break

    # zkontroluje svislou řadu 5-ti znaků (tabulka[index_radku][index_sloupce-1]) a případně ukončí hru
    konec_hry = zkontroluj_svisle(index_radku, index_sloupce)
    if konec_hry == True:
        print(f"Win. The player {znak} won the game. A row of 5 characters is vertical. Game Over.")
        print()
        break
    
    # zkontroluje řadu 5-ti znaků šikmo doprava nahoru (tabulka[index_radku][index_sloupce-1]) a případně ukončí hru
    konec_hry = zkontroluj_šikmo_doprava_nahoru(index_radku, index_sloupce)
    if konec_hry == True:
        print(f"Win. The player {znak} won the game. The row of 5 characters is diagonally upwards to the right. Game Over.")
        print()
        break

    # zkontroluje řadu 5-ti znaků šikmo doleva nahoru (tabulka[index_radku][index_sloupce-1]) a případně ukončí hru
    konec_hry = zkontroluj_šikmo_doleva_nahoru(index_radku, index_sloupce)
    if konec_hry == True:
        print(f"Win. The player {znak} won the game. The row of 5 characters is diagonally left upwards. Game Over.")
        print()
        break
    
    # pro další kolo změní znak X na O (nebo O na X)
    if znak == "X":
        znak = "O"
    else:
        znak = "X"
