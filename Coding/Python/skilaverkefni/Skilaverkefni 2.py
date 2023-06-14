#Hreiðar Pétursson
#Skilaverkefni 2
#17 janúar

#Geri valmynd að notandinn getur valið hvaða hluta hann vill keyra hverju sinni
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

    val = int(input("hvað viltu gera?"))

#Heiltala
    if val == 1:
       #Bið notanda um heiltölu
       heiltala = int(input("Sláðu inn heiltölu:"))
       #Prenta út heiltöluna
       print("Þú hefur valið töluna",heiltala,"!!!")

#Flatarmál fernings
    elif val == 2:
        #Bið notanda að slá inn breidd fernings
        breidd = int(input("Sláðu inn breidd fernings:"))
        #Bið notanda að slá inn lengd fernings
        lengd = int(input("Sláðu inn lengd fernings:"))
        #Reikna út flatarmálið með að margfalda breiddina og lengdina sem notandinn sló inn
        flatarmal = breidd * lengd
        #Prenta út niðurstöðuna
        print("Flatarmál ferningsins er:",flatarmal,"!!!")

#Lykilorð
    elif val == 3:
        #set lykilorðið inn í breytu
        leyniord = "Password"
        #Bið notanda um að slá inn lykilorðið
        leyniord2 = input("Sláðu inn leyniorð")

        #meðan lykilorðið er ekki sama og rétt lykilorð prenta ég rangt lykilorð
        while leyniord2 != leyniord:
            print("Rangt lykilorð reyndu aftur")
            #hér læt ég lúppuna biðja aftur um lykilorðið
            leyniord2 = input("Sláðu inn lykilorðið aftur")
        #ef lykilorðið er rétt slegið inn kemur rétt lykilorð
        print("Rétt lykilorð")

#Fimm heiltölur
    elif val == 4:
        #Byrjum á að setja teljara fyrir lúppuna
        teljari = 1
        #Byrja á að setja summu í breytu
        summa = 0
        #Byrja á lúppunni
        while teljari < 6:
            #bið notanda um tölu
            tala = int(input("Sláðu inn heiltölu"))
            #plúsa saman summuna og töluna svo input telji
            summa = summa + tala
            #læt lúppuna plúsa einn við í hvert skipti
            teljari = teljari + 1
        #Geri nýja breytu til að reikna medaltal
        medaltal = summa / 5
        #prenta meðaltalið utan lúppunnar
        print("meðaltalið er:",medaltal)

#Hlaupaár
    elif val == 5:
        #Bið notanda um að slá inn ár
        artal = int(input("Sláðu inn ár til að athuga hvort það sé hlaupa ár"))
        #Ef ártal er deilanlegt með 4 og niðurstaða gengur ekki upp í 100
        #Þá er það hlaupa ár
        if artal % 4 == 0 and artal % 100 != 0:
            print("þetta er hlaupaár")
        #ef ártal er deilanlegt með 400 þá er það líka hláupár
        elif artal % 400 == 0:
            print("þetta er hlaupaár")
        #Annars er það ekki hlaupaár
        else:
            print("Þetta er ekki hlaupaár")

#Hlaup
    elif val == 6:
        #bið notanda um slá hversu marga metra hann hljóp
        hlaup = int(input("Sláðu inn hvað þú hljópst marga metra:"))

        #nota heiltölu deilingu til að sjá hvað marga 400 metra hringi hann hljóp
        hringir = hlaup // 400
        #nota afgang af deilingunni til að sjá hvað margir metrar eru afgangs
        metrar = hlaup % 400
        #Prenta út niðurstöðuna
        print("þú hljópst",hringir,"hringi og",metrar,"metra")

#Körfuboltaæfing
    elif val == 7:
        #Bið not   anda að slá inn hversu margir leikmenn eru og lið
        spilarar = int(input("Sláðu inn hvað margir eru að spila"))
        lid = int(input("Sláðu inn hvað það eiga að vera mörg lið"))

        #Nota heiltöludeilingu til að sjá hversu mörg lið verða
        lidaskipting = spilarar // lid
        #nota afganginn til að sjá hversu margir leikmenn yrðu varamenn
        afgangsleikmenn = spilarar % lid
        #Prenta niðurstöðuna
        print("Liðaskiptingin er",lidaskipting,"og það verða",afgangsleikmenn,"varamenn")

#Tími
    elif val == 8:
        #bið notanda um að slá inn sekóntur
        sek = int(input("Sláðu inn hvað margar sekóntur:"))
        #nota heiltöludeilingu til að sjá hversu margir dagar sekónturnar eru
        solarhringur = sek // 86400
        #bý til breytu fyrir afganginn af sekóntunum
        afgsolarhringur = sek % 86400

        #athuga hvað margar klst afgangurinn hefur að geyma
        klst = afgsolarhringur // 3600
        #set afganginn inn í breytu
        afgklst = afgsolarhringur % 3600

        #athuga hvað margar mínótur afgangurinn hefur að geyma
        min = afgklst // 60
        #Set afganginn inn í breytu
        afgmin = afgklst % 60

        #Prenta niðurstöðuna
        print("þetta eru",solarhringur,"dagar og",klst,"klst og",min,"mínótur og",afgmin,"sekóntur")

#Millilítrar
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


#Margföldun
    elif val == 10:

        #byrja á að biðija notanda að slá inn tölu
        heiltala = int(input("Sláðu inn heiltölu"))
        #geri breytu fyrir margfeldið
        margfeldi = 1

        #meðan talan er stærri en 0
        while heiltala > 0:
            #margfalda breytuna með heiltölunni sem notandinn sló inn
            margfeldi = margfeldi * heiltala
            #læt teljarann telja niður um einn í hvert skipti
            heiltala = heiltala - 1
        #Prenta niðurstöðuna einu sinni með því að prenta utan lúppunnar
        print("margfeldið er",margfeldi)


    elif val == 11:
        on = False
    else:
        print("Þú hefur ekki valið rétt")