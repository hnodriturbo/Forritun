# Hreiðar Pétursson
# 16janúar
# While æfingaverkefni rallý
import random
on = True
#Valmyndin mín
while on == True:
    # Menuið mitt
    print("1. Lítrar eða gallon")
    print("2. Hraðatakmörk")
    print("3. Veldisreikningur")
    print("4. Teningakast")
    print("5. Listar")
    print("6. Talnadictionary")
    print("7. Einkunnir")
    print("8. Spurningar")
    print("9. Hætta")


    val = int(input("Hvað viltu gera?"))

    if val == 1:
        #Fall sem breytir gallon í lítra og skilar með 2 aukastöfum
        def gallon_i_litra(g):
            litrar = g * 3.78541
            roundedlitrar = "{:.2f}".format(litrar)
            return roundedlitrar
        #Fall sem breytir lítrum í gallon og skilar með 2 aukastöfum
        def litrar_i_gallon(l):
            gallon = l * 0.264172
            roundedgallon = "{:.2f}".format(gallon)
            return roundedgallon
        #Bið notanda um að segja mér magn sem hann vill breyta og skila þá fallinu
        g = int(input("Hversu mörgum gallon viltu breyta í lítra?"))
        print(gallon_i_litra(g))
        l = int(input("Hversu mörgum lítrum viltu breyta í gallon?"))
        print(litrar_i_gallon(l))

    elif val == 2:
        #Bý vill fall sem tekur inn hraða frá notanda
        def hversuhratt(hradi):
            if hradi <= 30:
                print("Ókídókí")
            #Hérna reikna ég út refsistig ef hraði er yfir 30
            elif hradi > 30:
                reikn = hradi - 30
                reikn2 = reikn / 5
                refsistig = reikn2 * 3
                roundrefsistig = "{:.0f}".format(refsistig)
                print("Refsistig =",roundrefsistig)
                if refsistig > 8:
                    print("Þú missir ökuskírteinið")
            else:
                return "Ekki rétt færibreyta"
        #Eftir því hvað hraðinn er mikill koma mismunandi skilaboð
        hradi = int(input("hversu hratt ókstu?"))
        hversuhratt(hradi)

    elif val == 3:
        #Fall sem tekur inn tvær tölur þar sem seinni er veldi af þeirri fyrri
        def Veldi(tala,veldi):
            #Eingöngu jákvæðar heiltölur leyfðar
            if tala >= 0:
                summa = 0
                summa = tala ** veldi
                #keyri margföldun eins oft og seinni talan er(veldið)
                for x in range(veldi):
                    #Prent út útreikninginn sjálfann og skila summu
                    if x == range(veldi)[-1]:
                        print(tala,"=",summa,end="",sep="")
                    else:
                        print(tala,end="*")
            else:
                print("Tek eingöngu við jákvæðum heiltölum")
        #Notandi velur hvaða tölur hann vill setja reikniformúluna
        tala = int(input("Sláðu inn tölu"))
        veldi = int(input("Sláðu inn veldi"))
        Veldi(tala,veldi)
        print()

    elif val == 4:
        #Fall sem skila summu teningakasts eftir því hvað notandinn vill
        #kasta teningnum oft. Reikna köstin og svarið með for lúppu.
        def kasta(oft):
            summa = 0
            for x in range(oft):
                tala = random.randint(1,6)
                summa = summa + tala
            return summa
        oft = int(input("Hversu oft viltu kasta teningnum"))
        print(kasta(oft))

    elif val == 5:
        #Fall sem á að skila öllum tölum sem enda á 2 úr tveim listum
        listi1 = [random.randint(0, 200) for x in range(200)]
        listi2 = [random.randint(0, 200) for x in range(200)]
        def eins(listi1, listi2):
            nyrlisti = []
            #Nota for lúppu sem breytir hverri tölu yfir í streng og
            #athugar hvort hann endi á tölunni 2 og ef svo þá setur
            #lúppan þá tölu í sér lista sem prentast svo út í lokin
            for x in listi1:
                if str(x)[-1] == "2":
                    nyrlisti.append(x)
            for x in listi2:
                if str(x)[-1] == "2":
                    nyrlisti.append(x)
            return nyrlisti
        print(eins(listi1,listi2))

    elif val == 6: # Talnadictionary
        dict1 = {"stólar":10,"borð":20,"myndir":2}
        dict2 = {"stólar":11,"borð":70,"myndir":80}
        dict3 = {}
        #Keyri for lúppu sem bætir öllum atriðum úr dict1 í dict3
        for key, value in dict1.items():
            dict3[key] = value
        #Þessi lúppa plúsar value saman ef það finnur key sem er alveg eins
        for key, value in dict2.items():
            if key in dict3:
                dict3[key] += value
        #Prenta út niðurstöðuna
        print(dict3)

    elif val == 7: #Dictionary innan dictionary
        nemadict = {"Jón Hallsson": {"STÆR": 7, "ENSK": 5, "FORR": 10, "VERS": 8},
                    "Hallur Halldórsson": {"STÆR": 2, "ENSK": 8, "FORR": 9, "VERS": 9},
                    "Dísa Jónsdóttir": {"STÆR": 3, "ENSK": 7, "FORR": 5, "VERS": 6},
                    "Anna Eiríksdóttir": {"STÆR": 10, "ENSK": 6, "FORR": 1, "VERS": 7},
                    "Kristín Vilhjálmsdóttir": {"STÆR": 9, "ENSK": 5, "FORR": 6, "VERS": 5},
                    "Daníel Sindrason": {"STÆR": 7, "ENSK": 7, "FORR": 5, "VERS": 10}, }
        nyttdict = {}
        #Fall sem reiknar meðaleinkun úr stær og forr
        def medaleinkunnStaeForr(nyttdict):
            #Keyri for lúppu sem plúsar saman einkunn úr stær og forr hjá öllum nemendum
            for nemendur,einkannir in nemadict.items():
                heildareinkunn = einkannir["STÆR"]+einkannir["FORR"]
                #Þegar það er búið deili ég því með 2 sem finnur meðaltalið
                medaleinkunn = heildareinkunn / 2
                #Set nemandann og meðaleinkunina í nýtt dict sem svo prentast út
                nyttdict[nemendur] = medaleinkunn
            return nyttdict
        print(medaleinkunnStaeForr(nyttdict))

    elif val == 8:
        print("Spurning A: Hvenær er eðlilegra að nota tuple heldur"
              "en lista í forritun og hvers vegna. Hverjir eru kostir"
              "og gallar tuple og lista")
        print("Mitt persónulega svar er þannig að mér finnst listi mun"
              "hentugri en tuple vegna þess að listar eru breytanlegir"
              "og hægt að færa inn í þá gögn og taka úr en með tuple"
              "þá er það ekki hægt og gagnagrindin helst föst og sú"
              "sama. Gáfulegt er að nota tuple og lista innan til dæmis"
              "dictionary")
        print("")
        print("Hver er grundvallar munur á gagnagrindunum list og dictionary"
              "í python")
        print("Listi er breytanlegur á allan hátt og dictionary er með"
              "lykla og gildi sem tengjast. Það er til dæmis hægt að sækja"
              "gildi út frá lykli og uppfæra gildi útfrá lyklum. Mikilvægt"
              "er að segja að það er hægt að geyma allar gerðir innan allra"
              "gerða. Hvort sem það sé tuple,listi eða dictionary. Hægt er að "
              "geyma þau öll innan hvors annars.")

    elif val == 9:
        on = False
    else:
        print("þú hefur ekki valið rétt")

print("Takk fyrir að nota forritið mitt")