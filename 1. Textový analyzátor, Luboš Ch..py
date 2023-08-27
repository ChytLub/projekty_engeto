print('--------------------')

"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Lubomír Chytil
email: lubomir.chytil@lionscz.cz
discord: Luboš Ch.
"""
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

# vstupní data
registered_users = {"bob":"123", "ann":"pass123", "mike":"password123", "liz":"pass123"}
print("$ python projekt1.py")

# vyžádá si od uživatele přihlašovací jméno a heslo
user = input("username: ")
password = input("password: ")


# zjistí, jestli zadané údaje odpovídají někomu z registrovaných uživatelů
if user in registered_users.keys() and password == registered_users[user]:
    # pokud je registrovaný, pozdrav jej a umožni mu analyzovat texty
    print("-" * 40)
    print("Welcome to the app, bob")
    print("We have 3 texts to be analyzed.")
    print("-" * 40)

# pokud není registrovaný, upozorni jej a ukonči program
else:
        print("unregistered user, terminating the program..")
        
# nechá uživatele vybrat mezi třemi texty, uloženými v proměnné TEXTS
number_btw = input("Enter a number btw. 1 and 3 to select: ")

# zkontroluje, zda je zadaná hodnota číslo
if int(number_btw.isdigit()):
        # zkontroluje, zda je číslo v rozsahu 1-3
    if int(number_btw) < 1 or int(number_btw) > 3:
        print("Zadané číslo není v rozsahu 1-3, program končí.")
    else:
        print("-" * 40)
# pokud zadaná hodnota není číslo
else:
     print("Zadaná hodnota není číslo, program končí.")

# vybraný text
text = TEXTS[int(number_btw)-1]

# SPOČÍTÁ NÁSLEDUJÍCÍ CHARAKTERISTIKY
# počet slov
pocet_slov = len(text.split())
print(f"There are {pocet_slov} words in the selected text.")

# počet slov začínajících velkým písmenem
pocet_slov_zacinajicich_velkym_pismenem = 0
for slovo in text.split():
    if slovo.istitle():
        pocet_slov_zacinajicich_velkym_pismenem += 1
print(f"There are {pocet_slov_zacinajicich_velkym_pismenem} titlecase words.")
     
# počet slov psaných velkými písmeny
pocet_slov_psanych_velkymi_pismeny = 0
for slovo in text.split():
    if slovo.isupper() and slovo.isalpha():
        pocet_slov_psanych_velkymi_pismeny += 1
print(f"There are {pocet_slov_psanych_velkymi_pismeny} uppercase words.")

# počet slov psaných malými písmeny
pocet_slov_psanych_malymi_pismeny = 0
for slovo in text.split():
    if slovo.islower(): # and slovo.isalpha():
        pocet_slov_psanych_malymi_pismeny += 1
print(f"There are {pocet_slov_psanych_malymi_pismeny} lowercase words.")

# počet čísel (ne cifer)
pocet_cisel = 0
for slovo in text.split():
    if slovo.isdigit():
        pocet_cisel += 1
print(f"There are {pocet_cisel} numeric strings.")

# suma všech čísel (ne cifer) v textu
soucet_cisel = 0
for slovo in text.split():
    if slovo.isdigit():
        soucet_cisel += int(slovo)
print(f"The sum of all the numbers {soucet_cisel}")

# ČETNOST RŮZNÝCH DÉLEK SLOV V TEXTU
# vypíše hlavičku tabulky
print("-" * 40)
print("{:>3} {:^1} {:^15} {:^1} {:<10}".format("LEN", "|", "OCCURENCES", "|", "NR."))
print("-" * 40)

# očistí text od čárek mezi slovy a teček na konci věty
text = text.replace(",", "")        
text = text.replace(".", "")

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

    # print("{:>5} {:^15} {:<10}".format(nazvy[i], ceny[i], cisla[i]))


