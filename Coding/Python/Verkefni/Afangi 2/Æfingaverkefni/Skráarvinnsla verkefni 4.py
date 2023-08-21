#Hreiðar Pétursson
#16 apríl 2023
#Skráarvinnsla verkefni 4 - D - CSV skrá

valmynd = True
while valmynd == True:
    print("1. Bæta við nýjum")
    print("2. Breyta upplýsingum")
    print("3. Eyða upplýsingum / línum")
    print("4. Prenta út alla. Ein lína per notanda")
    print("5. Hætta")
    val = int(input("Veldu hvað þú vilt gera"))

    # Bæta við nýjum inn í skránna
    if val == 1:
        nafn = input("Sláðu inn nafn til að bæta við")
        kt = int(input("Sláðu inn kennitölu"))
        simanr = int(input("Sláðu inn símanúmer"))
        with open("files/simaskra.csv","a",encoding="utf-8") as gogn:
            gogn.write(nafn)
            gogn.write(";")
            kt = str(kt)
            gogn.write(kt)
            gogn.write(";")
            simanr = str(simanr)
            gogn.write(simanr)
            gogn.write("\n")
        print("Tókst að bæta við")
        print("Nafn:",nafn,"Kt:",kt,"Sími:",simanr)

    # Breyta notanda upplýsingum
    elif val == 2:
        # Byrja á að sækja gögnin úr skránni
        with open("files/simaskra.csv", "r", encoding="utf-8") as gogn:
            linur = gogn.read().splitlines()
            listi = []
            for x in linur:
                listi.append(x)

        # Geri valmynd fyrir notanda til að auðvelda kóðann
        menu = True
        while menu == True:
            print("1. Breyta aðilum úr skránni")
            print("2. Skrifa breytingarnar í skránna")
            choice = int(input("Veldu nú"))

            #Breyta
            if choice == 1:
                # Prenta út listann sem er gerður úr skránni
                for x in range(len(listi)):
                    print(x + 1, ":", listi[x])

                # Býð notanda að velja útfrá númeri hverjum hann vill breyta
                breyta = int(input("Veldu númer hvað þú vilt breyta"))
                breyta = breyta - 1

                # Set þann sem notandi valdi inn í sér lista sem ég splitta útfrá semíkommunum
                nyrlisti = listi[breyta].split(";")

                # Prenta út hvað notandi valdi á snyrtilegan hátt
                print("Þú hefur valið:",nyrlisti[0],"-",nyrlisti[1],"-",nyrlisti[2])

                # Geri valmynd og spyr hverju notandi vill breyta í nafninu sem var valið
                valmynd2 = True
                while valmynd2 == True:
                    val = int(input("1. breyta nafn - 2. breyta kt - 3. breyta símanr - 4. Hætta við"))

                    if val == 1:
                        # Bið um nýja nafnið og breyti því
                        nyttnafn = input("Sláðu inn nýja nafnið")
                        nyrlisti[0] = nyttnafn
                        # Breyti aðskilda listanum í sameinaðan streng
                        sameinadurstrengur = ";".join(nyrlisti)
                        # Geri strenginn að lista inn í heildarlistanum
                        listi[breyta] = sameinadurstrengur
                        # Prenta út breytingarnar
                        print("Tókst að breyta")
                        print("Uppfærður listi")
                        for x in range(len(listi)):
                            print(x+1,":",listi[x])
                        valmynd2 = False

                    elif val == 2:
                        nykt = input("Sláðu inn nýju kennitöluna")
                        nyrlisti[1] = nykt
                        sameinadurstrengur = ";".join(nyrlisti)
                        listi[breyta] = sameinadurstrengur
                        print("Tókst að breyta")
                        print("Uppfærður listi")
                        for x in range(len(listi)):
                            print(x+1,":",listi[x])
                        valmynd2 = False

                    elif val == 3:
                        nyttsimanr = input("Sláðu inn nýtt símanúmer")
                        nyrlisti[2] = nyttsimanr
                        sameinadurstrengur = ";".join(nyrlisti)
                        listi[breyta] = sameinadurstrengur
                        print("Tókst að breyta")
                        print("Uppfærður listi")
                        for x in range(len(listi)):
                            print(x+1,":",listi[x])
                        valmynd2 = False
                    elif val == 4:
                        valmynd2 = False

            # Skrifa breytingarnar í skránna
            elif choice == 2:
                # Set í skránna(Geri nýja skrá sem inniheldur allt það gamla ásamt breytingunum)
                with open("files/simaskra.csv", "w", encoding="utf-8") as gogn:
                    for x in listi:
                        x = str(x)
                        gogn.write(x)
                        gogn.write("\n")
                print("Tókst að uppfæra skránna")
                menu = False

            # Hætta valmöguleikinn
            elif choice == 3:
                menu = False

    elif val == 3:
        # Byrja á að sækja gögnin og setja þau í lista
        with open("files/simaskra.csv","r",encoding="utf-8") as gogn:
            linur = gogn.read().splitlines()
            listi = []
            geymslulisti = []
            for x in linur:
                geymslulisti.append(x)
                x = x.split("\n")

                for i in range(len(x)):
                    x[i] = x[i].split(";")

                listi.append(x)

            nyrlisti = []
            for x in listi:
                for i in x:
                    nyrlisti.append(i)

            valmynd3 = True
            while valmynd3 == True:
                val = int(input("1. Velja aðila til að eyða - 2. Vista breytingar - 3. Hætta"))
                if val == 1:

                    for x in range(len(nyrlisti)):
                        print(x+1,":",nyrlisti[x][0],"- Kt:",nyrlisti[x][1],"- Sími:",nyrlisti[x][2])
                    eyda = int(input("Veldu númer hvað þú vilt eyða"))
                    eyda -= 1

                    if eyda not in range(len(geymslulisti)):
                        print("villa, númerið er ekki til á listanum")
                    else:
                        print("Tókst að eyða")
                        print(nyrlisti[eyda][0], "- Kt:", nyrlisti[eyda][1], "- Sími:", nyrlisti[eyda][2])
                        geymslulisti.pop(eyda)
                        nyrlisti.pop(eyda)

                elif val == 2:
                    with open("files/simaskra.csv","w",encoding="utf-8") as gogn:
                        for x in geymslulisti:
                            x = str(x)
                            gogn.write(x)
                            gogn.write("\n")
                        print("Tókst að uppfæra skránna")
                        valmynd3 = False

                elif val == 3:
                    valmynd3 = False

    elif val == 4:
        with open("files/simaskra.csv", "r", encoding="utf-8") as gogn:
            lines = gogn.read().splitlines()
            listi = []
            for x in lines:
                x = x.split("\n")

                for i in range(len(x)):
                    x[i] = x[i].split(";")

                listi.append(x)

            nyrlisti = []
            for x in listi:
                for i in x:
                    nyrlisti.append(i)
            for x in range(len(nyrlisti)):
                print(x + 1, ":", nyrlisti[x][0], "- Kt:", nyrlisti[x][1], "- Sími:", nyrlisti[x][2])
    elif val == 5:
        valmynd = False