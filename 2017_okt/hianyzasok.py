# Nehézség (könnyebb / nehezebb): KONNYEBB
def hetnapja(honap, nap):
    honap = int(honap)
    nap = int(nap)
    napnev = ["vasarnap", "hetfo", "kedd", "szerda", "csutortok", "pentek", "szombat"]
    napszam = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 335]
    napsorszam = (napszam[honap-1] + nap) % 7
    hetnapja = napnev[napsorszam]
    return hetnapja


################################################# 1. feladat #######################################################################
befile = open('./e_inffor_17okt_fl/Forrasok/4_Hianyzasok/naplo.txt')
belista = []
for sor in befile:
    belista.append(sor.strip().split())

# print(belista) # lista kiiratása csak teszteléshez

befile.close

################################################# 2. feladat #######################################################################
hianyzas_rogzites_szam = 0

for elem in belista:
    if elem[0] != '#':
        hianyzas_rogzites_szam += 1

print('2. feladat')
print('A naplóban', hianyzas_rogzites_szam, 'bejegyzés van.')

################################################# 3. feladat #######################################################################
# X igazolt, I igazolatlan
igazoltak = 0
igazolatlanok = 0

for elem in belista:
    if elem[0] != '#':
        igazoltak += elem[2].count('X')
        igazolatlanok += elem[2].count('I')
                
print('3. feladat')
print('Az igazolt hiányzások száma', igazoltak, ', az igazolatlanoké', igazolatlanok, 'óra.')

################################################# 4. feladat #######################################################################

################################################# 5. feladat #######################################################################
behonap = input('A hónap sorszáma=')
benap = input('A nap sorszáma=')
print('Azon a napon', hetnapja(behonap, benap), 'volt.')

################################################# 6. feladat #######################################################################
print('6. feladat')
be_napnev = input('A nap neve=')
be_ora = input('Az óra sorszáma=')
    
eves_hianyzas = 0
j = 1


for i in range(0, len(belista)):
    if belista[i][0] == '#':
        if hetnapja(belista[i][1], belista[i][2]) == be_napnev:
            while belista[i+j][0] != '#':
                if belista[i+j][2][int(be_ora)-1] == 'I' or belista[i+j][2][int(be_ora)-1] == 'X': 
                    eves_hianyzas += 1
                j += 1
            j = 1
            
print('Ekkor összesen', eves_hianyzas, 'óra hiányzás történt.')

################################################# 7. feladat #######################################################################

# 2 listát csinálunk, az egyikben a nevek a másikban azonos indexen a hiányzások.
# A 2. listában kell egy maximumkeresés, majd átfutunk rajta még1x, és ha
# a maxszal egyenlő elemet találunk kivesszük hozzá a nevet és beleappendeljük
# egy új maxhianyzas listába


nevek = []
hianyzasok_nevszerint = []
nevlista = []
index = 0
napihianyzasszam = 0
for sor in belista:
    if sor[0] != '#':
        
        nevlista.append(sor[0]) # csinálunk egy ideiglenes listát amibe beletesszük a vezeték és keresztnevet, majd ezt joinolva tesszük a végleges név listába
        nevlista.append(sor[1])
        if ' '.join(nevlista) in nevek:
            index = nevek.index(' '.join(nevlista))    # ha már benne van a név a listában akkor megkeressük az indexét és növeljük a neki megfelelő indexű hiányzásszámlálót
            for i in range(0, 7):
                if sor[2][i] == 'I' or sor[2][i] == 'X':
                    napihianyzasszam += 1
            hianyzasok_nevszerint[index] += napihianyzasszam
        else:
            nevek.append(' '.join(nevlista))
            for i in range(0, 7):
                if sor[2][i] == 'I' or sor[2][i] == 'X':
                    napihianyzasszam += 1
            hianyzasok_nevszerint.append(napihianyzasszam)
        napihianyzasszam = 0  
        nevlista = []
# print(nevek) #csak teszthez
# print(hianyzasok_nevszerint) # csak teszthez

max_hiany = max(hianyzasok_nevszerint)
max_hiany_nev = []

for i in range(0, (len(hianyzasok_nevszerint))):
    if hianyzasok_nevszerint[i] == max_hiany:
        max_hiany_nev.append(nevek[i])

print('7. feladat')
print('A legtöbbet hiányzó tanulók: ', end='')
for elem in max_hiany_nev:
    print(elem, end=' ')


