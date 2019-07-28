# Nehézség (könnyebb / nehezebb): NEHEZEBB
'''
Színház társalgója, 9 és 15 óra közötti időszak.
ajto.txt-ben 4 adat található, első 2 az ajtón való áthaladás időpontja óra és
perc értékkel, a 3. az áthaladó személy azonosítója, és a 4. az hogy be vagy ki
ment.
A sorok száma max 1000, és a személy azonosítója 1 és 100 közötti. 
Biztosan tudjuk, hogy 9-kor, a megfigyelés kezdetekor a társalgó ÜRES volt.
15 órakor, azaz a megfigyelés végén még lehettek bent emberek. A be és
kilépések időrendben vannak rögzítve, lehet hogy van 2 azonos időpont, ekkor a
felső az előbbi, még ha az az időpontból nem is látható.

A képernyőre írás előtt írjuk ki mindig a feladat sorszámát!

1.: Olvassuk be és tároljuk el a filet!
2.: Írjuk ki annak az azonosítóját, aki először lépett be, és annak,
aki utoljára távozott a megfigyelési időszakban
3.: Határozzuk meg, ki hányszor haladt át a társalgó ajtaján!
A meghatározott értékeket azonosító szerint írjuk ki növekvő sorrendben az
athaladas.txt fájlba.
Soronként egy személy azonosítója, és tőle szóközzel elválasztva az áthaladások
száma szerepeljen.

'''

def keres(athal, azon):
    i = 0
    for element in athal:
        if element[0] == azon:
            return int(i)
        else:
            i += 1
    return -1

def keresidopont(lista, elem1, elem2):
    for elem in lista:
        if int(elem[0]) == int(elem1) and int(elem[1]) == int(elem2):
            return -1
    return 1

def idopontok_kulonbsege(be_ido_ora, be_ido_perc, ki_ido_ora, ki_ido_perc):
    percvissza = 0
    be_ido_ora = int(be_ido_ora)
    be_ido_perc = int(be_ido_perc)
    ki_ido_ora = int(ki_ido_ora)
    ki_ido_perc = int(ki_ido_perc)       

    percvissza = (ki_ido_ora*60 + ki_ido_perc) - (be_ido_ora*60 + be_ido_perc)
    
    return percvissza
    
################################################# 1. feladat #######################################################################
bemenet = open('./e_inffor_18maj_fl/Forrasok/4_Tarsalgo/ajto.txt')
belista = []
for sor in bemenet:
    belista.append(sor.strip().split())

bemenet.close()
# print(belista) # Teszteléshez kiíratás

################################################# 2. feladat #######################################################################
print('2. feladat')
print('Az első belépő:', belista[0][2])
utolso = ''
for elem in belista:
    if elem[3] == 'ki':
        utolso = elem[2]
print('Az utolsó kilépő:', utolso)

################################################# 3. feladat #######################################################################
# érdemes úgy tárolni, hogy egy nagy listában mindent, és abban 2 elemű kis
# listák vannak azonosító - áthaladásszám párral. Emiatt kéne egy függvény, ami
# átveszi a nagy listát, és megnézi, hogy hol van benne a megfelelő fájl sorban
# lévő ember azonosítója, ha nincs benne, akkor visszatér -1-el és appendeljük a
# listát 1-es áthaladásszámmal, ha benne van, akkor simán visszatér az indexszel,
# és csak növeljük az adott indexen lévő azonosítójú ember áthaladásainak számát.
athaladasok = []
index = 0
kislista = [0, 0]

for elem in belista:
    index = keres(athaladasok, elem[2])
    if index == -1:
        kislista[0] = elem[2]
        kislista[1] = 1
        athaladasok.append([elem[2], 1])
    else:
        athaladasok[index][1] += 1


# Azonosító szerint úgy irjuk majd ki növekvőbe, hogy megy majd egy ciklus
# 1-100-ig, és nézi mindig, hogy van-e a listában olyan azonosítójú ember.
# Ha van, akkor kimegy az azonosító és az áthaladások száma
athaladas_ki_file = open('athaladas.txt', 'w')
for i in range(1, 100):
    for elem in athaladasok:
        if i == int(elem[0]):
            print(elem[0], elem[1], file=athaladas_ki_file)

athaladas_ki_file.close()
# Hibás tipuskonverziók rengeteg fejfájáshoz vezethetnek! Mindig gondoljuk
# végig, hogy is és while ciklus feltételében milyen tipust hasonlítunk
# milyennel!!!!!

################################################# 4. feladat #######################################################################
print('4. feladat')
craftoltstring = 'A végén a társalgóban voltak: '
for elem in athaladasok:
    if elem[1] % 2 == 1:
        craftoltstring += elem[0]
        craftoltstring += ' '

print(craftoltstring)
# ugye a feladat mintában növekvő sorban vannak, viszont a feladatban nem,
# tehát elvileg ennek is jónak kell lennie. Kihasználjuk, hogy azok maradnak a
# társalgóban, akik páratlan számszor haladtak át az ajtón, így felhasználjuk az
# előző feladat áthaladásait.

################################################# 5. feladat #######################################################################
print('5. feladat')
# kéne készíteni egy listát, amiben benne van, hogy
# időpont - hányan vannak, majd erre egy maximumkeresést
i = 0
idopontok = []
for elem in belista:
    if keresidopont(idopontok, elem[0], elem[1])==1:
        idopontok.append([elem[0], elem[1]])
# Ezzel kiválogatjuk az időpontokat úgy, hogy ne legyenek duplák

# megnézni minden bejegyzésről, hogy: van-e belőle több, és ha igen, akkor azt
# tesszük bele a bentlévők listába, amelyik több.

#lépések: megnézni, hogy egy adott időpont egyezik-e az előzővel, ha igen,
# akkor módosítjuk a legutolsó lista beli elemet, ha nem, akkor
# új listabeli elemet hozunk létre.
bentlevok_egy_idopontban = []
j = 0
buffer = 0
for i in range(0, len(belista)-1):
    if i>0:
        if belista[i][0] == belista[i-1][0] and belista[i][1] == belista[i-1][1]:
            if belista[i][3] == 'be':
                bentlevok_egy_idopontban[j] += 1
            else:
                # bentlevok_egy_idopontban[j] -= 1 # mivel a bentlévők maximumára vagyunk kíváncsiak, ezért
                # itt nem csökkentünk
                buffer += 1 # azért meg kell jegyezni hányan mennek ki, hogy új időpontban levonjuk
        else:
            if belista[i][3] == 'be':
                bentlevok_egy_idopontban.append(bentlevok_egy_idopontban[j]+1-buffer)
                buffer = 0
            else:
                bentlevok_egy_idopontban.append(bentlevok_egy_idopontban[j]-1-buffer)
                buffer = 0
            j += 1
    else:
        bentlevok_egy_idopontban.append(1)
'''
for i in range(0, len(idopontok)-1):
    print(idopontok[i], bentlevok_egy_idopontban[i])
'''
index = 0
bentmax = 0
for i in range(0, len(bentlevok_egy_idopontban)-1):
    if bentlevok_egy_idopontban[i] > bentmax:
        bentmax = bentlevok_egy_idopontban[i]
        index = i
    
print(idopontok[index][0], idopontok[index][1], '-kor voltak legtöbben a társalgóban.')

################################################# 6. feladat #######################################################################
bekert_azon = input('6. feladat\nAdja meg a személy azonosítóját! ')

################################################# 7. feladat #######################################################################
# simán csak kiiratjuk az azonosítóhoz tartozó időpontokat, ha bement a személy akkor máshogy mint hogyha ki
for elem in belista:
    if elem[2] == bekert_azon:
        if elem[3] == 'be':
            print(elem[0], ':', elem[1], '- ', end='')
        else:
            print(elem[0], ':', elem[1])
    
################################################# 8. feladat #######################################################################
# kell írni egy függvényt, ami 2 beadott időpontból kiszámolja a köztük lévő perc különbséget. Emellett meg
# kell nézni, hogy a végén van-e kimenetel, ha nincs, akkor bent maradt.

# meg kellene nézni, hogy bent maradt-e a társalgóban, mert akkor 15:00 és a legutolsó belépési
# idő közti különbséget kell venni. A 8. feladat első része hibás.

be_ido_ora = 0
be_ido_perc = 0
ki_ido_ora = 0
ki_ido_perc = 0
perckul = 0
for elem in belista:
    if elem[2] == bekert_azon:
        if elem[3] == 'be':
            be_ido_ora = int(elem[0])
            be_ido_perc = int(elem[1])
        else:
            ki_ido_ora = int(elem[0])
            ki_ido_ora = int(elem[1])
            perckul += idopontok_kulonbsege(be_ido_ora, be_ido_perc, ki_ido_ora, ki_ido_perc)
            be_ido_ora = 0
            be_ido_perc = 0

tarsalgo_allapot = ''
if be_ido_ora != 0:
    tarsalgo_allapot = 'a társalgóban volt.'
else:
    tarsalgo_allapot = 'nem volt a társalgóban.'
    
print('8. feladat')
print('A(z)', bekert_azon, 'személy összesen', perckul, 'percet volt bent, a megfigyelés végén', tarsalgo_allapot)





