T�et� projekt ENGETO kurz Python


Z�kladn� popis programu
Program stahuje data z�voleb 2017 v�okrese Prost�jov. Po drobn� �prav� m��e stahovat data i z�jin�ch okres�. Program prozat�m neum� stahovat data z�m�st, kter� byla p�i volb�ch rozd�len� do okrsk�.  

Instalace extern�ch knihoven
1. Vytvo�te si nov� virtu�ln� prost�ed�
2. Instalaci knihoven ud�lejte s�pomoc� souboru �requirements.txt�: pip install �r requirements.txt

Spu�t�n� programu
1. P�em�st�te se do p��kazov�ho ��dku nebo termin�lu
2. Zadejte p��kaz ke spu�t�n� programu: python volby.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103" vysledky_prostejov.csv

Prvn� pozn�mka ke spu�t�n� programu � p��kaz ke spu�t�n� programu
P��kaz ke spu�t�n� programu obsahuje n�sleduj�c� sou��sti: python nazev_programu argument1 argument2
Pozn�mka: argumentem1 je URL z�kladn� webov� str�nky pro okres Prost�jov
Pozn�mka: argumentem2 je n�zev v�stupn�ho souboru v�etn� p��lohy
Pozn�mka: mus�te napsat mezeru mezi: python, nazev_programu, argument1 a argument2

Druh� pozn�mka ke spu�t�n� programu � cesta k�virtu�ln�mu prost�ed�
V�programu je na ��dku 24 nastaven� cesta k�virtu�ln�mu prost�ed�. Opravte si ji podle sv�ho

T�et� pozn�mka ke spu�t�n� programu � vyu�it� pro jin� okres
Pokud budete cht�t program vyu��t pro jin� okres ne� je okres Prost�jov, mus�te ud�lat dv� zm�ny:
1. Mus�te zm�nit 4 ��slice vyjad�uj�c� okres v�URL adrese: V�URL adrese, kterou zad�v�te v�p��kazov�m ��dku jako prvn� argument, mus�te zm�nit posledn� �ty�i ��slice. Tyto ��slice jsou pro okres Prost�jov: 7103 a nap��klad pro okres Olomouc: 7102
2. Mus�te zm�nit ty stejn� ��slice v URL adrese v�programu na ��dc�ch 64 a 86. Tyto ��slice jsou pro okres Prost�jov: 7103 a nap��klad pro okres Olomouc: 7102 

Uk�zka programu � spu�t�n� programu pro okres Prost�jov
N�zev programu: volby.py
1. Argument: "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103"
2. Argument: vysledky_prostejov.csv
Cel� p��kaz ke spu�t�n� programu: python volby.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103" vysledky_prostejov.csv

Uk�zka programu - pr�b�h stahov�n�
Program importuje knihovny.
Program stahuje n�zvy obc� a jejich ��seln� k�dy.
Program stahuje po�ty voli��, ob�lek a platn� hlasy.
Program stahuje politick� strany.
Program vytv��� v�stupn� CSV soubor.
V�stupn� CSV soubor byl vytvo�en: vysledky_prostejov.csv

Uk�zka programu � ��ste�n� v�stup
k�d obce,n�zev obce,voli�i v seznamu,vydan� ob�lky,platn� hlasy,Ob�ansk� demokratick� strana,��d n�roda - Vlasteneck� unie,CESTA ODPOV�DN� SPOLE�NOSTI,�esk� str.soci�ln� demokrat.,Radostn� �esko,STAROSTOV� A NEZ�VISL�,Komunistick� str.�ech a Moravy,Strana zelen�ch,"ROZUMN�-stop migraci,dikt�t.EU",Strana svobodn�ch ob�an�,Blok proti islam.-Obran.domova,Ob�ansk� demokratick� aliance,�esk� pir�tsk� strana,Referendum o Evropsk� unii,TOP 09,ANO 2011,Dobr� volba 2016,SPR-Republ.str.�sl. M.Sl�dka,K�es�.demokr.unie-�s.str.lid.,�esk� strana n�rodn� soci�ln�,REALIST�,SPORTOVCI,D�lnic.str.soci�ln� spravedl.,Svob.a p�.dem.-T.Okamura (SPD),Strana Pr�v Ob�an�

