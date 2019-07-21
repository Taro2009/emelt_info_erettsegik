'''
A kerites.txt a forrás, A telkek vannak benne a vásárlás sorrendjében. Minden sorban 3 db adat található.
Az első: megmondja, hogy a telek páros (0) vagy páratlan (1) oldalán van az utcának. A második: a telek szélessége méterben (8 és 20 közötti int)
3.: megmondja milyen színű a kerítés. Ha nincs befestve, akkor # karakter, ha még nincs kész a kerítés, akkor : karakter. Az utca hossza max 1000 m
Mindkét oldalon legalább 3-3 telek elkelt.

Feladataink:
1.: Beolvasni és eltárolni a forrást
2.: Írjuk ki, hogy hány telek kelt el (forrásfájl sorszáma)
3.: Írjuk ki, hogy
    a; a legutolsó telek melyik oldalon (páros páratlan) került eladásra,
    b; és mi a házszám amit kapott.
4.: Írjuk ki annak a teleknek a házszámát a páratlan oldalról, amely melletti telken ugyanolyan színű a kerítés.
5.: Kérjük be a felhasználótól egy eladott telek házszámát, majd azt felhasználva:
    a; Írja ki a házszámhoz tartozó kerítés színét, ha az már elkészült és befestették.
    b; A házszámhoz tartozó kerítést be vagy át szeretnénk festeni olyan szín kell, ami különbözik a szomszédoktól és az aktuális színtől. Ez lehet bármilyen A-Z karakter
6.: Jelenítsük meg az utcakep.txt fájlban a páratlan oldal utcaképét a mintának megfelelően úgy, hogy az 1. sorban a megfelelő kerítés szín vagy állapot jelenjen meg
annyiszor, ahány méter a kerítés, a 2. sorban pedig a telek 1. karaktere alá kerüljön a házszám.
'''

import random

################################################# 1. feladat #######################################################################
kerites_file = open('./e_inffor_18okt_fl/Forrasok/4_Kerites/kerites.txt', 'r') #megnyitjuk a forrast
hazak = [] #lista, amibe beolvasunk
for sor in kerites_file:
    hazak.append(sor.strip().split())
kerites_file.close()
# print(hazak) # csak teszteléshez

################################################# 2. feladat #######################################################################
print('2. feladat')
print('Az eladott telkek száma: ', len(hazak), '\n')

################################################# 3. feladat #######################################################################
# a; Először nézzük meg, páros vagy páratlan-e a legutolsó eladott telek!
legutolso = ''
if hazak[-1][0] == '0':
    legutolso = 'páros'
else:
    legutolsó = 'páratlan'
print('3. feladat')
print('A', legutolso, 'oldalon adták el az utolsó telket.')
# b; A házszámok meghatározásához menjünk végig a listán, és számoljuk össze hány db van páros és páratlan oldalon.
paros_szam = 0
paratlan_szam = 0
for elem in hazak:
    if elem[0] == '0':
        paros_szam += 1
    else:
        paratlan_szam += 1
# A házszám 0-ról indul, majd ahogy végigmegyünk a páros oldali házakon, mindig növelgetjük 2-vel.
utolso_hazszam = 0
utolso_hazszam_egyszerubben = 2*paros_szam
for i in range(0, paros_szam):
    utolso_hazszam += 2

# print('Az utolsó telek házszáma:', utolso_hazszam, 'és ez egyszerűbben kiszámolva:', utolso_hazszam_egyszerubben) # itt ugye látszik,
                                                                                                                    # hogy kis gondolkodással a 2. for ciklus felesleges,
                                                                                                                    # mert elég 2-vel megszorozni a sorszámot, hogy megkapjuk a
                                                                                                                    # házszámot. Benthagyjuk mindkettőt, hogy lássunk
                                                                                                                    # 2 megoldást is
print('Az utolsó telek házszáma:', utolso_hazszam, '\n')

################################################# 4. feladat #######################################################################
# Válogassuk szét a házak töbünket páros és páratlan oldal szerint, ezt előbb is meg lehet tenni, de itt is tökéletes. Azért tesszük ezt meg külön for ciklusban és nem
# az előzőben, ami lényegében ugyanez, hogy ne végezzünk egyszerre több dolgot a jobb átláthatóság érdekében. Természetesen a kód sokkal kompaktabb is lehetne, de egyben
# kevésbé érthető. Mi most érthetőségre törekszünk.
ptlan_hazak = []
paros_hazak = []

for elem in hazak:
    if elem[0] == '0':
        paros_hazak.append(elem)
    else:
        ptlan_hazak.append(elem)

# print(paros_hazak)  # Csak teszteléshez
# print(ptlan_hazak)  # Csak teszteléshez

aktualis_szin = ''
megvan = 0
i = 0
# házszám páratlan oldalon: (1 + sorszám*2)
while not megvan:
    aktualis_szin = ptlan_hazak[i][2]
    if aktualis_szin == ptlan_hazak[i+1][2] and aktualis_szin != ':' and aktualis_szin != '#' : # Ne felejtsük el, hogy a : és #nem lesz jó!
        megvan = 1
    else:
        i += 1
print('4. feladat')
print('A szomszédossal egyezik a kerítés színe:', (1+i*2), '\n')

################################################# 5. feladat #######################################################################

print('5. feladat')
megadott_hazszam = int(input('Adjon meg egy házszámot! '))
allapot = ''
allapot_elotte = '' # ez a b-hez
allapot_utana = ''  # ez is a b-hez
if megadott_hazszam % 2:
    allapot = ptlan_hazak[int((megadott_hazszam-1)/2)][2]
    if ((megadott_hazszam-1)/2)-1 >= 0:                      # ez figyel, nehogy alul- vagy túlindexeljünk
        allapot_elotte = ptlan_hazak[int(((megadott_hazszam-1)/2)-1)][2]
    else:
        allapot_elotte = allapot
    if ((megadott_hazszam-1)/2)+1 < len(ptlan_hazak):
        allapot_utana = ptlan_hazak[int(((megadott_hazszam-1)/2)+1)][2]
    else:
        allapot_utana = allapot
else:
    allapot = paros_hazak[int((megadott_hazszam)/2-1)][2]
    if ((megadott_hazszam)/2-1)-1 >= 0:
        allapot_elotte = paros_hazak[int(((megadott_hazszam)/2-1)-1)][2]
    else:
        allapot_elotte = allapot
    if megadott_hazszam/2 < len(paros_hazak):
        allapot_utana = ptlan_hazak[int(((megadott_hazszam)/2))][2]
    else:
        allapot_utana = allapot
print('A kerítés színe / állapota:', allapot)

angol_abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
randomsorszam = random.randint(0, 25)
szin_otlet = angol_abc[randomsorszam]
while szin_otlet == allapot or szin_otlet == allapot_elotte or szin_otlet == allapot_utana:
    randomsorszam = (randomsorszam + 1) % 26
    szin_otlet = angol_abc[randomsorszam]       # %26 azért kell, nehogy túlindexeljük a tömböt. Az algoritmus lényegében vesz egy random karaktert az angol abc-böl,
                                                # és ha az a karakter egyezik az adott ház színével vagy bármely szomszédéval, akkor veszi az abc következő karakterét.
                                                # ez által legrosszabb esetben 3 iteráció után biztosan jó színt talál
print('Egy lehetséges festési szín:', szin_otlet)

################################################# 6. feladat #######################################################################

kimenet_file = open('utcakep.txt', 'w')
haz_kerites = ''
masodiksor = ''
pt_haz_sorszam = 0
# print(ptlan_hazak)
for elem in ptlan_hazak:
    for i in range(0, int(elem[1])):
        if i == 0:
            masodiksor += str(pt_haz_sorszam*2 + 1)
        else:
            masodiksor += ' '
        haz_kerites += elem[2]
    print(haz_kerites, end='', file=kimenet_file)
    haz_kerites = ''
    pt_haz_sorszam += 1

print('', file=kimenet_file)
print(masodiksor, file=kimenet_file)

kimenet_file.close()


