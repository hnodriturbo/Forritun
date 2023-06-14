# Hreiðar Pétursson
# 17 apríl 2023
# Skilverkefni 3 - Áfangi 2

import random

#Hefjum valmynd
on = True
while on == True:
    try:
        print("1. Talnaruna")
        print("2. Spurningabanki")
        print("3. Símaskrá")
        print("4. Hætta")
        val = int(input("Hvað viltu gera?"))

        if val == 1: # Talnaruna
            #Geri skráarbreytuna og geri valmynd
            skra = "files/randomtolur.txt"
            innrivalmynd = True
            while innrivalmynd == True:
                print("1. Skrifa tölurnar í skránna")
                print("2. Lesa tölurnar úr skránni")
                print("3. Birta meðaltal talnanna")
                print("4. Hætta")
                valinnri = int(input("Veldu nú"))

                if valinnri == 1: # Skrifa tölurnar í skránna
                    listi = []
                    # Fall sem tekur inn listann sem færibreytu
                    # Bý til random tölu, bæti henni í listann og skrifa tölurnar í skrá í stærðarröð
                    def skrifalista(listi):
                        for x in range(100):
                            tala = random.randint(10,20)
                            listi.append(tala)
                        listi.sort()
                        with open(skra,"w",encoding="utf-8") as gogn:
                            for x in range(len(listi)):
                                xx = str(listi[x])
                                if x != 0:
                                    gogn.write("-" + xx)
                                else:
                                    gogn.write(xx)

                    # Kalla á fallið með breytu og prenta út staðfestingu
                    kallaskrifalista = skrifalista(listi)
                    print("Tölurnar hafa verið settar í skránna í stærðar röð")

                elif valinnri == 2: # Lesa tölurnar úr skránni
                    # Geri fall sem les skránna, breytir strengjum í tölur og prenta út tíu tölur í línu
                    def lesalista(skra):
                        with open(skra,"r",encoding="utf-8") as gogn:
                            linur = gogn.read().split("-")
                        for x in range(len(linur)):
                            xx = int(linur[x])
                            linur[x] = xx
                        for x in range(len(linur)):
                            x += 1
                            if x == 100:
                                x -= 1
                            if x % 10 == 0:
                                print(linur[x])
                            else:
                                print(linur[x],end=" ")
                        print("")

                    # Kalla á fallið
                    lesalistabreyta = lesalista(skra)

                elif valinnri == 3: # Birta meðaltal talnanna
                    # Geri fall sem opnar skránna og setur gögnin í breytu, breytir strengjum
                    # í tölur og finnur út meðaltal talnanna og skilar niðurstöðu með 1 aukastaf
                    def medaltal(skra):
                        with open(skra,"r",encoding="utf-8") as gogn:
                            lesagogn = gogn.read().split("-")
                        for x in range(len(lesagogn)):
                            xx = int(lesagogn[x])
                            lesagogn[x] = xx
                        summa = 0
                        for x in lesagogn:
                            summa += x
                        lengdlista = len(lesagogn)
                        medaltal = summa / lengdlista

                        return "{0:.1f}".format(medaltal)

                    # Prenta út fallið
                    print(medaltal(skra))

                elif valinnri == 4: # Hætta valmöguleikinn
                    innrivalmynd = False

        elif val == 2: # Spurningabankinn

            # FÖLL SEM ÉG NOTA Í ÞESSUM LIÐ ERU EFST !

            # Fall sem sækir gögnin og setur í lista
            def lesatilvitnanir():
                spurningarogsvor = []
                with open("files/quotes.csv", "r", encoding="utf-8") as gogn:
                    linur = gogn.read().splitlines()
                    for x in linur:
                        x = x.replace("\'", "")
                        x = x.split(";")
                        spurningarogsvor.append(x)
                return spurningarogsvor

            # Fall sem athugar hvort svarið er rétt eða rangt
            def spurningin(svar):
                if svar != rettsvar:
                    print("Ekki rétt svar")
                    return False
                else:
                    print("Þetta var hárrétt svar hjá þér!!!")
                    return True

            # Gerum valmynd
            innrivalmynd2 = True
            while innrivalmynd2 == True:
                try: # Nota þetta þannig það komi ekki villa
                    print("Til að hætta í miðjum leik skrifaðu töluna 9")
                    valmenu = int(input("1. Byrja leikinn - 2. Hætta"))

                    # Ef ekki er rétt valið koma skilaboð
                    if valmenu not in (1,2):
                        print("Vinsamlegast veldu 1 eða 2")

                    # Byrja leikinn og núllstilli teljara og geri tóman lista
                    elif valmenu == 1:
                        buinnadspyrja = []
                        teljari = 0
                        teljarirettsvor = 0
                        tilraun = 0

                        # Næ í gögnin úr skránni og set í lista með fallinu
                        spurningarogsvor = lesatilvitnanir()
                        # 10 spurningar þýða að lykkjan keyrir 10 sinnum
                        while teljari < 10:
                            teljaritvoskipti = 0
                            teljari += 1


                            #Bý til spurninguna og svarið og set í annan lista
                            val = random.choice(spurningarogsvor)
                            if val in buinnadspyrja:
                                while val in buinnadspyrja:
                                    val = random.choice(spurningarogsvor)
                            buinnadspyrja.append(val)
                            spurning = buinnadspyrja[-1][0]
                            rettsvar = buinnadspyrja[-1][1]

                            # Og við spurjum notandann og fáum svarið
                            print("Spurningin er:")
                            print(spurning)
                            svar = input("Svarið þitt er:")

                            # Hætta valmöguleikinn
                            if svar == '9':
                                break

                            # Athuga svarið með fallinu og hækka teljara
                            athugasvar = spurningin(svar)
                            tilraun += 1
                            teljaritvoskipti += 1

                            # Ef svarið er vitlaust keyrir þessi blokk og spyr aftur
                            if athugasvar == False:
                                print("Spurt var að")
                                print(spurning)
                                svar = input("Svarið þitt er:")
                                if svar == '9':
                                    break

                                # Athuga seinna svarið og hækka teljara
                                athugasvar = spurningin(svar)
                                tilraun += 1
                                teljaritvoskipti += 1

                                # Ef svarið er rétt fær hann stig
                                if athugasvar == True:
                                    teljarirettsvor += 1

                                # Ef notandi hefur reynt tvisvar vitlaust fær hann rétta svarið
                                elif teljaritvoskipti == 2 and athugasvar == False:
                                    print("rétta svarið er:")
                                    print(rettsvar)

                            # Ef svarið er rétt fær hann stig
                            elif athugasvar == True:
                                teljarirettsvor += 1

                        # Í lokinn prentast út yfirlit yfir leikinn
                        print("Leikurinn er búinn")
                        print("Þú svaraðir",teljari,"spurningum í",tilraun,"tilraunum og varst með",teljarirettsvor,"rétt svör")

                    # Loka leiknum
                    elif valmenu == 2:
                        innrivalmynd2 = False

                # Ef það kemur einhver villa þá koma þessi skilaboð
                except ValueError:
                    print("Vinsamlegast veldu 1 eða 2")

        elif val == 3:

            # FÖLL SEM ÉG NOTA Í ÞESSUM LIÐ

            # Fallið sem nær í gögnin úr skránni og skilar þeim í lista
            def lesasimaskra():
                listi = []
                nyrlisti = []
                with open("files/simaskra.csv","r",encoding="utf-8") as gogn:
                    linur = gogn.read().splitlines()
                    print(linur)
                    for x in linur:
                        x = x.split("\n")
                        for i in range(len(x)):
                            x[i] = x[i].split(";")
                        nyrlisti.append(x)
                    print(nyrlisti)
                for x in nyrlisti:
                    for i in x:
                        listi.append(i)
                return listi

            # Fallið sem bætið nýjum aðila á listann
            def nyr(nafn,kt,simanumer):
                nyradililisti = []
                nyradililisti.append(nafn)
                nyradililisti.append(kt)
                nyradililisti.append(simanumer)
                listi.append(nyradililisti)
                print("Það tókst að bæta við",nafn,"í símaskránna")

            # Fallið sem breytir símanúmeri eftir kennitölu
            def breyta(kt,simanumer):
                for x in listi:
                    for i in x:
                        if kt == i:
                            x[2] = simanumer
                            print("Það tókst að breyta símanúmeri hjá", x[0])

            # Fallið sem eyðir úr listanum eftir kennitölu
            def eyda(kt):
                for x in listi:
                    if kt in x:
                        print("Það tókst að eyða",x[0])
                        listi.remove(x)
                        return True
                return listi

            # Fallið sem prentar út símaskránna
            def prenta():
                nyrlisti = []
                listi = []
                with open("files/simaskra.csv","r",encoding="utf-8") as gogn:
                    lesalinur = gogn.read().splitlines()
                    for x in lesalinur:
                        x = x.split("\n")
                        for i in range(len(x)):
                            x[i] = x[i].split(";")
                        nyrlisti.append(x)
                for x in nyrlisti:
                    for i in x:
                        listi.append(i)
                print("Þetta er Símaskráin þín:")
                for x in range(len(listi)):
                    print(x+1,":",listi[x][0],"Kt:",listi[x][1],"Sími:",listi[x][2])
                return listi

            # Fallið sem skrifar í símaskránna
            def skrifaisimaskra(listi):
                glaenyrlisti = []
                for x in listi:
                    sameinadurstrengurilista = ";".join(x)
                    glaenyrlisti.append(sameinadurstrengurilista)
                with open("files/simaskra.csv","w",encoding="utf-8") as gogn:
                    for x in glaenyrlisti:
                        gogn.write(x)
                        gogn.write("\n")
                print("Það tókst að skrifa í skránna")

            # AUKA - Fall sem athugar hvort innslegin kt sé í listanum
            def athuga(kt,listi):
                for x in listi:
                    if kt in x:
                        return True

            #  BYRJA Á AÐ KEYRA VALMYNDINA
            simaskravalmynd = True
            while simaskravalmynd == True:
                try:
                    print("1. Bæta við nýjum")
                    print("2. Breyta upplýsingum úr skránni")
                    print("3. Eyða vini úr skránni")
                    print("4. Prenta út alla skránna")
                    print("5. Hætta")
                    print("6. AUKA --- BREYTA NAFN, KT OG SÍMA --- AUKA")
                    val = int(input("Veldu nú"))

                    if val == 1: # Bæta við nýjum í skránna

                        # Næ í símaskránna og set í listi
                        listi = lesasimaskra()
                        print(listi)
                        # Bið notanda um nýju upplýsingarnar
                        nafn = input("Sláðu inn nafn")
                        kt = input("Sláðu inn kennitölu")
                        simanumer = input("Sláðu inn símanúmer")

                        # Kalla á fallið sem breytir listanum
                        kallanyr = nyr(nafn, kt, simanumer)

                        # Skrifa nýja listann í símaskránna
                        kallaskrifaisimaskra = skrifaisimaskra(listi)


                    elif val == 2: # Breyta upplýsingum (kt)

                        # Næ í gögnin og set í lista
                        listi = lesasimaskra()

                        # Bið notanda um gögn
                        kt = input("Sláðu inn kt hjá þeim sem skal breyta")
                        kallaathuga = athuga(kt,listi)

                        # Ef kennitala finnst á listanum keyrist restin
                        if kallaathuga == True:
                            # Bið um nýja símanr, keyri breyta fallið og skrifa fallið
                            simanumer = input("Sláðu inn nýja símanúmerið")
                            kallabreyta = breyta(kt,simanumer)
                            kallaskrifaisimaskra = skrifaisimaskra(listi)

                        # Ef kennitalan finnst ekki kemur villa
                        else:
                            print("Kennitalan finnst ekki")


                    elif val == 3: # Eyða vin úr símaskránni

                        # Næ í símaskránna og set í lista
                        listi = lesasimaskra()

                        # Bið notanda um kennitölu og athuga hvort hún sé til
                        kt = input("Sláðu inn kennitölu þess sem skal eyða")
                        kallaathuga = athuga(kt,listi)

                        # Ef kennitalan er í skránni keyrist eyða fallið og skrifa fallið
                        if kallaathuga == True:
                            kallaeyda = eyda(kt)
                            kallaskrifaisimaskra = skrifaisimaskra(listi)

                        # Annars kemur villa
                        else:
                            print("Kennitalan fannst ekki")

                    elif val == 4: # Prenta
                        # Prenta út skránna með fallinu
                        kallaprenta = prenta()

                    elif val == 5: # Hætta valmöguleikinn
                        simaskravalmynd = False

                    elif val == 6: # AUKA --- BREYTA NAFN,KT EÐA SÍMANR

                        # Prenta út símaskránna með númerum til að velja til að breyta
                        listi = prenta()
                        val = int(input("Veldu númer hvað þú vilt breyta"))

                        # Geri fall sem velur notanda úr lista og skilar því í nýjum lista til að vinna með
                        def velja(val,listi):
                            val -= 1
                            nyrlisti = []
                            for x in range(len(listi)):
                                if x == val:
                                    for i in listi[x]:
                                        nyrlisti.append(i)
                            print("Þú valdir:")
                            print(x+1, ":", nyrlisti[0], "Kt:", nyrlisti[1], "Sími:", nyrlisti[2])
                            return nyrlisti

                        # Geri nyrlisti með velja fallinu
                        nyrlisti = velja(val,listi)

                        # Fallið til að breyta nafni
                        def breytanafn(nyttnafn,val):
                            nyrlisti[0] = nyttnafn
                            val -= 1
                            for x in range(len(listi)):
                                if x == val:
                                    listi[x][0] = nyrlisti[0]
                            print(x + 1, ":", nyrlisti[0], "Kt:", nyrlisti[1], "Sími:", nyrlisti[2])


                        # Fallið til að breyta kennitölu
                        def breytakennitolu(nykt,val):
                            nyrlisti[1] = nykt
                            val -= 1
                            for x in range(len(listi)):
                                if x == val:
                                    listi[x][1] = nyrlisti[1]
                            print(x + 1, ":", nyrlisti[0], "Kt:", nyrlisti[1], "Sími:", nyrlisti[2])

                        # Fallið til að breyta símanúmeri
                        def breytasimanumer(nyttsimanr,val):
                            nyrlisti[2] = nyttsimanr
                            val -= 1
                            for x in range(len(listi)):
                                if x == val:
                                    listi[x][2] = nyrlisti[2]
                            print(x + 1, ":", nyrlisti[0], "Kt:", nyrlisti[1], "Sími:", nyrlisti[2])


                        # Fallið til að eyða
                        def eydavidkomandi(listi,val):
                            val -= 1
                            for x in range(len(listi)):
                                if val == x:
                                    print(listi[x][0], "var eytt")
                                    del listi[x]


                        # Geri valmynd
                        valmynd3 = True
                        while valmynd3 == True:
                            valmenu = int(input("1. Breyta nafni - 2. Breyta kt - 3. Breyta símanúmeri - 4. Vista breytingar - 5. Eyða viðkomandi"))

                            if valmenu == 1: # Breyta nafni
                                # Bið um nýtt nafn og framkalla breytinguna með falli
                                nyttnafn = input("Sláðu inn nýtt nafn")
                                kallabreytanafn = breytanafn(nyttnafn,val)

                            elif valmenu == 2: # Breyta kennitölu
                                # Bið um nýja kennitölu og framkalla breytingu með falli
                                nykt = input("Sláðu inn nýja kt")
                                kallanykt = breytakennitolu(nykt,val)

                            elif valmenu == 3: # Breyta símanúmeri
                                # Bið um nýtt símanúmer og framkalla breytingu með falli
                                nyttsimanr = input("Sláðu inn nýtt símanúmer")
                                kallanyttsimanr = breytasimanumer(nyttsimanr,val)

                            elif valmenu == 4: # Vista breytingar
                                # Nota fallið skrifa í símaskrá til að vista breytingar
                                kallaskrifaisimaskra = skrifaisimaskra(listi)
                                valmynd3 = False

                            elif valmenu == 5: # Eyða viðkomandi
                                # Nota fallið eyða til að eyða úr listanum og skrifa svo listann í skránna
                                kallaeyda = eydavidkomandi(listi,val)
                                kallaskrifaisimaskra = skrifaisimaskra(listi)
                                valmynd3 = False

                            elif val == 5: # Hætta valmöguleikinn
                                valmynd3 = False

                    # Ef ekki er rétt valið kemur villa
                    elif val not in (1,2,3,4,5):
                        print("Verður að velja rétt")

                # Ef eitthvað kemur upp þá kemur villa
                except ValueError:
                    print("Villa. Veldu rétt")

        # Hætta í forritinu
        elif val == 4:
            on = False

        # Villuskilaboð
        else:
            print("þú hefur ekki valið rétt")
    except ValueError:
        print("Veldu rétt")

# TAKK FYRIR AÐ SKOÐA KÓÐANN MINN !!!
print("Takk fyrir að nota forritið mitt")