#Hreiðar Pétursson
#Skilaverkefni 2 - taka 2
#20 jan 2023

on = True

while on == True:

    print("1. Heiltala")
    print("2. Flatarmál")
    print("3. Leyniorð")
    print("4. Fimm heiltölur")
    print("5. Hlaupaár")
    print("6. Hlaup")
    print("7. Körfuboltaæfing")
    print("8. Tími")
    print("9. Millilítrar")
    print("10. Margföldun")
    print("11. Hætta")

    val = int(input("Hvað viltu gera?"))

    #Heiltala
    if val == 1:
        heiltala = int(input("Sláðu inn heiltölu"))
        print("Þú slóst inn töluna",heiltala,"!!!")

    #Flatarmál
    elif val == 2:
        lengd = int(input("Sláðu inn lengd fernings:"))
        breidd = int(input("Sláðu inn breidd fernings"))

        flatarmal = lengd * breidd

        print("Flatarmál ferningsins er",flatarmal,"!!!")

    #Leyniorð
    elif val == 3:
        leyniord = "password"
        leyniord2 = input("Sláðu inn lykilorðið:")

        while leyniord2 != leyniord:
            print("Ekki rétt lykilorð")
            leyniord2 = input("Sláðu aftur inn lykilorðið:")

        print("Rétt lykilorð")

    #Fimm heiltölur
    elif val == 4:
        teljari = 1
        summa = 0

        while teljari < 6:
            tala = float(input("Sláðu inn heiltölu"))
            teljari = teljari + 1
            summa = summa + tala
        medaltal = summa / 5
        print("Meðaltal talnanna er:",round(medaltal,2))

    #Hlaupaár
    elif val == 5:
        hlaupaar = int(input("Sláðu inn ártal til að vita hvort sé hlaupaár eða ekki:"))

        if hlaupaar % 4 == 1 or hlaupaar % 400 == 0:
            print("þetta er ekki hlaupaar")
        elif hlaupaar % 4 == 0 or hlaupaar % 400 == 1:
            print("þetta er hlaupaár")



    #Hlaupahringir og metrar
    elif val == 6:
        metrar = int(input("sláðu hvað þú hljópst marga metra:"))
        hringir = metrar // 400
        afghringir = metrar % 400

        print("Þú hljópst",hringir,"hringi og",afghringir,"metra")

    #Körfuboltaæfing
    elif val == 7:
        leikmenn = int(input("Sláðu hvað margir ætla að spila"))
        lid = int(input("Sláðu inn hvað mörg lið eiga að vera"))

        lidaskipting1 = leikmenn // lid
        lidaskipting2 = leikmenn % lid

        print("Það verða",lidaskipting1,"margir í hverju liði og",lidaskipting2,"margir varamenn")

    #
    elif val == 8:
        timi = int(input("Sláðu inn hvað margar sekóntur"))

        solarhringur = timi // 86400
        afgsolahringur = timi % 86400

        klst = afgsolahringur // 3600
        afgklst = afgsolahringur % 3600

        min = afgklst // 60
        afgmin = afgklst % 60

        print("þetta eru",solarhringur,"sólarhringir og",klst,"klst og",min,"mínótur og",afgmin,"sekóntur")

    elif val == 9:
        #Bið notanda að slá inn hvað marga millilítra hann hefur
        ml = int(input("Sláðu inn millilítra:"))

        #nota heiltöludeilingu til að sjá hvað margir lítrar eru
        litrar = ml // 1000
        #Set afganginn í breytu
        afglitrar = ml % 1000

        #athuga hvað marga desilítra afgangurinn hefur að geyma
        desilitrar = afglitrar // 100
        #Set afganginn af því inn í breytu
        afgdesilitrar = afglitrar % 100

        #athuga hvað marga sentilítra afgangurinn hefur að geyma
        sentilitrar = afgdesilitrar // 10
        #set afganginn inn í breytu
        afgsentilitrar = afgdesilitrar % 10

        #Prenta niðurstöðuna
        print("Þetta eru",litrar,"lítrar og",desilitrar,"desilítrar og",sentilitrar,"sentilítrar og",afgsentilitrar,"millilítrar")

    elif val == 10:
        heiltala = int(input("Sláðu inn heiltölu"))
        margfeldi = 1

        while heiltala > 0:
            margfeldi = margfeldi * heiltala
            heiltala = heiltala - 1
        print(margfeldi)






    elif val == 11:
        on = False

    else:
        print("þú hefur ekki valið rétt")

