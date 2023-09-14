print('--------------------')

"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author:  Lubomír Chytil
email:   lubomir.chytil@lionscz.cz
mobil:   777 101 245
discord: Luboš Ch.#4345
"""

# IMPORTUJE TEXT
# import ...
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

# PŘIHLÁSÍ DO SYSTÉMU
# vstupní data
registered_users = {"bob":"123", "ann":"pass123", "mike":"password123", "liz":"pass123"}
print("$ python projekt1.py")

# vyžádá si od uživatele přihlašovací jméno a heslo
user = input("username: ")
password = input("password: ")

'''
NÁSLEDUJÍCÍ ZÁPIS JSEM OPRAVIL, VIZ NÍŽE
# zjistí, jestli zadané údaje odpovídají někomu z registrovaných uživatelů
if user in registered_users.keys() and password == registered_users[user]:
    # pokud je registrovaný, pozdrav jej a umožni mu analyzovat texty
    print("-" * 40)
    print("Welcome to the app, bob")
    print("We have 3 texts to be analyzed.")
    print("-" * 40)

# pokud není registrovaný, upozorni jej a ukonči program
else:
    print("Unregistered user, terminating the program..")
    exit()
    '''

# zjistí, jestli zadané údaje odpovídají někomu z registrovaných uživatelů
if password == registered_users.get(user):
    # pokud jsou jméno a heslo zadána správně, pozdraví jej a umožni mu pokračovat v programu
    print("-" * 40)
    print("Welcome to the app, bob")
    print("We have 3 texts to be analyzed.")
    print("-" * 40)   
else:
    # v ostatních přípacech ukončí program
    print("Unregistered user, terminating the program..")
    exit()   


# VYBERE VARIANTY TEXTU
# nechá uživatele vybrat mezi třemi texty, uloženými v proměnné TEXTS
number_btw = input("Enter an integer btw. 1 and 3 to select: ")

'''
NÁSLEDUJÍCÍ ZÁPIS JSEM OPRAVIL, VIZ NÍŽE
# zkontroluje, zda je zadaná hodnota číslo
if int(number_btw.isdigit()):
        # zkontroluje, zda je číslo v rozsahu 1-3
    if int(number_btw) < 1 or int(number_btw) > 3:
        print("The entered number is not in the range 1-3, the program ends.")
        exit()
    else:
        print("-" * 40)
# pokud zadaná hodnota není číslo
else:
     print("The entered value is not a number, the program ends.")
     exit()
'''

# zkontroluje, zda je zadaná hodnota celé číslo v rozsahu 1 až 3
try:
    # zkontroluje, zda je zadaná hodnota celé číslo v rozsahu 1 až 3
    if int(number_btw) in range(1, 4):
        print("-" * 40)
    # pro ostatní případy, tzn. zadaná hodnota je celé číslo, ale mimo rozsah 1 až 3
    else:
        print("The entered value is an integer, but not in the range 1 to 3, the program ends")
except:
    # pro ostatní případy, tzn. zadaná hodnota není celé číslo
    print(f"The entered value is not a integer, the program ends.")

# vybraný text
text = TEXTS[int(number_btw)-1]


# SPOČÍTÁ POŽADOVANÉ CHARAKTERISTIKY A VYPÍŠE JE
# počet slov
pocet_slov = len(text.split())
print(f"There are {pocet_slov} words in the selected text.")

'''
NÁSLEDUJÍCÍ ZÁPIS JSEM OPRAVIL, VIZ NÍŽE
# 1. počet slov začínajících velkým písmenem
pocet_slov_zacinajicich_velkym_pismenem = 0
for slovo in text.split():
    if slovo.istitle():
        pocet_slov_zacinajicich_velkym_pismenem += 1
print(f"There are {pocet_slov_zacinajicich_velkym_pismenem} titlecase words.")
     
# 2. počet slov psaných velkými písmeny
pocet_slov_psanych_velkymi_pismeny = 0
for slovo in text.split():
    if slovo.isupper() and slovo.isalpha():
        pocet_slov_psanych_velkymi_pismeny += 1
print(f"There are {pocet_slov_psanych_velkymi_pismeny} uppercase words.")

# 3. počet slov psaných malými písmeny
pocet_slov_psanych_malymi_pismeny = 0
for slovo in text.split():
    if slovo.islower(): # and slovo.isalpha():
        pocet_slov_psanych_malymi_pismeny += 1
print(f"There are {pocet_slov_psanych_malymi_pismeny} lowercase words.")

# 4. počet čísel (ne cifer)
pocet_cisel = 0
for slovo in text.split():
    if slovo.isdigit():
        pocet_cisel += 1
print(f"There are {pocet_cisel} numeric strings.")

# 5. suma všech čísel (ne cifer) v textu
soucet_cisel = 0
for slovo in text.split():
    if slovo.isdigit():
        soucet_cisel += int(slovo)
print(f"The sum of all the numbers {soucet_cisel}")
'''

# připraví proměnné pro požadované charakteristiky
pocet_slov_zacinajicich_velkym_pismenem = 0
pocet_slov_psanych_velkymi_pismeny = 0
pocet_slov_psanych_malymi_pismeny = 0
pocet_cisel = 0
soucet_cisel = 0

# zjistí pomocí for cyklu požadované charakteristiky
for slovo in text.split():
    if slovo.istitle():
        pocet_slov_zacinajicich_velkym_pismenem += 1
    if slovo.isupper() and slovo.isalpha():
        pocet_slov_psanych_velkymi_pismeny += 1
    if slovo.islower(): # and slovo.isalpha():
        pocet_slov_psanych_malymi_pismeny += 1
    if slovo.isdigit():
        pocet_cisel += 1
    if slovo.isdigit():
        soucet_cisel += int(slovo)

# vypíše požadované charakteristiky
print(f"There are {pocet_slov_zacinajicich_velkym_pismenem} titlecase words.")
print(f"There are {pocet_slov_psanych_velkymi_pismeny} uppercase words.")
print(f"There are {pocet_slov_psanych_malymi_pismeny} lowercase words.")
print(f"There are {pocet_cisel} numeric strings.")
print(f"The sum of all the numbers {soucet_cisel}")


# ZJISTÍ ČETNOST RŮZNÝCH DÉLEK SLOV V TEXTU A VYPÍŠE TABULKU
# vypíše hlavičku tabulky
print("-" * 40)
print("{:>3} {:^1} {:^15} {:^1} {:<10}".format("LEN", "|", "OCCURENCES", "|", "NR."))
print("-" * 40)

'''
NÁSLEDUJÍCÍ ZÁPIS JSEM OPRAVIL, VIZ NÍŽE
# očistí text od čárek mezi slovy a teček na konci věty
text = text.replace(",", "")        
text = text.replace(".", "")
'''
# očistí text od čárek mezi slovy a teček na konci věty a znovu zjistí počet slov
text = text.replace(",", "").replace(".", "")

''' 
vytvořil jsem nový následující řádek a zjistil jsem v něm počet slov v textu očištěném od čárek a teček
'''
pocet_slov = len(text.split())

# převede text ve stringu na text v listu
text_v_listu = text.split()

# vytvoří list, kde namísto slov jsou čísla vyjadřující délku slova
list_s_delky_slov = []
for cislo_slova in range(pocet_slov):
    list_s_delky_slov.append(len(text_v_listu[cislo_slova]))

# zjistí délku nejdelšího slova
delka_nejdelsiho_slova = max(list_s_delky_slov)

# zjistí a vypíše délky slov a jejich počet výskytů
for delka_slova in range(delka_nejdelsiho_slova):
    pocet_vyskytu_delky_slova = list_s_delky_slov.count(delka_slova+1)
    print("{:>3} {:^1} {:<15} {:^1} {:<10}".format(
        delka_slova+1,
        "|",
        "*" * pocet_vyskytu_delky_slova,
        "|",
        pocet_vyskytu_delky_slova
        ))
