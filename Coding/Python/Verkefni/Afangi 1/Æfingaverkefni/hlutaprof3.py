#Hreiðar Pétursson
#2 febrúar 2023
#æfing fyrir hlutapróf 3
#hangman og fleira skemmtilegt !!!

import random
import math


on = True

while on == True:

    print("1. Jöfn tala eða oddatala")
    print("2. Orðaleikur")
    print("3. Fjöldi Talna")
    print("4. Samanburður")
    print("5. Hangman")
    print("6. Hætta")


    val = int(input("Hvað viltu gera?"))

    if val == 1:
        tala = int(input("Sláðu inn tölu"))

        for x in range(0,tala+1):
            if x % 2 == 0:
                print(x,"= Jöfn")
            else:
                print(x,"= oddatala")

    elif val == 2:
        tala = int(input("Sláðu inn tölu"))

        if tala % 3 == 0 and tala % 5 == 0:
            print("FIZZ-BUZZ")
        elif tala % 3 == 0:
            print("FIZZ")
        elif tala % 5 == 0:
            print("BUZZ")

    elif val == 3:
        tala = int(input("Sláðu inn tölu"))

        tala = str(tala)
        lengdtolu = len(tala)

        print("Það eru",lengdtolu,"tölustafir í þessari tölu")


    elif val == 4:
        strengur1 = input("Sláðu inn streng 1")
        strengur2 = input("sláðu inn streng 2")

        true = False

        sidustu2strengur1 = strengur1[-2:]
        sidustu2strengur2 = strengur2[-2:]

        if sidustu2strengur1 == sidustu2strengur2:
            true = True

        if true == False:
            print("Siðustu tveir stafirnir eru ekki eins")
        if true == True:
            print("Síðustu tveir stafirnir eru eins")

    elif val == 5:
        true = True

        listiord = ["esjan","reykjavík","akureyri","ís","hreiðar"]
        teljarigisk = 0
        giskadirstafir = []
        validord = random.choice(listiord)
        print("Velkominn í Hangman leikinn minn")
        print("Tölvan hefur valið eitt orð sem þér ber að giska á")
        print("Þú færð 12 tilraunir til að giska á rétt orð")
        while true == True:
            gisk = input("Veldu hvaða staf þú vilt giska á")
            if gisk in validord:
                print("Þú hittir á réttan staf")
                if gisk not in giskadirstafir:
                    giskadirstafir.append(gisk)
            elif gisk in giskadirstafir:
                print("Þú ert nú þegar búinn að velja þennan staf")
            elif teljarigisk == 12:
                print("Þú tapaðir leiknum!!!")
                break
            else:
                if gisk not in giskadirstafir:
                    giskadirstafir.append(gisk)
                    teljarigisk = teljarigisk + 1
            print("Þú ert búinn að giska á", giskadirstafir)
            print("Þú ert búinn að giska",teljarigisk,"sinnum rangt")

            sigur = True
            for x in validord:
                if x in giskadirstafir:
                    print(x,end="")
                else:
                    print("-",end="")
                    sigur = False
            print()
            if sigur == True:
                print("Þú vannst leikinn til hamingju !!!")
                break
            print()











    elif val == 6:
        on = False
    else:
        print("þú hefur ekki valið rétt")

print("Takk fyrir að nota forritið mitt")