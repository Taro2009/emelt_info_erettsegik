
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

