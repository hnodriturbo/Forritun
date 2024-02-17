#Hreiðar Pétursson
#13.02.2023
#Skilaverkefni 4

import math
import random
#Set satt gildi
on = True
#Meðan on er satt
while on == True:
    #Fæst þessi valmynd
    print("1. Random Tölur")
    print("2. Talnabil")
    print("3. Strengjalisti")
    print("4. Samanburður")
    print("5. Hætta")
    #Bið notanda að velja hvað hann vill gera
    val = int(input("Hvað viltu gera?"))
    if val == 1: #Liður 1 - Random Tölur
        #Bý til tóman lista
        listi = []
        #Keyri lúppu 30 sinnum
        for x in range(30):
            #hvert skipti sem lúppan keyrir setur það random tölu í breytu
            tala = random.randint(10,40)
            #og bætir henni við listann
            listi.append(tala)

        #Prenta út listann með bandstrik á milli talnanna
        print("Hérna er talnalistinn minn")
        for x in range(len(listi)):#Keyri lúppu í gegnum lengd listans
            if x == len(listi) -1:#Ef síðasta gildið finnst
                print(listi[x])#Prentast það gildi stakt
            else:#allar aðrar tölur prentast annars út með bandstrik á eftir sér
                print(listi[x],"-",sep="",end="")
        print("Hérna er listinn minn raðaður")
        #Prenta út listann raðaðan
        listi.sort() #sortera listann
        print(listi) #Prenta listann

        #Leggja allar oddatölur listans saman
        oddatolurlisti = []# Set tómann lista
        summa = 0#set töluna 0 í breytu
        for x in listi:#Keyri lúppuna í gegnum listann
            if x % 2 == 1:# Ef talan á listanum skilar afgangi ef deilt er með 2
                oddatolurlisti.append(x)#Set ég þá tölu í annan oddatölulista
        for x in oddatolurlisti:#Keyri í gegnum oddatölulistann
            summa = summa + x#Set hverja tölu inn í summu breytuna
        print("Summa allra oddatalna í listanum er:",summa)#Prenta út summu talnanna

        #Telja hversu margar sléttar tölur eru í listanum
        teljari = 0#Byrja á að setja teljara
        for x in listi:#Keyri lúppu í gegnum listann
            if x % 2 == 0:#Ef gildi í listanum skilar engum afgangi deilt með 2
                teljari = teljari + 1#Hækkar teljari um einn
        print("Það eru",teljari,"sléttar tölur í listanum")#Svo prenta ég út niðurstöðuna
        #Sýna lægstu tölu listans
        laegstatala = min(listi)#Finn lægstu töluna og set hana í breytu
        print("Lægsta tala listans er",laegstatala)#Prenta út lægstu töluna
        print()#Set inn eina auka línu svo verkefnið líti betur út

    elif val == 2: #Liður 2 Talnabil
        nyrlisti = []#Geri tóman lista
        for x in range(2000,3200):#Keyri lúppu frá tölunni 2000 og upp í 3200
            if x % 7 == 0 and x % 5 == 1:#Ef talan er deilannleg með 7 og ekki deilanleg með 5
                nyrlisti.append(x)#Fer sú tala í nýjan lista
        print(nyrlisti)#Prenta út nýja listann
        summa = 0#Set summu í breytu
        for x in nyrlisti:#Keyri lúppu í gegnum nýja listann
            summa = summa + x#Plúsa hverja tölu við summuna
        print("Summa allra talnnanna í listanum er:",summa)#Prenta út summuna

    elif val == 3: #Liður 3 - Strengjalisti
        listi = []#Bý til tóman lista
        for x in range(10):#Keyri lúppu tíu sinnum
            ord = input("Sláðu inn 10 strengi")#Bið notanda um orð í hvert skipti
            listi.append(ord)#Bæti því orði við listann
        #Byrja á að búa til valmynd með while lykkju
        gull = True#Setjum gildi sem er satt
        while gull == True:#meðan gildið er satt  keyrist þessi lykkja (valmynd)
            print("1. Finna fjölda orða sem eru aðeins 4 stafir")
            print("2. Skrifa annað hvert orð út öfugt")
            print("3. Skrifa listann út raðaðan")
            print("4. Eyða orðum út sem byrja á ákveðnum staf")
            print("5. Skrifa út listann aftur")
            print("6. Hætta")
            val = int(input("Veldu númer hvað þú vilt gera"))

            if val == 1: #Finna fjölda orða sem eru aðeins 4 stafir
                #Byrja á að setja teljara
                teljari4stafir = 0
                #Keyri lúppu í gegnum listann
                for x in listi:
                    #Ef lengd orðs á listanum er samasem 4 stafir
                    if len(x) == 4:
                        #Hækka ég teljarann um einn
                        teljari4stafir = teljari4stafir + 1
                        print("Orðið",x,"fannst")
                #Prenta svo út hvað það eru mörg orð aðeins með 4 stöfum
                print("Það eru",teljari4stafir,"fjögurra stafa orð í listanum")

            elif val == 2:#Skrifa annaðhvert orð út öfugt
                #Byrja á að gera tóman lista
                nyrlisti = []
                #Fer í gegnum listann í tölum
                for x in range(len(listi)):
                    #Ef talan er deilanleg með 2 þá bæti ég x í nýjan lista
                    if x % 2 == 0:
                        nyrlisti.append(listi[x])
                #Fer í gegnum nýja listann sem ég var að búa til
                for x in nyrlisti:
                    #Prenta út hvert gildi listans afturábak
                    print(x[::-1])

            elif val == 3: #Skrifa út listann raðaðan
                listi.sort()
                print(listi)

            elif val == 4: #Eyða orðum sem byrja á ákveðnum staf
                #Byrjum á að setja teljara
                teljarinofn = 0
                #Bið notanda um hvaða stað hann vill að nöfnin sem á að eyða  byrji á
                eyda = input("Sláðu inn staf og nöfnum sem byrja á þeim staf verður eytt")
                listi5 = []
                #Keyri lúppu í gegnum listann
                for x in listi:
                    #Finn fyrsta stafinn og ef hann er sami og valið var
                    if x[0:1] == eyda:
                        #þá set ég það nafn inn í nýjan lista
                        listi5.append(x)
                #Keyri aðra lúppu í gegnum nýja listann
                for x in listi5:
                    #Öll nöfn sem eru sömu og inná nýja listanum eru eytt út af gamla
                    listi.remove(x)
                    #og prenta svo að nafninu hafi verið eytt út
                    print("Nafnið",x,"var eytt út af listanum")
                    #Hækkum teljarann um einn
                    teljarinofn = teljarinofn + 1
                #Prenta hvað mörgun nöfnum var eytt út
                print(teljarinofn,"nöfnum var eytt út af listanum")

            elif val == 5:#Skrifa út listann aftur
                print(listi)

            elif val == 6:
                gull = False

    elif val == 4: #Samanburður
        listi1 = []#Geri tóman lista
        listi2 = []#Geri tóman lista
        #Byrja á að láta for lúppu biðja um bæði 7 og 6 orð til að setja í sitthvoran listann
        for x in range(7):
            ord1 = input("Sláðu inn 7 orð")
            listi1.append(ord1)
        for x in range(6):
            ord2 = input("Sláðu inn 6 orð")
            listi2.append(ord2)
        #Keyri for lúppu til að renna í gegnum listann
        for x in listi1:
            #Keyri svo aðra for lúppu inn í henni sem keyrir á sama tíma
            for i in listi2:
                #Ef nafnið á lista 1 er það sama og í lista 2 þá koma skilaboð
                if x == i:
                    print("Sama orðið fannst og það er:",x)

    elif val == 5:#Hætta valmöguleikinn
        #Gildið gert falskt
        on = False
    else:#Ef ekki er valið rétt koma þessi skilaboð
        print("þú hefur ekki valið rétt")
#Þegar notandi er búinn og kominn úr lúppunni keyrast þessi skilaboð
print("Takk fyrir að nota forritið mitt")
tala = random.randrange(1,50)
listi = [random.randrange(1,20) for i in range(200) if i % 2 == 0]
print(listi)
def tala(*tala):

    tala = min(tala)
    return "minnsta talan er",tala
print(tala(5,4,3,2,1,0))