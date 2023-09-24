
"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie - piškvorky
author:  Lubomír Chytil
email:   lubomir.chytil@lionscz.cz
mobil:   777 101 245
discord: Luboš Ch.#4345

INFORMACE O DOKONČENOSTI PROGRAMU
1. Výstupní soubor neobsahuje informace v různých sloupcích, všechny informace jsou uvedené ve sloupci A
2. Program neumí načítat data z okrsků
3. Program neobsahuje kontrolu zadaných parametrů - zda byla zadaná URL adesa a zda byl zadaný formát .csv

POKYNY PRO SPUŠTĚNÍ PROGRAMU
Přesuňte se do terminálu (nebo příkazového řádku) a pro okres Prostějov zadejte:
python volby.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103" vysledky_prostejov.csv
"""

# VSTUPY
print("Program importuje knihovny.")
# importuje knihovny
import sys
import os
sys.path.append(r'C:\Users\Lubomír Chytil\Documents\Vzdělávací programy\Výpočetní technika\Python\ENGETO\domácí úkoly\Volby_env\Lib\site-packages')
import requests
from bs4 import BeautifulSoup
import csv

def stahni_zakladni_informace(zakladni_url):
    print("Stahuji základní informace o obcích.")
    odp_serveru_zakladni_web = requests.get(zakladni_url)
    
    if odp_serveru_zakladni_web.status_code != 200:
        print("Základní webová stránka se nesměla, program končí.")
        sys.exit(1)
    
    polevka = BeautifulSoup(odp_serveru_zakladni_web.text, "html.parser")
    vsechny_tabulky = polevka.find_all("table", {"class": "table"})
    
    seznam_obci = {}
    
    for tabulka_tag_table in vsechny_tabulky:
        caption = tabulka_tag_table.find("caption")
        if caption:
            nazev_tabulky = caption.text.strip()
            print(f"Data z tabulky: {nazev_tabulky}")
        
        vsechny_tr = tabulka_tag_table.find_all("tr")
        
        for tr in vsechny_tr[1:]:
            td_na_radku = tr.find_all("td")
            if len(td_na_radku) >= 3:
                cislo_obce_text = td_na_radku[0].get_text().strip()
                if cislo_obce_text.isdigit():
                    cislo_obce = int(cislo_obce_text)
                    nazev_obce = td_na_radku[1].get_text().strip()
                    seznam_obci[nazev_obce] = cislo_obce
    
    return seznam_obci

def stahni_specifikace_obci(seznam_obci):
    print("Stahuji specifikace obcí.")
    for nazev_obce, cislo_obce in seznam_obci.items():
        specificka_url = f'https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=12&xobec={cislo_obce}&xvyber=7103'
        odp_serveru_specificky_web = requests.get(specificka_url)
        
        if odp_serveru_specificky_web.status_code != 200:
            print(f"Webová stránka pro obec {nazev_obce} se nesměla, program končí.")
            sys.exit(1)
        
        polevka_specificka = BeautifulSoup(odp_serveru_specificky_web.text, "html.parser")
        tabulka_specificka = polevka_specificka.find("table", {"class": "table"})
        vsechny_tr = tabulka_specificka.find_all("tr")
        treti_radek = vsechny_tr[2]
        td_na_radku = treti_radek.find_all("td")
        
        volici_v_seznamu = td_na_radku[3].get_text()
        vydane_obalky = td_na_radku[4].get_text().strip()
        platne_hlasy = td_na_radku[7].get_text().strip()
        
        seznam_obci[nazev_obce] = [cislo_obce, volici_v_seznamu, vydane_obalky, platne_hlasy]
    
def stahni_politicke_strany(seznam_obci):
    print("Stahuji politické strany.")
    for nazev_obce, cislo_obce in seznam_obci.items():
        specificka_url = f'https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=12&xobec={cislo_obce}&xvyber=7103'
        odp_serveru_specificky_web = requests.get(specificka_url)
        
        if odp_serveru_specificky_web.status_code != 200:
            print(f"Webová stránka pro obec {nazev_obce} se nesměla, program končí.")
            sys.exit(1)
        
        polevka_specificka = BeautifulSoup(odp_serveru_specificky_web.text, "html.parser")
        tabulky_specificka_strany = polevka_specificka.select('div.t2_470 table.table')
        druha_tabulka = tabulky_specificka_strany[0]
        treti_tabulka = tabulky_specificka_strany[1]
        
        for tr in druha_tabulka.find_all("tr")[2:]:
            strana = tr.find_all("td")[2].get_text().strip()
            seznam_obci[nazev_obce].append(strana)
        
        for tr in treti_tabulka.find_all("tr")[2:]:
            strana = tr.find_all("td")[2].get_text().strip()
            seznam_obci[nazev_obce].append(strana)

def uloz_do_csv(seznam_obci, nazev_vystupniho_souboru):
    print("Vytvářím výstupní CSV soubor.")
    with open(nazev_vystupniho_souboru, 'w', newline='', encoding='utf-8-sig') as csvfile:
        csv_writer = csv.writer(csvfile)
        
        header = ['kód obce', 'název obce', 'voliči v seznamu', 'vydané obálky', 'platné hlasy', 
                  'Občanská demokratická strana', 'Řád národa - Vlastenecká unie', 'CESTA ODPOVĚDNÉ SPOLEČNOSTI', 
                  'Česká str.sociálně demokrat.', 'Radostné Česko', 'STAROSTOVÉ A NEZÁVISLÍ', 
                  'Komunistická str.Čech a Moravy', 'Strana zelených', 'ROZUMNÍ-stop migraci,diktát.EU', 
                  'Strana svobodných občanů', 'Blok proti islam.-Obran.domova', 'Občanská demokratická aliance', 
                  'Česká pirátská strana', 'Referendum o Evropské unii', 'TOP 09', 'ANO 2011', 'Dobrá volba 2016', 
                  'SPR-Republ.str.Čsl. M.Sládka', 'Křesť.demokr.unie-Čs.str.lid.', 'Česká strana národně sociální', 
                  'REALISTÉ', 'SPORTOVCI', 'Dělnic.str.sociální spravedl.', 'Svob.a př.dem.-T.Okamura (SPD)', 
                  'Strana Práv Občanů']
        csv_writer.writerow(header)
        
        for nazev_obce, hodnoty in seznam_obci.items():
            row = [hodnoty[0], nazev_obce] + hodnoty[1:]
            csv_writer.writerow(row)
    
    print(f"Výstupní CSV soubor byl vytvořen: {nazev_vystupniho_souboru}")

def main():
    if len(sys.argv) != 3:
        print("Chyba - zadal jsi nesprávný počet argumentů. Program končí.")
        sys.exit(1)

    zakladni_url = sys.argv[1]
    nazev_vystupniho_souboru = sys.argv[2]

    seznam_obci = stahni_zakladni_informace(zakladni_url)
    stahni_specifikace_obci(seznam_obci)
    stahni_politicke_strany(seznam_obci)
    uloz_do_csv(seznam_obci, nazev_vystupniho_souboru)

if __name__ == "__main__":
    main()








