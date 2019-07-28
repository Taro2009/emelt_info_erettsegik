# Nehézség (könnyebb / nehezebb): NEHEZEBB
################################################# 1. feladat #######################################################################
def mpbe(ora, perc, masodperc):
    return (int(masodperc) + 60*int(perc) + 3600*int(ora))

################################################# 2. feladat #######################################################################
befile = open('./e_inffor_16okt_fl/Forrasok/4_Telefonos_ugyfelszolgalat/hivas.txt')
belista = []
for sor in befile:
    sorclean = sor.strip().split()
    #belista.append([[sorclean[0], sorclean[1], sorclean[2]],[sorclean[3], sorclean[4], sorclean[5]]])
    belista.append(sorclean)
#print(belista) # csak teszteléshez    
befile.close()

################################################# 3. feladat #######################################################################
print('3. feladat')
orakra_bontva = []
darab_oraban = []
for elem in belista:
    if not elem[0] in orakra_bontva:
        orakra_bontva.append(elem[0])
        darab_oraban.append(1)
    else:
        darab_oraban[orakra_bontva.index(elem[0])] += 1

for i in range(0, len(orakra_bontva)):
    print(orakra_bontva[i],'ora',darab_oraban[i],'hivas')

################################################# 4. feladat #######################################################################
maxhivas = 0
sorszam = 0
for i in range(0, len(belista)):
    if mpbe(belista[i][3], belista[i][4], belista[i][5])-mpbe(belista[i][0], belista[i][1], belista[i][2]) > maxhivas:
        maxhivas = mpbe(belista[i][3], belista[i][4], belista[i][5])-mpbe(belista[i][0], belista[i][1], belista[i][2])
        sorszam = i
    i += 1
sorszam += 1
print('')
print('4. feladat')
print('A leghosszabb ideig vonalban levo hivo', sorszam, 'sorban szerepel, a hivas hossza:', maxhivas, 'masodperc.')
print('')

################################################# 5. feladat #######################################################################

print('5. feladat')
beido = input('Adjon meg egy idopontot! (ora perc masodperc) ')
#kell várakozók száma, beszélő sorszáma hogyha épp van, 'Nem volt beszélő', hogyha nincs

beido = beido.strip().split()
varakozok = 0
sorszam = 0
elso = True
vanbeszelo = False
for i in range(0, len(belista)):
    if mpbe(belista[i][3], belista[i][4], belista[i][5]) >= mpbe(beido[0], beido[1], beido[2]) >= mpbe(belista[i][0], belista[i][1], belista[i][2]):
        if elso:
            sorszam = i+1
            elso = False
        varakozok += 1
    i += 1

    
if varakozok > 1:
    print('A varakozok szama:', varakozok-1, 'a beszelo a', sorszam, 'hivo.')
elif varakozok == 1:
    print('A varakozok szama: 0 a beszelo a', sorszam, 'hivo.')
else:
    print('Nem volt beszélő')

################################################# 6. feladat #######################################################################
# 1.: megkeresni azt a személyt, aki legközelebb kezdte a hívását 12:00:00-hoz visszafele nézve. Ettől visszafelé lépkedve
# megkeresni azt, aki a legkésőbb fejezte be. Ez lesz az a személy, aki utoljára beszélt.
# ha ez a személy megvan, akkor
# megnézünk minden nála előbb megkezdett hívást, aminek a vége az ő megkezdése utáni, és ezekből vesszük a legnagyobb végűt,
# ebből kivonjuk a vizsgált személy megkezdését és megvan

min_tavolsag = mpbe(12, 0, 0) - mpbe(belista[0][0], belista[0][1], belista[0][2])
for i in range(0, len(belista)):
    akt_kul = mpbe(12, 0, 0) - mpbe(belista[i][0], belista[i][1], belista[i][2])
    if akt_kul > 0 and akt_kul < min_tavolsag:
        min_tavolsag = akt_kul
        sorszam = i + 1

maxbefejez = mpbe(belista[sorszam-1][3], belista[sorszam-1][4], belista[sorszam-1][5])
for i in range(sorszam-1, 0, -1):
    if mpbe(belista[i][3], belista[i][4], belista[i][5]) > maxbefejez:
        maxbefejez = mpbe(belista[i][3], belista[i][4], belista[i][5])
        sorszam = i+1

# most nézzük meg, mennyit kellett várnia a megtalált személynek aki utoljára telefonált!
vege_max = mpbe(belista[0][3], belista[0][4], belista[0][5])
sorszam_2 = 0
for i in range(0, len(belista)):
    if mpbe(belista[sorszam-1][0], belista[sorszam-1][1], belista[sorszam-1][2]) - mpbe(belista[i][0], belista[i][1], belista[i][2]) > 0 and mpbe(belista[i][3], belista[i][4], belista[i][5]) > mpbe(belista[sorszam-1][0], belista[sorszam-1][1], belista[sorszam-1][2]):
        if mpbe(belista[i][3], belista[i][4], belista[i][5]) > vege_max:
            vege_max = mpbe(belista[i][3], belista[i][4], belista[i][5])
            sorszam_2 = i + 1
print('')
print('6. feladat')
if vege_max < mpbe(belista[sorszam-1][0], belista[sorszam-1][1], belista[sorszam-1][2]):
    print('Az utolso telefonalo adatai a(z)', sorszam, '. sorban vannak, 0 masodpercig vart.')
else:
    print('Az utolso telefonalo adatai a(z)', sorszam, '. sorban vannak,', (vege_max - mpbe(belista[sorszam-1][0], belista[sorszam-1][1], belista[sorszam-1][2])), 'masodpercig vart.')

################################################# 7. feladat #######################################################################
# először megnézzük, van-e olyan hívó aki a nyitás előtt hívott, de a nyitás utánig várt. Ha van, akkor ezekből a
# legkorábban kezdettet kell kezdő hívónak választani.
# ha nincs ilyen, akkor a nyitás utáni első hívó az első hívó
# ha megvan az első hívó, megnézzük, hogy van-e olyan, aki a befejezése utánig tartotta a telefont, és ha van, akkor
# ezekből vesszük a legkorábban kezdő hívót, ha nincs, akkor vesszük a befejezése utáni legkorábbi hívót.
# ezt ismételjük.

# kell egy fv. ami bevesz egy bármilyen időpontot, és visszaadja az az előtti legkorábbi olyan hívót aki az
# időpont utánig tartotta a telefont. Ha nincs ilyen visszaad csupa 0-t vagy 0-t

# kell egy függvény ami visszaad egy adott időpont utáni legkorábbi hívót, ezt csak akkor hívjuk meg, ha az előző fv nem
# ad vissza.

# az egész egy while(amig a végére nem érünk) ciklusba lesz téve.
# meg is van minden ami a sikeres futáshoz kell
