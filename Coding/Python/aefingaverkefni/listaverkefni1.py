#Hreiðar Pétursson
#1 febrúar
#Lista verkefni

import math
import random

on = True

while on == True:
    print("Velkominn í forritið mitt. Veldu hvað þú vilt gera")
    print("1. Innkaupalisti")
    print("2. Random tölur")
    print("3. Fyrsta og síðasta")
    print("4. Nemendur")
    print("5. Hætta")

    val = int(input("hvað viltu gera?"))

    if val == 1:

        ok = True
        list = []
        while ok == True:
            print("Skrifaðu hætta til að hætta og prenta út listann í stafrófsröð")
            hlutur = input("Hverju vilta bæta við á listann?")

            if hlutur == "hætta":
                break

            list.append(hlutur)

        print("Takk fyrir að bæta á listann")

        #for x in list:
        #    if "hætta" in list:
        #        list.remove("hætta")



        print("þú valdir kaupa inn")
        list.sort()
        print(list)


    elif val == 2:
        #Bý til tóman lista
        list = []

        #Hérna raða ég 15 tölum inn í listann á bilinu 5 og 25
        for x in range(15):
            list.append(random.randint(5,25))

        #Hérna raða ég listanum niður
        list.sort()
        print(list)

        #Hérna finn ég út hvaða gildi í listanum er hæðst og lægst
        maxtala = max(list)
        print(maxtala)
        mintala = min(list)
        print(mintala)

        #Hérna skrifa ég út summu allra gilda í listanum
        summa = 0

        for i in list:
            summa = summa + i
        print(summa)

        #Hérna skrifa ég út lengd listans
        lengd = len(list)
        print(lengd)



    elif val == 3:
        #Byrja á að búa til tóman lista
        list = []
        list2 = []
        list3 = []

        #Héra bið ég um 20 tölur og set þær inn í lista 1
        for x in range(20):
            list.append(random.randint(1,100))

        print(list)

        #Hérna finn ég fyrsta og síðasta stakið og set það inn í breytu
        fyrstastak = list[0]
        seinnastak = list[-1]

        #Herna set ég fyrsta og síðasta stakið inn í lista 2 og 3
        list2.append(fyrstastak)
        list3.append(seinnastak)
        print(list2)
        print(list3)


    elif val == 4:

        #Byrja á að búa til tóman lista og teljara
        list = []
        teljari = 0

        #Læt while lykkju ganga 10 sinnum
        while teljari < 11:
            #Bið notanda um nafn
            nafn = input("Sláðu inn nafn")

            #Ef nefnið er þegar komið á listann
            if nafn in list:
                print("ekki má setja sama nafn tvisvar")

            #ef nafnið er ekki þegar á listanum þá bæti ég því við listann
            else:
                list.append(nafn)

            #Læt teljarann telja
            teljari = teljari + 1


        #Hérna prenta ég listann út öfugan
        list.reverse()
        print(list)


    elif val == 5:
        on = False

    else:
        print("valdir vitlaust")

print("Takk fyrir að nota forritið mitt")