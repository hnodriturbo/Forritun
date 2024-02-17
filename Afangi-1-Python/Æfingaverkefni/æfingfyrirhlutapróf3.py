on = True

while on == True:

    print("1. Dæmi")
    print("2. Dæmi")
    print("3. Dæmi")
    print("4. Dæmi")
    print("5. Dæmi")
    print("6. Dæmi")
    print("7. Hætta")

    val = int(input("Hvað viltu gera?"))

    if val == 1:
        tala1 = int(input("Sláðu inn tölu 1"))
        tala2 = int(input("Sláðu inn tölu 2"))

        print("Summa talnanna er {} + {} = {}".format(tala1,tala2,tala1+tala2))

    elif val == 2:
        fyrranafn = input("Sláðu inn fyrra nafnið þitt")
        seinnanafn = input("Sláðu inn seinna nafnið þitt")

        print("Halló",fyrranafn,seinnanafn)
    elif val == 3:
        kilometrar = float(input("Sláðu inn lengd í kílómetrum"))

        metrar = kilometrar * 1000

        print(kilometrar,"eru",metrar,"metrar")


    elif val == 4:
        laun = int(input("Sláðu inn laun á klukkustund"))
        klst = int(input("Sláðu inn fjölda klukkustunda sem unnið var"))
        print("heilarlaun verða þá {} kr".format(laun * klst))
        skattur = 0
    elif val == 5:
        laun = int(input("Sláðu inn laun á klukkustund"))
        klst = int(input("Sláðu inn fjölda klukkustunda sem unnið var"))
        heildarlaun = laun * klst
        skattur = 0
        if heildarlaun > 30000:
            umfram = heildarlaun - 30.000
            skattur = umfram * 0.20
            heildarlaun2 = umfram - skattur
            print("Heildarlaunin þín eru",heildarlaun)
            print("Skattur sem þú þarft að borga er",skattur)
            print("Útborgað færðu:",heildarlaun2)
        else:
            print("Heilarlaun þín verða þá:",heildarlaun)
            print("Skattur:",skattur)
    elif val == 6:
        gradur = int(input("Sláðu inn gráður"))

        hringur = gradur // 360

        afghringur = gradur % 360

        print("Það gera",hringur,"hringir og",afghringur,"gráður afgangs")

    elif val == 7:
        on = False


    else:
        print("þú hefur ekki valið rétt")

print("Takk fyrir að nota forritið mitt")