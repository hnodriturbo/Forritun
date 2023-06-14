#Hreiðar Pétursson
#Æfing dict föll
# 17.2.2023

import random


on = True

while on == True:
    print("1. Danspörin")
    print("2. Símaskrá")
    print("3. Skráning í bekk")
    print("4. Hætta")
    val = int(input("Veldu nú"))
    if val == 1:
        #Fyrsti liður - Danspörin
        dansspor = True
        while dansspor == True:
            print("1. Sitthvort tuple")
            print("2. Para fyrsta saman")
            print("3. Para random par")
            print("4. Para öll pörin random")
            print("5. Finna staf")
            print("6. Finna fyrsta staf")
            print("7. Fleiri en eitt n")
            print("8. Hætta")
            val = int(input("Veldu nú"))
            tup1 = ("Hreiðar", "Gunnar", "Jónas", "Andri", "Pétur", "Anton")
            tup2 = ("Jóna", "Gunna", "Hnoðrína", "Diljá", "Eva", "Erna")
            if val == 1:
                #Liður 1 - 1 Prenta út tuple listana
                def prentatTuple(tup1, tup2):
                    print("Herranöfnin eru:", *tup1)
                    print("Dömunöfnin eru:", *tup2)
                print(prentatTuple(tup1, tup2))
            elif val == 2:
                #Liður 1 - 2 Para fyrstu gildin saman
                def pararod(tup1, tup2):
                    for x in range(len(tup1)):
                        print(tup1[x], "og", tup2[x])
                print(pararod(tup1, tup2))
            elif val == 3:
                #Liður 1 - 3 Para saman random par
                def pararandom(tup1, tup2):
                    herra = random.choice(tup1)
                    dama = random.choice(tup2)
                    print(herra, "og", dama)
                print(pararandom(tup1, tup2))
            elif val == 4:
                #Liður 1 - 4 Para öll pörin random saman
                def paraRandomStakur(tup1, tup2):
                    listi1 = []
                    listi2 = []
                    for x in range(len(tup1)):
                        herra = random.choice(tup1)
                        if herra in listi1:
                            while herra in listi1:
                                herra = random.choice(tup1)
                        listi1.append(herra)
                    for i in range(len(tup2)):
                        dama = random.choice(tup2)
                        if dama in listi2:
                            while dama in listi2:
                                dama = random.choice(tup2)
                        listi2.append(dama)
                    for x in range(len(listi1)):
                        print("Random val herra og dömu:", listi1[x], "og", listi2[x])
                print(paraRandomStakur(tup1, tup2))
            elif val == 5:
                #Liður 1 - 5 - Finna staf
                listi = []
                stafur = input("Finna nöfn sem innihalda stafinn:")
                def finnaNafn(stafur, tup2):
                    for x in tup2:
                        for i in x:
                            if i == stafur:
                                print("nafnið", x, "er með stafinn", i)
                print(finnaNafn(stafur, tup2))
            elif val == 6:
                #Liður 1 - 6 Finna fyrsta staf í tuple lista
                stafur = input("Finna nöfn sem hafa fyrsta staf:")
                def finnfyrstistafur(tup1, tup2):
                    for x in tup1:
                        if x[0:1] == stafur:
                            print("Nafnið", x, "er með", stafur, "sem fyrsta staf")
                    for x in tup2:
                        if x[0:1] == stafur:
                            print("Nafnið", x, "er með", stafur, "sem fyrsta staf")
                print(finnfyrstistafur(tup1, tup2))
            elif val == 7:
                #Skila lista af nöfnum sem innihalda nn
                def listinafnmedn(tup1, tup2):
                    listi = []
                    for x in tup1, tup2:
                        for i in x:
                            if "nn" in i:
                                listi.append(i)
                    print(listi)
                print(listinafnmedn(tup1, tup2))
            elif val == 8:
                dansspor = False
    elif val == 2:
        simaskra = {"Hreiðar":7617603,"Gunni":7777777,"Jóna":1111111,"Jónas":2222222,"Hnoðrína":3333333,
                    "Hnoðri":4444444,"Pétur":8462875,"Silla":5555555,"Gunna":6666666,"Andri":8888888}
        print(simaskra)
        nafn = input("Sláðu inn nafn til að finna það")
        def finnasima(simaskra,nafn):
            if nafn in simaskra:
                gildi = simaskra.get(nafn)
                print("Þetta fannst undir nafninu",nafn,":",gildi)
            elif nafn not in simaskra:
                print("Nafnið fannst ekki")
        print(finnasima(simaskra,nafn))
    elif val == 3:
        bekkur = {"Hreiðar":35,"Gunni":17,"Jóna":32,"Jónas":16,"Hnoðrína":20,
                  "Hnoðri":14,"Pétur":18,"Silla":45,"Gunna":17,"Andri":15,
                  "Jón":13,"Hjölli":15,"Hekla":16,"Anton":14,"Jonni":16}
        valmynd = True
        while valmynd == True:
            print("1. Skrifa út alla nemendur")
            print("2. 18 ára og eldri")
            print("3. Meðalaldur")
            print("4. heildaraldur")
            print("5. Stafur og meðalaldur")
            print("6. Hætta")
            val = int(input("Veldu nú"))
            if val == 1:
                def allirnememdur(bekkur):
                    for key, value in bekkur.items():
                        print("Nafn: {0} Aldur: {1}".format(key,value))
                    for x in bekkur:
                        print("Nafn:",x,"Aldur:",bekkur[x])
                print(allirnememdur(bekkur))
            elif val == 2:
                def yfiraldur(bekkur):
                    nyrdict=[]
                    teljari = 0
                    for x in bekkur:
                        if bekkur[x] > 17:
                            nyrdict.append(x)
                            teljari +=1
                            print("Hann",x,bekkur[x],"er 18+")
                    for x in nyrdict:
                        print("Hann",x,"Er 18 ára eða eldri")
                    print("Það eru",teljari,"nemendur yfir 18 ára")
                print(yfiraldur(bekkur))
            elif val == 3:
                def finnamedalaldur(bekkur):
                    nyrlisti=[]
                    summa=0
                    for x in bekkur:
                        nyrlisti.append(bekkur[x])
                    for x in nyrlisti:
                        summa=summa+x
                    lengdlista = len(nyrlisti)
                    medalaldur = summa / lengdlista
                    return round(medalaldur,2)
                print(finnamedalaldur(bekkur))
            elif val == 4:
                def finnaheildaraldur(bekkur):
                    nyrlisti = []
                    summa = 0
                    for x in bekkur:
                        nyrlisti.append(bekkur[x])
                    for x in nyrlisti:
                        summa = summa + x
                    return summa
                print(finnaheildaraldur(bekkur))
            elif  val == 5:
                nyrlisti = []
                stafur = input("Sláðu inn staf til að finna öll nöfn sem byrja á þeim staf")
                def nafn(bekkur):
                    for x in bekkur:
                        if x[0:1] == stafur:
                            nyrlisti.append(bekkur[x])
                            print(x,bekkur[x])
                print(nafn(bekkur))
                def medalaldur(nyrlisti,bekkur):
                    summa = 0
                    lengd = len(nyrlisti)
                    for x in nyrlisti:
                        summa = summa + x
                    medalaldur = summa / lengd
                    return "Meðalaldur þeirra sem byrja á "+stafur+" er "+str(medalaldur)
                print(medalaldur(nyrlisti,bekkur))
            elif val == 6:
                valmynd = False
    elif val == 4:
        on = False
print("Takk fyrir að nota mig")