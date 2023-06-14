on = True

while on == True:

    print("1. Áfangalisti")
    print("2. Athuga nafn")
    print("3. Athuga kyn")
    print("4. Fimm listar í lista")
    print("5. Hætta")


    val = int(input("Hvað viltu gera?"))

    if val == 1:
        notendur = int(input("Hversu margir eru skráðir í íslensku tímann"))
        teljari = 0
        listi = []
        on = True
        """
        while teljari < notendur:
            nafn = input("Sláðu inn nafni til að bæta við á listann")
            if nafn not in listi:
                listi.append(nafn)
                teljari = teljari + 1
            elif nafn in listi:
                print("Nafnið er nú þegar á listanum")
        """
        for x in range(notendur):
            nafn = input("Sláðu inn nafn til að bæta við á listann")
            if nafn not in listi:
                listi.append(nafn)


        while on == True:
            print("1. Prenta raðaðan lista")
            print("2. Eyða")
            print("3. Bæta við")
            print("4. Prenta óbreyttan lista")
            print("5. Hætta")
            val = int(input("Veldu hvað þú vilt gera"))

            if val == 1:
                copylisti = listi.copy()
                listi.sort()
                listi.reverse()
                print(listi)

            elif val == 2:
                eyda = input("Veldur hvaða nafn þú vilt eyða")

                if eyda not in listi:
                    print("Nafnið var ekki á listanum")
                elif eyda in listi:
                    listi.remove(eyda)
                    print("Nafninu var eytt út að listanum")
            elif val == 3:
                nafn = input("Sláðu inn nafn til að bæta því við á listann")
                if nafn in listi:
                    print("nafnið er nú þegar á listanum")
                elif nafn not in listi:
                    listi.append(nafn)
            elif val == 4:
                print(copylisti)
                print(listi)

            elif val == 5:
                on = False
            else:
                print("Þú valdir ekki rétt")

        print("Takk fyrir að nota listaprógrammið mitt")


    elif val == 2:
        nafn1 = input("Sláðu inn nafn")
        nafn2 = input("Sláðu inn nafn")

        if len(nafn1) == len(nafn2):
            print("Nöfnin eru jafn löng")
        lengd = len(nafn1)
        if len(nafn2) < lengd:
            lengd = len(nafn2)

        for x in range(lengd):
            if nafn1[x] == nafn2[x]:
                print("bókstafur",x+1,nafn1[x],"er eins í báðum nöfnunum")


    elif val == 3:
        listi = []
        teljari = 0
        while teljari < 10:
            nafn = input("Sláðu inn nafn 10 sinnum")
            if nafn in listi:
                print("Nafnið er nú þegar á listanum")
            else:
                listi.append(nafn)
                teljari = teljari + 1
        listi.sort()
        print(listi)

        lengstanafn = max(listi)
        stystanafn = min(listi)


        print("Lengsta nafnið á listanum er:",lengstanafn)
        print("Stysta nafnið á listanum er:",stystanafn)


    elif val == 4:
        listi = [["Karl Jónsson", 17, "Tölvubraut"], ["Jóna Hannesdóttir",18,"Málabraut"],["Eiríkur Jónsson",21,"Hárgreiðslubraut"],["Svana Sveinsdóttir",19,"Tölvubraut"]]
        on2 = True
        while on2 == True:
            print("Listi innan lista")
            print("1. Prenta út lista línu fyrir línu")
            print("2. Eyða nemanda úr listanum")
            print("3. Reikna meðalaldur")
            print("4. Bæta nemanda við í listann")
            print("5. Breyta braut")
            print("6. Leita eftir nafni")
            print("7. Hætta")
            val = int(input("veldu nú"))
            if val == 1:
                for x in range(len(listi)):
                    print("--", listi[x][0], "--", listi[x][1], "--", listi[x][2])
                for x in range(len(listi)):
                    print(listi[x])
            elif val == 2:
                for x in range(len(listi)):
                    print(listi[x])
                val = int(input("veldu hvaða notanda þú vilt eyða(0,1,2,3...)"))
                if listi[val] in listi:
                    del(listi[val])
                    print("Tókst")
                else:
                    print("Tókst ekki")
            elif val == 3:
                summa = 0
                listi2 = [item[1] for item in listi]
                for x in listi2:
                    summa = summa + x
                lengdlistans = len(listi2)
                medalaldur = summa / lengdlistans
                print(medalaldur)

                summa2 = 0
                for x in range(len(listi)):
                    summa2 = summa2 + listi[x][1]
                lengdlista = len(listi)
                medalaldur2 = summa / lengdlista
                print(medalaldur2)


            elif val == 4:
                gull = True
                while gull == True:
                    nafn = input("Sláðu inn nafn til að bæta við á listann")
                    for x in range(len(listi)):
                        if nafn in listi[x]:
                            print("Nafnið er nú þegar á listanum")
                            nafn = input("Sláðu inn nafn aftur")

                    aldur = int(input("Sláðu inn aldur"))
                    braut = input("Sláðu inn  braut")
                    aftur = input("Viltu bæta öðru nafni við  listann? Já/Nei")
                    if aftur == "Já":
                        gull = True
                    else:
                        gull = False
                nyrlisti = []

                nyrlisti.append(nafn)
                nyrlisti.append(aldur)
                nyrlisti.append(braut)
                listi.append(nyrlisti)
            elif val == 5:
                for x in range(len(listi)):
                    print(x+1,listi[x])
                val = int(input("hvaða notanda viltu breyta"))
                val = val - 1
                for x in range(len(listi)):
                    if x == val:
                        print("Þú valdir",listi[x],"Sem er listi númer",x+1)
                        val2 = int(input("Hverju viltu breyta? 1. Nafn 2. Aldur 3. Braut"))
                        val2 = val2 - 1
                        if val2 == 0:
                            nafn1 = input("Í hvað viltu breyta nafninu?")
                            listi[x][0] = nafn1
                        elif val2 == 1:
                            aldur2 = int(input("Í hvað viltu breyta aldrinum?"))
                            listi[x][1] = aldur2
                        elif val2 == 2:
                            braut2 = input("Í hvað viltu breyta brautinni?")
                            listi[x][2] = braut2
                print("Villa, byrjaðu aftur")
            elif val == 6:
                leita = False
                leit = input("Sláðu inn nafn til að athuga hvort það sé á listanum")
                for x in range(len(listi)):
                    for i in range(len(listi[x])):
                        if leit == listi[x][i]:
                            print("Nafnið fannst")
                            print(listi[x])
                            leita = True
                if leita == False:
                    print("Nafnið fannst ekki")

            elif val == 7:
                on2 = False
    elif val == 5:
        on = False

    else:
        print("þú hefur ekki valið rétt")

print("Takk fyrir að nota forritið mitt")