Tøetí projekt ENGETO kurz Python


Základní popis programu
Program stahuje data z voleb 2017 v okrese Prostìjov. Po drobné úpravì mùe stahovat data i z jinıch okresù. Program prozatím neumí stahovat data z mìst, která byla pøi volbách rozdìlená do okrskù.  

Instalace externích knihoven
1. Vytvoøte si nové virtuální prostøedí
2. Instalaci knihoven udìlejte s pomocí souboru ‘requirements.txt‘: pip install –r requirements.txt

Spuštìní programu
1. Pøemístìte se do pøíkazového øádku nebo terminálu
2. Zadejte pøíkaz ke spuštìní programu: python volby.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103" vysledky_prostejov.csv

První poznámka ke spuštìní programu – pøíkaz ke spuštìní programu
Pøíkaz ke spuštìní programu obsahuje následující souèásti: python nazev_programu argument1 argument2
Poznámka: argumentem1 je URL základní webové stránky pro okres Prostìjov
Poznámka: argumentem2 je název vıstupního souboru vèetnì pøílohy
Poznámka: musíte napsat mezeru mezi: python, nazev_programu, argument1 a argument2

Druhá poznámka ke spuštìní programu – cesta k virtuálnímu prostøedí
V programu je na øádku 24 nastavená cesta k virtuálnímu prostøedí. Opravte si ji podle svého

Tøetí poznámka ke spuštìní programu – vyuití pro jinı okres
Pokud budete chtít program vyuít pro jinı okres ne je okres Prostìjov, musíte udìlat dvì zmìny:
1. Musíte zmìnit 4 èíslice vyjadøující okres v URL adrese: V URL adrese, kterou zadáváte v pøíkazovém øádku jako první argument, musíte zmìnit poslední ètyøi èíslice. Tyto èíslice jsou pro okres Prostìjov: 7103 a napøíklad pro okres Olomouc: 7102
2. Musíte zmìnit ty stejné èíslice v URL adrese v programu na øádcích 64 a 86. Tyto èíslice jsou pro okres Prostìjov: 7103 a napøíklad pro okres Olomouc: 7102 

Ukázka programu – spuštìní programu pro okres Prostìjov
Název programu: volby.py
1. Argument: "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103"
2. Argument: vysledky_prostejov.csv
Celı pøíkaz ke spuštìní programu: python volby.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103" vysledky_prostejov.csv

Ukázka programu - prùbìh stahování
Program importuje knihovny.
Program stahuje názvy obcí a jejich èíselné kódy.
Program stahuje poèty volièù, obálek a platné hlasy.
Program stahuje politické strany.
Program vytváøí vıstupní CSV soubor.
Vıstupní CSV soubor byl vytvoøen: vysledky_prostejov.csv

Ukázka programu – èásteènı vıstup
kód obce,název obce,volièi v seznamu,vydané obálky,platné hlasy,Obèanská demokratická strana,Øád národa - Vlastenecká unie,CESTA ODPOVÌDNÉ SPOLEÈNOSTI,Èeská str.sociálnì demokrat.,Radostné Èesko,STAROSTOVÉ A NEZÁVISLÍ,Komunistická str.Èech a Moravy,Strana zelenıch,"ROZUMNÍ-stop migraci,diktát.EU",Strana svobodnıch obèanù,Blok proti islam.-Obran.domova,Obèanská demokratická aliance,Èeská pirátská strana,Referendum o Evropské unii,TOP 09,ANO 2011,Dobrá volba 2016,SPR-Republ.str.Èsl. M.Sládka,Køes.demokr.unie-Ès.str.lid.,Èeská strana národnì sociální,REALISTÉ,SPORTOVCI,Dìlnic.str.sociální spravedl.,Svob.a pø.dem.-T.Okamura (SPD),Strana Práv Obèanù

