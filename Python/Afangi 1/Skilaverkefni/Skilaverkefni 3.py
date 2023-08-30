#Hreiðar Pétursson
#Skilaverkefni 3
#6 Febrúar 2023

import math
import random

on = True
#Hefjum lúppu meðan on er true
while on == True:
    #Valmyndin sjálf
    print("1. Talnabil A")
    print("2. Talnabil B")
    print("3. Orðasprell")
    print("4. Stafastytting")
    print("5. Margföldun")
    print("6. Finna fjölda bókstafa og tölustafa")
    print("7. strengur")
    print("8. Strengjarugl")
    print("9. Orðaklipping")
    print("10. Ýmsilegt")
    print("11. Hætta")
    #Veldu hvað þú vilt gera input
    val = int(input("Hvað viltu gera?"))
    #Hér hefst liður 2 úr verkefninu
    if val == 1:
        #Bið notanda um tvær tölur
        tala1 = int(input("Sláðu inn tölu 1"))
        tala2 = int(input("Sláðu inn tölu 2"))
        #Set Mismunin milli talnanna og summuna
        mismunur = tala1-tala2
        summa = 0
        #Ef mismunur milli talnanna er meiri en 1 hefst liðurinn
        if abs(mismunur) > 1:
            #Ef tala 1 er minni en tala 2
            if tala1 < tala2:
                #Set breytuna summu sem 0

                #Keyri lúppu frá tölu 1 að tölu 2 (tala 2 meðtalin)
                for x in range(tala1, tala2 + 1):
                    #Meðan talan er minni en tala2
                    if x < tala2:
                        #Prenta ég töluna með tvíkommu á milli
                        print(x, end=";")
                    #Síðasta talan kemur hérna án tvíkommu
                    else:
                        print(x)
                #Hérna reikna ég summu talnanna og keyri lúppu frá tölu 1 að tölu 2 (með tölu 2)
                for x in range(tala1, tala2 + 1):
                    #Hérna nota ég summu breytuna sem ég setti áðan
                    #og plúsa hverja tölu saman við summuna
                    summa = summa + x
                #Prenta niðurstöðuna
                print("Samanlögð summa allra talnanna er:", summa)

            #Ef seinni talan er minni en fyrri talan:
            elif tala2 < tala1:
                #Keyri nákvæmlega sama með smá breytingu
                for x in range(tala2, tala1 + 1):
                    if x < tala1:
                        print(x, end=";")
                    else:
                        print(x)
                #Hérna plúsa ég saman eins og að ofan
                for x in range(tala2, tala1 + 1):
                    summa = summa + x
                print("Samanlögð summa allra talnanna er:", summa)
        #Ef bilið milli talnanna er ekki meira en 1 keyrir þetta
        else:
            print("Það er ekki nægjanlegt bil milli talnanna")
    # Hér hefst liður 2 úr verkefninu
    elif val == 2:
        #Keyri lúppu frá tölunni 100 - 200
        for x in range(100,200+1):
            #Ef talan er deilanleg með 4 og 5 prentast skilaboðin
            if x % 4 == 0 and x % 5 == 0:
                print("Jiu-Jitzu")
            #Ef talan er ekki deilanleg með 4 og 5 prentast talan
            elif x % 4 == 1 and x % 5 == 1:
                print(x)
            #Ef talan er deilanleg með 4 prentast skilaboðin
            elif x % 4 == 0:
                print("Júdó")
            #Ef talan er deilanleg með 5 prentast skilaboðin
            elif x % 5 == 0:
                print("Kung-Fu")
            #Allar aðrar tölur prentast
            else:
                print(x)
    # Hér hefst liður 3 úr verkefninu
    elif val == 3:
        #spyr notandann hversu oft hann vill woohoo
        wohoo = int(input("Hversu oft viltu að orðið woohoo prentist út?"))
        #Set lúppu sem keyrir eins oft og notandinn vildi
        for x in range(wohoo):
            #Ef lúppan keyrist einu sinni (0) prentast eitt woohoo
            if x == 0:
                print("wohoo")
            #Ef lúppan keyrir oftar þá prentast woohoo-woohoo eins oft og lúppan keyrir
            else:
                print("wohoo",end="")
                print("-wohoo" * x)

    # Hér hefst liður 4 úr verkefninu
    elif val == 4:
        #Bið notanda að slá inn textastreng
        strengur = input("Sláðu inn textastreng")
        """
        #keyri lúppu sem gefur mer hvern staf
        for x in range(len(strengur)):
            #Prenta strenginn og sleppi fyrsta og síðasta
            print(strengur[x:-x])
            #Stoppa lúppunna þegar 1 stafur er eftir
            if len(strengur[x:-x]) == 1:
                break
        """
        # keyri lúppu sem gefur mer hvern staf
        for x in range(len(strengur)):
            # Prenta strenginn og sleppi fyrsta og síðasta
            print(strengur[x+1:len(strengur)-(x+1)])
            # Stoppa lúppunna þegar 1 stafur er eftir
            if len(strengur[x+1:len(strengur)-(x+1)]) == 1:
                break



    # Hér hefst liður 5 úr verkefninu
    elif val == 5:
        #Bið notanda um heiltölu
        heiltala = int(input("Sláðu inn heiltölu"))
        #Set breytuna fyrir margfeldið
        margfeldi = 1
        #Læt lúppu keyra frá valdri tölu og niður að 0(-1 þýðir að talið er niður)
        for x in range(heiltala,0,-1):
            #Margfalda frá fyrstu tölu og niður að einum
            margfeldi = margfeldi * x
            #Til að prentast í einni línu geri ég þessa kóða
            #Þegar talan er komin niður að 1 þá kemur samasem merki
            if x == 1:
                print(x,end="=")
                print(margfeldi)
            #Prenta út hverja tölu með stjörnu á milli
            else:
                print(x,end="*")


    # Hér hefst liður 6 úr verkefninu
    elif val == 6:
        #Bið notanda um streng
        strengur = input("Sláðu inn streng")
        #Set teljara fyrir tölu og bókstafi
        teljaritolur = 0
        teljaribokstafur = 0
        #Les yfir hvern staf/tölu með for lúppunni
        for x in strengur:
            #Ef stafur/tala er tala hækkar teljari fyrir tölur um 1
            if x.isdigit():
                teljaritolur = teljaritolur + 1
            #Ef stafur/tala er bókstafur hækkar teljari fyrir bókstafi um 1
            if x.isalpha():
                teljaribokstafur = teljaribokstafur + 1
        #Prenta út hvað margar tölur og bókstafir eru
        print("Það eru",teljaritolur,"tölur í strengnum")
        print("Það eru",teljaribokstafur,"bókstafir í textanum")

    # Hér hefst liður 7 úr verkefninu
    elif val == 7:
        #Bið notanda um streng
        strengur = input("Sláðu inn streng til að athuga hvort hann sé samhverfur")
        #set breytuna casefold sem gerir alla bókstafi litla sama hvað
        strengurfram = strengur.casefold()
        #Set strenginn afturábak inn í breytu
        strengurbak = strengur[::-1]

        #Ef strengirnir er eins fram og aftur þá er hann samhverfur
        if strengurfram == strengurbak:
            print("Strengurinn er samhverfur")
        #Ef hann er ekki eins fram og aftur þá er hann ekki samhverfur
        else:
            print("strengurinn er ekki samhverfur")
    # Hér hefst liður 8 úr verkefninu
    elif val == 8:
        #Bið notanda um 2 orð
        strengur1 = input("Sláðu inn orð 1")
        strengur2 = input("Sláðu inn orð 2")

        #Næ í fyrstu tvo stafina i báðum orðunum og set í bútabreytu
        butur1 = strengur1[:2]
        butur2 = strengur2[:2]
        #Næ í síðustu tvo stafinu í breytu og set í bútabreytu
        butur3 = strengur1[-2::]
        butur4 = strengur2[-2::]
        #Set alla bútana í breytu
        ordarugl = butur1 + butur2 + butur3 + butur4
        #Prenta orðaruglið
        print("Orðaruglið er:",ordarugl)
        #Set orðaruglið í CAPS
        hastafir = ordarugl.upper()
        print("Allt stórir stafir:",hastafir)
        #Set orðaruglið í lástafi
        lastafir = ordarugl.lower()
        print("Allt litlir stafir",lastafir)
        #Næ í lengd strengjanna tveggja og set í breytu
        lengd = len(strengur1)
        lengd2 = len(strengur2)
        #Plúsa lengdirnir saman í eina breytu
        lengd3 = lengd + lengd2
        #Prenta úr lengd strengjanna tveggja
        print("lengd strengjanna er", lengd3,"stafir")
    # Hér hefst liður 9 úr verkefninu
    elif val == 9:
        #Bið notanda um að slá inn nafnið sitt
        nafn = input("Sláðu inn nafn")

        #keyri lúppu staf fyrir staf / tölu fyrir tölu
        for x in range(len(nafn)):
            #Prenta út
            print(nafn[x:])

    # Hér hefst liður 10 úr verkefninu
    elif val == 10:
        #Geri breytu sem er sönn
        true = True
        #Set teljara sem telur hversu oft valmyndin er keyrð
        keyrsla = 0
        #Set lúppu sem keyrir meðan hún er sönn
        while true == True:
            #Prenta út valmynd
            print("1. 10 Tölur")
            print("2. jöfn tala oddatala")
            print("3. Hætta")
            #Leið og valmyndin er keyrð hækkar teljarinn um einn
            keyrsla = keyrsla + 1
            #Bið notanda um að velja hvað hann vill gera
            val = input("Veldu hvað þú vilt gera")

            #Ef valið hans er 1 þá keyrist þessi kóði
            if val == "1":
                #Byrjum á að setja teljara og summu breytu
                teljari = 0
                summa = 0
                #Meðan teljarinn er minni en 11 (gengur 10 sinnum)
                while teljari < 11:
                    #Fæ 10 tölur frá notanda
                    tala = int(input("Sláðu inn 10 tölur"))
                    #Bæti hverri tölu inn í summu breytuna
                    summa = tala + summa
                    #Í hvert skipti sem lúppan keyrir hækkar teljarinn um 1
                    teljari = teljari + 1

                #Reiknum meðaltal talnanna en það fáum við með að deila summuna við 10
                medaltal = summa / 10
                #Prentum niðurstöðurnar
                print("Summa talnanna er",summa)
                print("Meðaltal talnanna er",medaltal)

            #Ef valið hans er 2 þá keyrist þessi kóði
            elif val == "2":
                #Bið notanda að slá inn tölu
                tala = int(input("Sláðu inn tölu til að vita hvort sé oddatala eða slétt tala"))
                #Ef talan gefur engan afgang þegar deilt er með 2 þá er það slétt tala
                if tala % 2 == 0:
                    print("þetta er slétt tala")
                #Allar aðrar tölur eru þá væntanlega oddatala
                else:
                    print("Þetta er oddatala")

            #Ef valið hans er 3 þá látum við lúppuna hætta og keyra þennan kóða
            elif val == "3":
                #Hérna hættir fullyrðingin að ofan að vera sönn og lúppan brotnar
                true = False
                #Setjum teljara því við viljum að ég sé frábær forritari prentast út 10 sinnum
                teljari2 = 1
                while teljari2 < 11:
                    print("Ég er frábær forritari")
                    teljari2 = teljari2 + 1
                #Segjum notandanum hversu oft valmyndin var keyrð
                print("valmyndin var keyrð", keyrsla, "sinnum")



            else:
                print("Valdir ekki rétt")



    elif val == 11:
        on = False
    else:
        print("þú hefur ekki valið rétt")

print("Takk fyrir að nota forritið mitt")