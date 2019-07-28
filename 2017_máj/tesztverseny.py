# Nehézség (könnyebb / nehezebb): KONNYEBB
# tesztverseny

befile = open('./e_inffor_17maj_fl/Forrasok/4_Tesztverseny/valaszok.txt')
belista = []
for sor in befile:
    if len(sor) == 15:
        megoldas = sor.strip()
    else:
        belista.append(sor.strip().split())

# print(megoldas, '\n', belista) # csak teszteléshez
befile.close()

################################################# 1. feladat #######################################################################
print('1. feladat: Az adatok beolvasása\n')

################################################# 2. feladat #######################################################################
print('2. feladat: A vetélkedőn', len(belista), 'versenyző indult.\n')

################################################# 3. feladat #######################################################################
beversenyzo = input('3. feladat: A versenyző azonosítója = ')
for elem in belista:
    if elem[0] == beversenyzo:
        versenyzo_valasza = elem[1]
        print(elem[1], '(a versenyző válasza)\n')

################################################# 4. feladat #######################################################################

print('4. feladat')
print(megoldas, '(a helyes megoldás)')

for i in range(0, len(megoldas)):
    if megoldas[i] == versenyzo_valasza[i]:
        print('+', end='')
    else:
        print(' ', end='')
print('(a versenyző helyes válaszai)\n')

################################################# 5. feladat #######################################################################
feladat_sorszam = input('5. feladat: A feladat sorszáma = ')
feladat_sorszam = int(feladat_sorszam)
jovalaszok = 0
for elem in belista:
    if elem[1][feladat_sorszam-1] == megoldas[feladat_sorszam-1]:
        jovalaszok += 1

print('A feladatra', jovalaszok, 'fő, a versenyzők', round(jovalaszok/303*100, 2), '%-a adott helyes választ.\n')

################################################# 6. feladat #######################################################################
# 1-5. feladat: 3 pont; 6-10. feladat: 4 pont;
# 11-13. feladat: 5 pont; 14. feladat: 6 pont
# pontok.txt-be a versenyzők pontszáma úgy hogy: [versenyző kód] [összpontszám]

kifile = open('pontok.txt', 'w')

print('6. feladat: A versenyzők pontszámának meghatározása\n')
osszpontok_lista = []
j = 0
for elem in belista:
    osszpontok_lista.append(0)
    for i in range(0, 14):
        if megoldas[i] == elem[1][i]:
            if 0 <= i <= 4:
                osszpontok_lista[j] += 3
            elif 5 <= i <= 9:
                osszpontok_lista[j] += 4
            elif 10 <= i <= 12:
                osszpontok_lista[j] += 5
            elif i == 13:
                osszpontok_lista[j] += 6
    j += 1
for i in range(0, len(belista)):
    print(belista[i][0], osszpontok_lista[i], file=kifile)
kifile.close()

################################################# 7. feladat #######################################################################
# első 3 max pontot elérő embereket kell kiírni, ha vannak azonos pontszámok,
# akkor azt mind.

pontszam_csokkenobe = []
pontszam_azonositoval = []
for i in range(0, len(osszpontok_lista)):
    pontszam_azonositoval.append([belista[i][0], osszpontok_lista[i]])

osszpontok_lista.sort(reverse=True)
elsok = []
masodikak = []
harmadikak = []

# elso harom legnagyobb pontszam kinyerese
haromlegnagyobb = []
szamlalo = 0
for elem in osszpontok_lista:   # megnézi mi a 3 legnagyobb pontszám, kiveszi az ismétlődéseket
    if szamlalo < 3 and not elem in haromlegnagyobb:
        haromlegnagyobb.append(elem)
        szamlalo += 1

for elem in pontszam_azonositoval:
    if elem[1] == haromlegnagyobb[0]:
        elsok.append(elem[0])
    elif elem[1] == haromlegnagyobb[1]:
        masodikak.append(elem[0])
    elif elem[1] == haromlegnagyobb[2]:
        harmadikak.append(elem[0])
print('7. feladat: A verseny legjobbjai:')
for elem in elsok:
    print('1. díj (' + str(osszpontok_lista[0]) + ' pont): ' + elem)
for elem in masodikak:
    print('2. díj (' + str(osszpontok_lista[1]) + ' pont): ' + elem)
for elem in harmadikak:
    print('3. díj (' + str(osszpontok_lista[2]) + ' pont): ' + elem)
            

