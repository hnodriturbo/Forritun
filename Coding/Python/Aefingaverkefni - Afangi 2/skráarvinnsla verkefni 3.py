#Hreiðar Pétursson
#12/4 2023
#Skráarverkefni C - Föll og skrár

#Föll til að geta notað aftur og aftur

#Liður 1 - B
def skrifaiskra(listi, nafntxt):
    # geraLista(fjoldi=2,byrjun=0,endir=1001)
    with open(nafntxt, "w", encoding="utf-8") as f:
        for x in range(len(listi)):
            xx = str(listi[x])
            if x != 0:
                f.write(',' + xx)
            else:
                f.write(xx)
        return listi
#Liður 1 - C
def lesaskra(nafntxt):
    with open(nafntxt,"r",encoding="utf-8") as f:
        tolur = f.read().split(",")
    for x in tolur:
        x = x.strip(",")

    nyrlisti = []
    for x in tolur:
        x = x.strip()
        if x:
            nyrlisti.append(int(x))
    return nyrlisti

#Liður 1 - D
def prenta(listi):
    for x in listi:
        print(x, end=",")


valmynd = True
while valmynd == True:
    print("1. Sléttar Tölur")
    print("2. Prímtölur")
    print("3. Tuple skrá")
    val = int(input("Veldu nú"))
    if val == 1:
        #Liður A
        listi = []
        def geraLista(fjoldi,byrjun,endir):
            for x in range(byrjun,endir,fjoldi):
                if x % 2 == 0:
                    listi.append(x)
            return listi
        #Liður A
        listinn = geraLista(fjoldi=2,byrjun=0,endir=1001)
        #Liður B
        def skrifaiskra(listi, nafntxt):
            # geraLista(fjoldi=2,byrjun=0,endir=1001)
            with open(nafntxt, "w", encoding="utf-8") as f:
                for x in range(len(listi)):
                    xx = str(listi[x])
                    if x != 0:
                        f.write(',' + xx)
                    else:
                        f.write(xx)
        #Liður C
        def lesaskra(nafntxt):
            with open(nafntxt,"r",encoding="utf-8") as f:
                tolur = f.read().split(",")
            for x in tolur:
                x = x.strip(",")

            nyrlisti = []
            for x in tolur:
                x = x.strip()
                if x:
                    nyrlisti.append(int(x))
            return nyrlisti
        #Liður C
        print("Skráin sjálf í lista")
        listi = lesaskra("files/tolur.txt")
        print(listi)
        #Liður D
        def prenta(listi):
            for x in listi:
                print(x,end=",")
        prenta(listi)
        #Liður E
        def medaltal(nyrlisti):
            lengd = len(nyrlisti)
            summa = 0
            for x in nyrlisti:
                summa = summa + x
            medaltal = summa / lengd
            return "{0:.2f}".format(medaltal)
        print("")
        print("meðaltal")
        print(medaltal(lesaskra("files/tolur.txt")))
        #Liður F og G
        def uppiatta(nyrlisti):
            uppiattalisti = []
            for x in nyrlisti:
                if x % 8 == 0:
                    uppiattalisti.append(x)
            with open("files/sumarslettartolur.txt","w",encoding="utf-8") as f:
                for x in uppiattalisti:
                    x = str(x)
                    f.write(x+",")
            return uppiattalisti
        print("Tölur upp í átta")
        print(uppiatta(lesaskra("files/tolur.txt")))
        #Liður H
        def tiutolurilinu(nyrlisti):
            teljari = 0
            for x in range(len(nyrlisti)):
                teljari += 1
                if teljari % 10 == 0:
                    print(nyrlisti[x])
                else:
                    print(nyrlisti[x], end=" ")
        print("Tíutölur í línu")
        print(tiutolurilinu(lesaskra("files/tolur.txt")))
    elif val == 2:
        #Föll úr hluta 2
        #liður A
        primes=[]
        def primtolur(primes):
            for x in range(2,101):
                teljari = 0
                for i in range(1,x+1):
                    if x % i == 0:
                        teljari += 1
                if teljari == 2:
                    primes.append(x)
            return primes
        #Liður E
        def tolurseminnihalda7(primes):
            for x in primes:
                xx = str(x)
                for i in xx:
                    if i == "7":
                        print(x,"inniheldur töluna 7")
        #Liður F
        def fjordahver(primes):
            listifjordahver = []
            for x in range(len(primes)):
                if x % 4 == 0:
                    listifjordahver.append(primes[x])
            return listifjordahver
        #Liður A
        primtolulisti = primtolur(primes)
        #Liður B
        #skrifa2 = skrifaiskra(primes,"files/primtolur.txt")
        #Liður C
        skrifa3 = lesaskra("files/primtolur.txt")
        print(skrifa3)
        #Liður D
        prentalista = prenta(skrifa3)
        print(prentalista)
        #Liður E
        tolursjo = tolurseminnihalda7(primes)
        #Liður F
        fjorda = fjordahver(primes)
        print(fjorda)
        #Liður G
        listiUrF = skrifaiskra(fjorda,"files/fjorda.txt")

    elif val == 3:
        #Tuple fyrir skránna
        tuple1 = (1,2,3,4,5,6,7,8,9)
        tuple2 = ("a","b","c","d","e","f","g","h")
        tuple3 = ("konni",123,"sponni",234)
        #Föll sem eru notuð í lið 3
        #Liður A
        def skrifatuple(tuple,skra):
            with open(skra,"a",encoding="utf-8") as gogn:
                tuplestrengur = str(tuple)
                gogn.write(tuplestrengur)
                gogn.write("\n")
        #Liður B
        def lesatuple(skra):
            with open(skra,"r",encoding="utf-8") as gogn:
                data = gogn.read()
            print(data)
        #Liður C
        def buatiltuple():
            print("Athugið að það þarf að vera komma á milli gilda")
            notandatuple = input("Sláðu inn gögnin sem eiga að vera í þínu tuple")
            tuplen = tuple(notandatuple.split(","))
            return tuplen
        #Liður D
        def skrifatuple(tuplen,skra):
            with open(skra,"a",encoding="utf-8") as gogn:
                tuplegogn = str(tuplen)
                gogn.write(tuplegogn)
                gogn.write("\n")
            with open(skra,"r",encoding="utf-8") as gogn:
                lesagogn = gogn.read()
            print(lesagogn)
        #Liður E
        def summafyrstutuple(skra):
            with open(skra, "r") as gogn:
                linur = gogn.read().splitlines()
            for i in range(len(linur)):
                if i == 0:
                    lina1 = linur[i]
            lina1listi = lina1.strip("()").split(",")
            lina1listi = list(map(int, lina1listi))
            summa = 0
            for x in lina1listi:
                summa += x
            return(summa)
        #Liður F
        def prentautsummu(summa):
            print(summa)

        #Verkefnið sjálft
        valmynd2 = True
        while valmynd2 == True:
            print("A. Skrifa tuple skrá")
            print("B. Lesa tuple skrá og prenta")
            print("C. Búðu til þitt eigið tuple")
            print("D. Notendatuple")
            print("E. Summa fyrstu tupplu úr skránni")
            print("F. Prenta út samtölu fyrstu tupplu")
            val = input("Veldu nú")
            if val == "A":
                skrifa1 = skrifatuple(tuple1, "files/tuple.txt")
                skrifa2 = skrifatuple(tuple2, "files/tuple.txt")
                skrifa3 = skrifatuple(tuple3, "files/tuple.txt")
            elif val == "B":
                print(lesatuple("files/tuple.txt"))
            elif val == "C":
                print(buatiltuple())
            elif val == "D":
                skrifatuplebreytan = skrifatuple(buatiltuple(),"files/tuple.txt")
                print(skrifatuplebreytan)
            elif val == "E":
                print(summafyrstutuple("files/tuple.txt"))
            elif val == "F":
                print(prentautsummu(summafyrstutuple("files/tuple.txt")))

    elif val == 4:
        valmynd = False