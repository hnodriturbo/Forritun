#Hreiðar Pétursson
#Skilaverkefni 1 - áfangi 2
#13 Mars 2023
import random
import math

#Byrja á að opna valmynd fyrir verkefnið
on = True
while on == True:
    print("Velkomin í forritið mitt")
    print("1. Listi")
    print("2. Skráningaform")
    print("3. Lukkuhjól")
    print("4. Runureikningur")
    print("5. Skammstöfun")
    print("6. Hætta")
    val = int(input("Veldu nú"))
    if val == 1:
        #Set 200 random tölur inn í lista og bý til aðra valmynd
        listi = []
        for x in range(200):
            tala = random.randint(1,100)
            listi.append(tala)
        valmynd = True
        while valmynd == True:
            print("1. Prenta út listann")
            print("2. Talan 6")
            print("3. Meðaltal")
            print("4. Öfug röð 10 dálkar")
            print("5. Fjöldi talna á talnabili")
            print("6. Hætta")
            val = int(input("Veldu nú"))
            if val == 1:
                #Hér keyri ég í gegnum listann og prenta hann út 5 tölur í hverja línu
                teljari = 0
                for x in listi:
                    print(x,end=" ")
                    teljari += 1
                    if teljari % 5 == 0:
                        print("")
            elif val == 2:
                #Keyri í gegnum listann og tel hversu margar tölurnar 6 eru í listanum
                teljari = 0
                lengd = len(listi)
                for x in range(lengd):
                    if listi[x] == 6:
                        teljari += 1
                        print("Talan 6 fannst og er númer",x, "í listanum")
                print("Talan 6 kom", teljari, "sinnum fyrir í listanum")
            elif val == 3:
                #Keyri í gegnum listann og summa upp allar tölurnar og finn út meðaltal þeirra
                summa = 0
                lengdlista = len(listi)
                for x in listi:
                    summa = summa + x
                medaltal = summa / lengdlista
                print("Meðaltal listans er",round(medaltal,3))
            elif val == 4:
                #Geri nýjan lista úr gamla og hef hann afturábak og prenta hann út 20 gildi per línu
                teljari = 0
                listiafturabak = list(reversed(listi))
                for x in listiafturabak:
                    print(x, end=" ")
                    teljari += 1
                    if teljari % 20 == 0:
                        print("")
            elif val == 5:
                #Hækka teljara um einn í hvert skipti sem lúppan finnur tölur á bilinu 51-100
                teljari = 0
                for x in listi:
                    if x > 50 and x < 101:
                        teljari += 1
                print("Tölur á bilinu 51-100 eru",teljari)
            elif val == 6: #Hætta valmöguleikinn
                valmynd = False
    elif val == 2:
        #Bið notanda um nöfn til að skrá inn í lista og bæti þeim við
        listi = []
        nofn = int(input("Hvað eru margir sem eru skráðir í hópinn FOR1TÖ05BU ?"))
        for x in range(nofn):
            nafn = input("Sláðu inn nafn til að skrá í hópinn")
            listi.append(nafn)
        #Bý til glææææænýja valmynd aftur
        valmynd = True
        while valmynd == True:
            print("Skráningarform")
            print("1. Prenta raðaðan lista(í öfugri stafrófsröð")
            print("2. Eyða")
            print("3. Bæta við")
            print("4. Prenta óbreyttan lista")
            print("5. Hætta")
            val = int(input("Veldu nú"))
            if val == 1:
                #Sorta nýjan lista afturábak úr þeim gamla og prenta út
                aftur2 = sorted(listi,reverse=True)
                for x in range(len(aftur2)):
                    print(x+1,":",aftur2[x])
            elif val == 2:
                #Bý til glænýja valmynd fyrir EYÐA valmöguleika
                valmynd2 = True
                while valmynd2 == True:
                    print("1. Slá inn nafn til að eyða")
                    print("2. Velja úr lista nafn til að eyða")
                    print("3. Fara tilbaka í fyrri valmynd")
                    val = int(input("Veldu nú"))
                    if val == 1:
                        #Hérna er hægt að slá inn nafn til að eyða
                        eyda = input("Sláðu inn nafn sem þú vilt eyða úr listanum")
                        if eyda in listi:
                            print("Tókst að eyða",eyda,"úr listanum")
                            listi.remove(eyda)
                        elif eyda not in listi:
                            print("Nafnið fannst ekki")
                    elif val == 2:
                        #Prenta út listann með númerum og eyði út úr listanum með númeravali frá notanda
                        for x in range(len(listi)):
                            print(x+1,"-",listi[x])
                        valeyda = int(input("Veldu númer hvað þú vilt eyða"))
                        valeyda = valeyda - 1
                        for x in range(len(listi)):
                            if valeyda == x:
                                print("Tókst að eyða", listi[x], "úr listanum")
                                del listi[valeyda]
                    elif val == 3: #Hætta valmöguleikinn
                        valmynd2 = False
            elif val == 3:
                #Hérna bæti ég við nafni á listann sem notandi slær inn
                nyttnafn = input("Sláðu inn nafn sem þú vilt bæta á listann")
                listi.append(nyttnafn)
                for x in listi:
                    if nyttnafn == x:
                        print("Tókst að bæta við nafninu")
            elif val == 4:
                #Prenta út listann óbreyttan eins og hann var í byrjun. Óhreyfður
                print("Hér er óbreyttur listi")
                for x in range(len(listi)):
                    print(x+1,":",listi[x])
            elif val == 5:#Hætta valmöguleikinn
                valmynd = False
    elif val == 3:
        #set summu sem 0 og kastteljjara sem 0 og bý til lista sem geymir hvert teningakast
        summa18 = 0
        kastnr = 0
        listikast = []
        hversuoft = int(input("Hversu oft viltu kasta þremur 6 hliða teningum?"))
        #Keyri lúppu sem kastar teningunum þremur eins oft og notandi velur
        for x in range(hversuoft):
            kastnr += 1
            print("Þetta er kast númer",kastnr)
            #Set hvert kast inn í listann
            teningur1 = random.randint(1, 6)
            listikast.append(teningur1)
            teningur2 = random.randint(1, 6)
            listikast.append(teningur2)
            teningur3 = random.randint(1, 6)
            listikast.append(teningur3)
            #Prenta út hvað hver teningur kemur upp sem
            print("Teningur 1:",teningur1)
            print("Teningur 2:",teningur2)
            print("Teningur 3:",teningur3)
            #Summa hvert kast og prenta út summuna
            summa = 0
            summa = teningur1 + teningur2 + teningur3
            print("Summa kastsins er",summa)
            print("")
            #Ef summan er 18 koma skilaboð
            if summa == 18:
                summa18 += 1
                print("BINGÓ þú fékkst þrjár sexur!")
        #Til að finna út hvaða tala kom oftast upp geri ég teljaralista sem telur
        #hversu oft hver tala kom fyrir og setur hana inn teljaralistann
        teljaralisti = []
        tala1 = listikast.count(1)
        tala2 = listikast.count(2)
        tala3 = listikast.count(3)
        tala4 = listikast.count(4)
        tala5 = listikast.count(5)
        tala6 = listikast.count(6)
        teljaralisti.append(tala1)
        teljaralisti.append(tala2)
        teljaralisti.append(tala3)
        teljaralisti.append(tala4)
        teljaralisti.append(tala5)
        teljaralisti.append(tala6)
        #Svo finn ég hvaða tala er hæðst í þeim lista
        haedsta = max(teljaralisti)
        #Keyri lúppu og nota index listans til að finna út hvaða tala það er
        #sem hæðsta og lægsta gildi tengist við
        for x in range(len(teljaralisti)):
            if teljaralisti[x] == haedsta:
                print("Talan",x+1,"kom oftast upp")
        laegsta = min(teljaralisti)
        for x in range(len(teljaralisti)):
            if teljaralisti[x] == laegsta:
                print("Talan",x+1,"kom sjaldnast upp")
        #Ef þrjár sexur komu þá prentast bingó skilaboð, annars ekki
        if summa18 != 0:
            print("Þrjár sexur komu",summa18,"sinnum! Bingó!")
        else:
            print("Því miður komu þrjár sexur ekki í neinu kasti")
        print("")

    elif val == 4:
        #Bið notanda um nafn til að bera saman og finn út lengd nafnanna
        print("Athuga hvaða stafir eru á sama stað og hvort nöfnin séu jafnlöng")
        nafn1 = input("Sláðu inn fyrra nafn")
        nafn2 = input("Sláðu inn seinna nafn")
        lengdnafn1 = len(nafn1)
        lengdnafn2 = len(nafn2)
        #Ef nöfnin eru jafnlöng prentast skilaboð
        if lengdnafn2 == lengdnafn1:
            print("Nöfnin eru jafnlöng")
        else:
            print("Nöfnin eru ekki jafn löng. Fyrra nafn er",lengdnafn1,"stafir og seinna nafn er",lengdnafn2,"stafir")

        #Fer eftir því hvort nafnið er lengra hvaða for lúppu ég keyri svo ég pottþétt beri alla stafina saman
        #Keyri for lúppu og ber saman staf við staf og prenta skilaboð ef það finnst eins bókstafur
        if len(nafn1) < len(nafn2):
            for x in range(len(nafn1)):
                if nafn1[x] == nafn2[x]:
                    print("Bókastafur númer", x + 1, nafn1[x], "er eins í báðum nöfnum")

        elif len(nafn1) > len(nafn2):
            for x in range(len(nafn2)):
                if nafn1[x] == nafn2[x]:
                    print("Bókastafur númer",x+1,nafn1[x],"er eins í báðum nöfnum")
        else:
            for x in range(len(nafn1)):
                if nafn1[x] == nafn2[x]:
                    print("Bókastafur númer",x+1,nafn1[x],"er eins í báðum nöfnum")
    elif val == 5:
        #Útskýri vel hvernig á að stafa áfanga og bið notanda að slá inn áfanga
        print("Skammstafa áfanga checkerinn minn")
        print("Fyrstu 4 eiga að vera stórir bókstafir")
        print("Bókstafur 5 á að vera tala, næstu 2 svo stórir bókstafir")
        print("svo koma 2 tölur og bandstrik og í kjölfarið 2 stórir bókstafir")
        print()
        afangi = input("Sláðu inn skammstöfun áfanga rétt inn")
        #Keyri tjekk fyrir tjekk hvort stafir séu upper og alpha og hvort tölur séu tölur
        #Ef eitthvað í þessu ferli klikkar koma villuskilaboð
        if afangi[0:4].isalpha() and afangi[0:4].isupper():
            if afangi[4:5].isdigit:
                if afangi[5:7].isalpha and afangi[5:7].isupper():
                    if afangi[7:9].isdigit:
                        if afangi[9] == "-":
                            if afangi[10:11].isalpha() and afangi[10:11].isupper():
                                print("Þetta er rétt skammstöfun á áfanga")
                            else:
                                print("ekki rétt skammstöfun")
                        else:
                            print("ekki rétt skammstöfun")
                    else:
                        print("ekki rétt skammstöfun")
                else:
                    print("Ekki rétt skammstöfun")
            else:
                print("Þetta er ekki rétt skammstöfun áfanga")
        else:
            print("Þetta er ekki rétt skammstöfun á áfanga")
        #Val númer sex er hætta valmöguleikinn
    elif val == 6:
        on = False
    #Ef ekki er rétt valið koma villuskilaboð
    else:
        print("Ekki rétt val")
#Takk fyrir mig!
print("Takk fyrir að nota forritið mitt")