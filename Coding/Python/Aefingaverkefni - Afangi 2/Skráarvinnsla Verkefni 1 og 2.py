#Hreiðar Pétursson
#Skráarvinnsla
"""
#Æfingadæmi 1
on = True
while on == True:
    strengur = input("Sláðu inn streng til að setja í skráana")

    with open("files/skra.txt","a",encoding="utf-8") as f:
        f.write(strengur+"\n")
    print(strengur,"Hefur verið skrifaður í skránna skra.txt")

    with open("files/skra.txt","r",encoding="utf-8") as f:
        skrain = f.read()
    print(skrain)
"""
#Æfingadæmi 2 - 1
valmynd = True
while valmynd == True:
    print("1.Skrifa 5 sinnum einkunn í skránna")
    print("2. Lesa gögn úr skránni")
    print("3. Meðaltal með 2 aukastöfum")
    val = int(input("Veldu nú"))
    if val == 1:
        teljari = 0
        with open("files/Einkunnir.txt","w",encoding="utf-8") as f:
            for x in range(5):
                einkunn = input("Sláðu inn 5 heiltölueinkunnir")
                f.write(einkunn+",")
        """
        while teljari < 6:
            einkunn = input("Sláðu inn 5 heiltölueinkunnir")
            teljari += 1
            with open("files/Einkunnir.txt", "w", encoding="utf-8") as f:
                f.write(einkunn)
                f.write(",")
        print("Það gekk upp að skrifa í skránna 5 sinnum með nýja línu á milli")
"""
    elif val == 2:
        listi = []

        with open("files/Einkunnir.txt","r",encoding="utf-8") as f:
            innihald = f.read().split(",")
            innihald.pop()

        print(innihald)
        listi = list(map(int,innihald))
        print(listi)

        nyrlistiintegers = []
        for x in innihald:
            x = int(x)
            nyrlistiintegers.append(x)
        print(nyrlistiintegers)
    elif val == 3:
        with open("files/Einkunnir.txt","r",encoding="utf-8") as f:
            innihald = f.read().split(",")
            innihald.pop()
        nyrlistiintegers = []
        for x in innihald:
            x = int(x)
            nyrlistiintegers.append(x)
        lengd = len(nyrlistiintegers)
        print(lengd)
        summa = 0
        for x in nyrlistiintegers:
            summa = summa + x
        medaltal = summa / lengd
        print("{0:.2f}".format(medaltal))
        summa = 0
        nyrnyrlistiintegers = list(map(int,innihald))
        for x in nyrnyrlistiintegers:
            summa = summa + x
        medaltal = 0
        medaltal = summa / lengd
        print("{0:.2f}".format(medaltal))







