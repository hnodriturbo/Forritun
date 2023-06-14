#Hreiðar Pétursson
#Lokaverkefni
#14.Febrúar.2023

import math
import random

on = True

while on == True:

    print("1. Samlagning")
    print("2. Skæri, blað, steinn")
    print("3. Samanburður")
    print("4. Teningar")
    print("5. Teningaspilið Craps")
    print("6. Happadrætti")
    print("7. Hætta")
    val = int(input("Hvað viltu gera?"))

    if val == 1: #Samlagning
        #Set breytuna fyrir tölu og summu
        tala = 1
        summa = 0

        #Á meðan talan er ekki 0 keyrir kóðinn
        while tala != 0:
            tala = int(input("Sláðu inn tölu"))

            if tala > 0: #Ef talan er meiri en 0 keyrir þessi kóði
                #Plúsum frá 1 og upp að tölunni sem notandi velur og prenta niðurstöðuna
                for x in range(1,tala+1):
                    summa = summa + x
                    if x == tala:
                        print(x,end="")
                    else:
                        print(x,end="+")
                print(" gefur töluna",summa)

            elif tala < 0: #Ef talan er minni en 0 keyrir þessi kóði
                #Plúsa frá tölunni og niður að 0 og prenta út niðurstöðuna
                for x in range(tala,0):
                    summa = summa + x
                    if x == -1:
                        print("(",x,")",end="",sep="")
                    else:
                        print("(",x,")","+",end="",sep="")
                print(" gefur töluna",summa)

            #Ef talan er 0 prentast þetta og forritið hættir
            elif tala == 0:
                print("Takk fyrir að nota forritið mitt")

    elif val == 2: #Skæri, blað, steinn
        #Byrja á að setja boolean breytu og hina ýmsu teljara
        spila = True
        teljarijafntefli = 0
        teljarisigur = 0
        teljaritap = 0
        teljarileikir = 0
        teljaritolvavann = 0
        teljaritolvatapadi = 0
        listi = ["Skæri", "Blað", "Steinn"]

        #Bið leikmann um upplýsingar og byrja leikinn og bý til menu
        nafn = input("Hvað heitir þú fullu nafni?")
        aldur = int(input("Hvað ertu gamall/gömul?"))
        while spila == True:
            print()
            print("Velkominn í skæri blað steinn leikinn minn")
            print()
            print("Veldu 1 til að vera skæri")
            print("Veldu 2 til að vera blað")
            print("Veldu 3 til að vera steinn")
            print("Veldu 4 til að hætta")
            val = int(input("Veldu nú"))

            if val == 1: #Skæri
                #Læt tölvuna velja og prenta út hvað hvor valdi
                valtolvu = random.choice(listi)
                print()
                print("Þú valdir Skæri")
                print("Tölvan valdi",valtolvu)

                #Fer eftir því hvað tölvan valdi hver niðurstaðaleiksins verður
                #Læt telja hvern leik og hvor vann eða hvort fór jafntefli
                if valtolvu == "Skæri":
                    print("Leikurinn fór jafntefli")
                    teljarijafntefli = teljarijafntefli + 1
                    teljarileikir = teljarileikir + 1
                elif valtolvu == "Blað":
                    print("Þú vannst! Tölvan valdi",valtolvu)
                    teljarisigur = teljarisigur + 1
                    teljaritolvatapadi = teljaritolvatapadi + 1
                    teljarileikir = teljarileikir + 1
                elif valtolvu == "Steinn":
                    print("Þú tapaðir!! Tölvan valdi",valtolvu)
                    teljaritap = teljaritap + 1
                    teljaritolvavann = teljaritolvavann + 1
                    teljarileikir = teljarileikir + 1

            elif val == 2: #Blað
                # Læt tölvuna velja og prenta út hvað hvor valdi
                valtolvu = random.choice(listi)
                print()
                print("Þú valdir Blað")
                print("Tölvan valdi", valtolvu)

                #Fer eftir því hvað tölvan valdi hver niðurstaðaleiksins verður
                #Læt telja hvern leik og hvor vann eða hvort fór jafntefli
                if valtolvu == "Skæri":
                    print("Þú tapaðir!! Tölvan valdi", valtolvu)
                    teljaritap = teljaritap + 1
                    teljaritolvavann = teljaritolvavann + 1
                    teljarileikir = teljarileikir + 1
                elif valtolvu == "Blað":
                    print("Leikurinn fór jafntefli")
                    teljarijafntefli = teljarijafntefli + 1
                    teljarileikir = teljarileikir + 1
                elif valtolvu == "Steinn":
                    print("Þú vannst! Tölvan valdi",valtolvu)
                    teljarisigur = teljarisigur + 1
                    teljaritolvatapadi = teljaritolvatapadi + 1
                    teljarileikir = teljarileikir + 1
            elif val == 3: #Steinn
                #Læt tölvuna velja og prenta út hvað hvor valdi
                valtolvu = random.choice(listi)
                print()
                print("Þú valdir steinn")
                print("Tölvan valdi", valtolvu)

                #Fer eftir því hvað tölvan valdi hver niðurstaðaleiksins verður
                #Læt telja hvern leik og hvor vann eða hvort fór jafntefli
                if valtolvu == "Skæri":
                    print("Þú vannst! Tölvan valdi", valtolvu)
                    teljarisigur = teljarisigur + 1
                    teljaritolvatapadi = teljaritolvatapadi + 1
                    teljarileikir = teljarileikir + 1
                elif valtolvu == "Blað":
                    print("Þú tapaðir!! Tölvan valdi", valtolvu)
                    teljaritap = teljaritap + 1
                    teljaritolvavann = teljaritolvavann + 1
                    teljarileikir = teljarileikir + 1
                elif valtolvu == "Steinn":
                    print("Leikurinn fór jafntefli")
                    teljarijafntefli = teljarijafntefli + 1
                    teljarileikir = teljarileikir + 1

            elif val == 4: #Niðurstöður
                #Prenta út niðurstöður leiksins með teljurunum
                print()
                print("Kæri",nafn)
                print("Aldur",aldur)
                print("Úrslit leiksins hljóða svo:")
                print("Spilaðir leikir voru",teljarileikir)
                print("Þú vannst",teljarisigur,"sinnum")
                print("Tölvan vann",teljaritolvavann,"sinnum")
                print("Jafntefli var í",teljarijafntefli,"leikjum")
                print()

                #Ef leikmaður vann fleiri eða tapaði fleiri leikjum en tölvan koma skilaboð
                if teljaritolvavann > teljarisigur:
                    print("Þvi miður tapaðir þú leiknum")
                    mismunur = teljaritolvavann - teljarisigur
                    print("Tölvan vann",mismunur,"sinnum oftar en þú")
                elif teljaritolvavann < teljarisigur:
                    print("Til hamingju!! Þú vannst leikinn!!")
                    mismunur = teljarisigur - teljaritolvavann
                    print("Þú vannst",mismunur,"sinnum oftar en tölvan")
                elif teljaritolvavann == teljarisigur:
                    print("Leikurinn fór jafntefli")
                    print("Þú vannst",teljarisigur,"sinnum og tölvan vann",teljaritolvavann,"sinnum")
                spila = False

    elif val == 3: # Samanburður
        #Byrja á að setja boolean breytu og biðja um strengina
        satt = False
        strengur1 = input("Sláðu inn fyrri strenginn")
        strengur2 = input("Sláðu inn seinni strenginn")

        #Set öftustu 2 stafina í breytu
        butur1 = strengur1[-2::]
        butur2 = strengur2[-2::]

        #Ef breyturnar eru eins þá geri ég boolean breytuna sanna
        if butur1 == butur2:
            satt = True
        else:
            satt = False

        #Skilaboð prentast eftir því hvort boolean breytan sé sönn eða ekki
        if satt == True:
            print("Síðustu tveir stafirnir eru eins")
        elif satt == False:
            print("Síðustu tveir stafirnir eru ekki eins")

        #for x in range(len(strengur1[-2::])):
        #    for i in range(len(strengur2[-2::])):
        #        if strengur1[x] == strengur2[x]:
        #            print("Þeir eru eins")

    elif val == 4: # Teningar
        #Byrja á að gera tóman lista og setja teljara og summu breytur
        listi = []
        summalistans = 0
        medaltal = 0
        teljarisumma10 = 0
        teljarisumma12 = 0
        teljarisumma7 = 0

        #geri tvær random tölur 50 sinnum og summa þær sem kast og prenta út niðurstöðuna
        for x in range(50):
            summa = 0
            teningur1 = random.randint(1,6)
            teningur2 = random.randint(1,6)
            summa = teningur1 + teningur2
            print("Kast teningur 1 =",teningur1)
            print("Kast teningur 2 =",teningur2)
            print()
            print("Samtals",summa)
            print()
            listi.append(summa)

            #Tel hvert skipti sem summan er 10,12 eða 7
            if summa == 10:
                teljarisumma10 = teljarisumma10 + 1
            elif summa == 12:
                teljarisumma12 = teljarisumma12 + 1
            elif summa == 7:
                teljarisumma7 = teljarisumma7 + 1

        #Prenta lista óraðaðan
        print("Hérna er listi summu kastanna óraðaður")
        print(listi)

        #Prenta listann út raðaðan
        print("Hérna er listi summu kastanna raðaður")
        listi.sort()
        print(listi)

        #Finna summu listans
        for x in listi:
            summalistans = summalistans + x
        print("Summa allra talnanna er:",summalistans)

        #Finna meðaltal listans
        medaltal = summalistans / 50
        print("Meðtal kastanna er:",round(medaltal,1))

        #Prenta út hve oft summa kastanna var 10,12 eða 7
        print(teljarisumma10,"sinnum var summa kastanna 10")
        print(teljarisumma12,"sinnum var summa kastanna 12")
        print(teljarisumma7,"sinnum var summa kastanna 7")


    elif val == 5: #Crabs leikurinn minn
        #Byrja á að setja teljara og hvaða köst láta leikmann tapa og hvaða köst vinna
        husidvinnur = 0
        leikmadurvinnur = 0
        listitap = [2,3,12]
        lististig = [4,5,6,8,9,10]
        teljarikast = 0
        gull = True
        #keyri lúppu til að byrja leikinn
        while gull == True:
            #Núlla stig fyrir hvern leik og teljara sem telur fyrsta kastið
            stig = 0
            kastnumer = 0
            #Byrjum leikinn
            print("Velkominn í Craps leikinn minn")
            val = int(input("veldu 1 til að byrja og 2 til að hætta"))
            if val == 1:
                #Kominn inn í leikinn og býð uppá valmynd
                gull2 = True
                while gull2 == True:
                    print("Veldu 1 til að kasta")
                    print("Veldu 2 til að hætta")
                    val2 = int(input("Veldu nú:"))

                    #Sé valið einn til að kasta keyrir þessi kóði
                    if val2 == 1:
                         #Tel hvert einasta kast fyrir lokayfirlit

                        #Keyri lúppu sem er kastið sjálft og fæ random tölu frá tveim teningum
                        for x in range(1):
                            summa = 0
                            teningur1 = random.randint(1,6)
                            teningur2 = random.randint(1,6)
                            summa = teningur1 + teningur2
                            kastnumer = kastnumer + 1
                            teljarikast = teljarikast + 1
                        print("Summa kastsins þíns var",summa)

                        #Ef summa kastsins er 7 í fyrsta kasti vinnur leikmaður
                        if summa == 7 and kastnumer == 1:
                            print("Þú vannst í fyrsta kasti með tölunni 7")
                            print()
                            leikmadurvinnur = leikmadurvinnur + 1
                            gull2 = False
                        #Ef summa kastsins er 11 í fyrsta kasti vinnur leikmaður
                        elif summa == 11 and kastnumer == 1:
                            print("Þú vannst í fyrsta kasti með tölunni 11")
                            print()
                            gull2 = False
                            leikmadurvinnur = leikmadurvinnur + 1
                        #Ef summa kastsins er á lista yfir tap summur tapar leikmaður
                        elif summa in listitap and kastnumer == 1:
                            print("Þú tapaðir leiknum því þú fékkst",summa,"í fyrsta kasti")
                            gull2 = False
                            husidvinnur = husidvinnur + 1
                        #Ef summa kastsins er á lististig hefst leikurinn þangað til leikmaður fær aftur sömu summu og í fyrsta kasti
                        elif summa in lististig and kastnumer == 1:
                            stig = summa
                            gull2 = True
                            print("Núna verðuru að kasta aftur þangað til þú færð aftur",stig)
                        #Ef kast leikmannsis er sama og í fyrstakastinu sem hóf leikinn þá vinnur leikmaður
                        elif summa == stig:
                            print("Til hamingju þú fékkst aftur töluna",summa,"og vannst því leikinn")
                            gull2 = False
                            leikmadurvinnur = leikmadurvinnur + 1
                        #Ef summa kasts er 7 áður en hann nær aftur sama og í fyrsta kastinu tapar leikmaður
                        elif summa == 7:
                            print("Þú tapaðir leiknum útaf þú fékkst 7 áður en þú náðir",stig,"aftur")
                            gull2 = False
                            husidvinnur = husidvinnur + 1

            elif val == 2:
                #Leikmaður ákveður að hætta og fær yfirlit yfir niðurstöður leiksins
                gull = False
                print("Þú vannst", leikmadurvinnur, "sinnum")
                print("Þú tapaðir", husidvinnur, "sinnum")
                print("Þú kastaðir teningnum",teljarikast,"sinnum")


    elif val == 6:#Happadrætti
        #Set boolean breytur og byrja leikinn
        lottoleikur = True
        while lottoleikur == True:
            print("Til að kaupa raðir veldu 1")
            print("Til að spila veldu 2")
            print("Til að hætta veldu 3")
            print("500 skipti")
            val = int(input("hvað viltu gera?"))

            if val == 1:
                #Lottómiðinn
                lottomidi = []
                radir = int(input("Hversu margar raðir viltu kaupa"))
                for x in range(radir):
                    lottorod = []
                    for x in range(5):
                        tala = random.randint(1,40)
                        if tala in lottorod:
                            while tala in lottorod:
                                tala = random.randint(1,40)
                        lottorod.append(tala)
                        lottorod.sort()
                    lottomidi.append(lottorod)
                print("Þú keyptir",radir,"raðir")

                #Prenta út lottómiðann
                teljarirod = 1
                for x in lottomidi:
                    print("Röð nr", teljarirod, ": ", *x, sep=" ")
                    teljarirod = teljarirod + 1

            elif val == 2:
                #Lottoniðurstöður
                dregnartolur = []
                for x in range(5):
                    tala = random.randint(1,40)
                    if tala in dregnartolur:
                        while tala in dregnartolur:
                            tala = random.randint(1,40)
                    dregnartolur.append(tala)
                dregnartolur.sort()
                print("Tölurnar sem komu voru:",*dregnartolur)

                #Setja réttu tölurnar í hverri röð í lista innan lista
                rettartolur = []
                for x in range(len(lottomidi)):
                    rettartolur1 = []
                    for a in lottomidi[x]:
                        for i in dregnartolur:
                            if a == i:
                                rettartolur1.append(a)
                    rettartolur.append(rettartolur1)

                #Prenta út allar raðirnar og hvaða tölur voru réttar
                for x in range(len(rettartolur)):
                    if len(rettartolur[x]) > 0:
                        print("Tölur réttar í röð",x+1,":",*rettartolur[x])


            elif val == 3: # Hætta valmöguleikinn (Lottó)
                lottoleikur = False
            elif val == 4: # 500 skipti
                lottomidi = []
                radir = int(input("Hversu margar raðir viltu kaupa"))
                for x in range(radir):
                    lottorod = []
                    for x in range(5):
                        tala = random.randint(1, 40)
                        if tala in lottorod:
                            while tala in lottorod:
                                tala = random.randint(1, 40)
                        lottorod.append(tala)
                        lottorod.sort()
                    lottomidi.append(lottorod)
                print("Þú keyptir", radir, "raðir")

                # Prenta út lottómiðann
                teljarirod = 1
                for x in lottomidi:
                    print("Röð nr", teljarirod, ": ", *x, sep=" ")
                    teljarirod = teljarirod + 1
                skipti = int(input("Til að spila 500 sinnum veldu 1"))
                if skipti == 1:
                    teljari = 0
                    teljari4tolur = 0
                    teljari5tolur = 0
                    while teljari < 501:
                        dregnartolur = []
                        for x in range(5):
                            tala = random.randint(1, 40)
                            if tala in dregnartolur:
                                while tala in dregnartolur:
                                    tala = random.randint(1, 40)
                            dregnartolur.append(tala)
                        dregnartolur.sort()
                        print("Tölurnar sem komu voru:", *dregnartolur)
                        # Setja réttu tölurnar í hverri röð í lista innan lista
                        rettartolur = []
                        for x in range(len(lottomidi)):
                            rettartolur1 = []
                            for a in lottomidi[x]:
                                for i in dregnartolur:
                                    if a == i:
                                        rettartolur1.append(a)
                            rettartolur.append(rettartolur1)
                            print(rettartolur)
                        for x in range(len(rettartolur)):
                            if len(rettartolur[x]) == 4:
                                teljari4tolur += 1
                            if len(rettartolur[x]) == 5:
                                teljari5tolur += 1

                        teljari +=1
                    print("4 tölur réttar gerðist",teljari4tolur,"sinnum")
                    print("5 tölur réttar gerðist",teljari5tolur,"sinnum")


                else:
                    print("villa")


        print("Takk fyrir að spila")

    elif val == 7: # Hætta valmöguleikinn
        on = False

    else:
        print("þú hefur ekki valið rétt")

print("Takk fyrir að nota forritið mitt")