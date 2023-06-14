# Hreiðar Pétursson
# 26-30 apríl 2023
# Klasar - Ættbálkar með hermönnum

import random

# Klasinn fyrir herdeild og leikmenn
class herdeild:
    def __init__(self, deild, leikmenn):
        self.deild = deild
        self.leikmenn = leikmenn


    def __str__(self):
        return f"{self.deild}:\n" \
               f"{self.leikmenn}"

# Klasinn fyrir hvern leikmann og gildin hans. Þessi klasi inheritar herdeild klasann
class leikmadur(herdeild):
    def __init__(self, lif, vopn, afl, nr, deild, nafn):
        #
        herdeild.__init__(self, deild=deild, leikmenn=[])
        self.afl = afl
        self.lif = lif
        self.vopn = vopn
        self.nr = nr
        self.nafn = nafn

    def set_lif(self,nyttlif):
        self.lif = nyttlif

    def __str__(self):
        return f"{self.nr} - {self.nafn} - Líf: {self.lif} - Vopn: {self.vopn}({self.afl}) ({self.deild})"

# Klasinn til að velja herdeild í leiknum
class veljaherdeild:
    def __init__(self,herdeildarlisti):
        self.herdeildarlisti = herdeildarlisti

    # Fallið til að velja herdeild útfrá herdeildarlistanum
    def velja(herdeildarlisti):
        for x, i in enumerate(herdeildarlisti):
            print(f"{x+1} Herdeild: {i.deild}")
        while True:
            try:
                val = int(input("Sláðu inn nr hvaða deild þú vilt velja"))
                val -= 1
                lengd = len(herdeildarlisti)
                if val < 0 or val >= lengd:
                    print("Innsláttarvilla")
                    return None

                herdeild = herdeildarlisti[val]
                herdeildafrit = list(herdeild.leikmenn)
                print(f"Þú valdir herdeild nr {val + 1} {herdeild.deild}")
                for l in herdeild.leikmenn:
                    print(l)

                return herdeild, herdeildafrit
            except ValueError:
                print("Innsláttur ekki á réttu formi")

    # Fallið fyrir val tölvunnar
    def valtolvu(herdeildarlisti):
        while True:
            herdeild = random.choice(herdeildarlisti)
            hermenntolvuafrit = list(herdeild.leikmenn)
            if herdeild != leikmadurval:
                break
        print(f"Tölvan valdi:{herdeild.deild}")
        return herdeild, hermenntolvuafrit

# Klasinn fyrir bardagann sjálfann
class bardagi:
    def __init__(self, leikmadurval,tolvaval):
        self.leikmadurval = leikmadurval
        self.tolvaval = tolvaval

    # Fallið sem velur leikmenn í bardagann
    def veljaleikmennibardaga(leikmadurval,tolvaval):
        # Vel tvo leikmenn og skilgreini þá
        leikmadur1 = random.choice(leikmadurval.leikmenn)
        leikmadur2 = random.choice(tolvaval.leikmenn)
        print(f"Leikmenn {leikmadur1.nafn}({leikmadur1.deild}) og {leikmadur2.nafn}({leikmadur2.deild}) berjast!")

        # Leikmaður særist um það sem hinn hefur í afl
        leikmadur1.lif -= leikmadur2.afl
        if leikmadur1.lif < 0:
            leikmadur.set_lif(leikmadur1,0)
        print(f"{leikmadur1.nafn} særðist um {leikmadur2.afl} stig og á núna {leikmadur1.lif} eftir í líf")

        # Ef leikmaður á minna en 0 í líf deyr hann
        if leikmadur1.lif <= 0:
            print(f"Leikmaður {leikmadur1.nafn} er dáinn")
            leikmadurval.leikmenn.remove(leikmadur1)

        # Sama að gerast hérna og fyrir leikmann eitt
        leikmadur2.lif -= leikmadur1.afl
        if leikmadur2.lif < 0:
            leikmadur.set_lif(leikmadur2,0)
        print(f"{leikmadur2.nafn} særðist um {leikmadur1.afl} stig og á núna {leikmadur2.lif} eftir í líf")
        if leikmadur2.lif <= 0:
            print(f"Leikmaður {leikmadur2.nafn} er dáinn")
            tolvaval.leikmenn.remove(leikmadur2)
        print("")


    # Fallið sem keyrir fallið veljaleikmenn í bardaga þangað til annað hvort liðið vinnur
    def bardagakeyrsla(leikmadurval,tolvaval):
        while leikmadurval.leikmenn and tolvaval.leikmenn:
            bardagi.veljaleikmennibardaga(leikmadurval,tolvaval)
            if not leikmadurval.leikmenn:
                herdeildarlisti.remove(leikmadurval)
                print(f"Herdeild tölvunnar {tolvaval.deild} vann bardagann!")
                tolvaval.leikmenn = hermenntolvuafrit
                for leikmenn in tolvaval.leikmenn:
                    leikmenn.lif = 100
                break
            elif not tolvaval.leikmenn:
                herdeildarlisti.remove(tolvaval)
                print(f"Herdeildin þín {leikmadurval.deild} vann bardagann!")
                leikmadurval.leikmenn = leikmadurleikmennafrit
                for leikmenn in leikmadurval.leikmenn:
                    leikmenn.lif = 100
                break
        print("")


# Fall sem býr til leikmenn leiksins
def buatilleikmenn():
    # Listar og mappað dictionary með info fyrir leikmenn sem verða búnir til:
    mannanofn = ['Adam', 'Benjamin', 'Caleb', 'Daniel', 'Ethan', 'Finn', 'Gavin', 'Henry', 'Isaac', 'Jack', 'Kai', 'Liam', 'Mason', 'Nathan', 'Oliver', 'Parker', 'Quinn', 'Ryan', 'Samuel', 'Theodore', 'Uri', 'Vincent', 'Wyatt', 'Xander', 'Yadiel', 'Zachary', 'Abigail', 'Brielle', 'Chloe', 'Delilah', 'Ella', 'Faith', 'Grace', 'Harper', 'Isabella', 'Jasmine', 'Kennedy', 'Lily', 'Makayla', 'Natalie', 'Olivia', 'Peyton', 'Quinn', 'Riley', 'Sophia', 'Tessa', 'Violet', 'Willow', 'Ximena', 'Yara', 'Zoe', 'Avery', 'Bella', 'Camila', 'Daisy', 'Emily', 'Fiona', 'Gianna']
    listideildir = ["Hamarsdeild","Indjánahermenn","Blóðbálkur","Víkingar","Þessalóníumenn","Breiðhyltingar"]

    listivopn = {
        1: ("Axt", 30),
        2: ("Höggspjót", 25),
        3: ("Sverð", 20),
        4: ("Bogi", 15),
        5: ("Skjöldur", 10),
        6: ("Geirvöðvi", 26),
        7: ("Hnífur", 17),
        8: ("Spjót", 24),
        9: ("Byssa", 35),
        10: ("Klökk", 22),
    }

    # Set tvo teljara og geri for lúppu sem keyrir 6 sinnum fyrir 6 herdeildir
    teljari = 0
    teljarideildir = 0
    teljarivopn = 0
    herdeildarlisti = []
    for x in range(1, 7):
        deild = listideildir[teljarideildir]
        teljarideildir += 1
        # Bý tillista fyrir hermenn og keyri 10 lúppur fyrir 10 hermenn
        hermenn = []
        for i in range(10):
            # Skilgreini nafn útfrá nafnalista
            if teljari < len(mannanofn):
                nafn = mannanofn[teljari]
            else:
                nafn = "Aukalingur"
            teljari += 1

            # Skilgreini vopn og afl úr möppuðu dictionary
            vopn, afl = listivopn[i+1]

            # Bý til leikmann úr breytunum að ofan og bæti þeim í listann
            hermadur = leikmadur(lif=100, vopn=vopn, afl=afl, nr=i + 1, deild=deild, nafn=nafn)
            hermenn.append(hermadur)
        # Adda þessu öllu í herdeildir og hermenn og set það í listann
        lid = herdeild(deild, hermenn)
        herdeildarlisti.append(lid)
    return herdeildarlisti

# Bý til alla leikmenn:
herdeildarlisti = buatilleikmenn()

# Keyri svo leikinn sjálfann!!!
while True:
    try:
        valmynd = True
        while valmynd == True:
            print("Velkominn í bardagaleikinn minn")
            print("1. Velja herdeild")
            print("2. Berjast")
            print("3. Prenta út alla leikmenn")
            print("4. Bardaga og leikreglur")
            print("5. Hætta")
            val = int(input("Veldu nú"))

            if val == 1: # Velja herdeild
                nidurstada = veljaherdeild.velja(herdeildarlisti)
                if nidurstada == None:
                    print("Ekkert lið valið")
                else:
                    # Sæki liðið sem leikmaður velur
                    leikmadurval, leikmadurleikmennafrit = veljaherdeild.velja(herdeildarlisti)
                    # Sæki liðið sem tölvan velur
                    tolvaval, hermenntolvuafrit = veljaherdeild.valtolvu(herdeildarlisti)

            elif val == 2: # Berjast

                # Keyri klasann og fallið sem keyrir bardagann til enda
                bardagi.bardagakeyrsla(leikmadurval,tolvaval)

                if len(herdeildarlisti) < 2:
                    print("Leik lokið! Það er bara 1 lið eftir! Viltu spila aftur?")
                    print("1 = Já --- 2 = Nei")
                    val=int(input("Veldu 1 eða 2"))
                    if val == 1:
                        herdeildarlisti.clear()
                        herdeildarlisti = buatilleikmenn()
                    else:
                        valmynd = False

            elif val == 3: # Prenta út lið og leikmenn sem eru eftir í leiknum

                # Nota for lúppu til að prenta út herdeildir sem eru enþá til í listanum
                for herdeild in herdeildarlisti:
                    print(f"Herdeild: {herdeild.deild}")
                    for i in herdeild.leikmenn:
                        print(f"{i}")

            elif val == 4: # Bardaga og leikreglur
                print("Leikreglur eru þannig að þú velur þér lið sem þú vilt að berjist.")
                print("Tölvan velur sér svo sjálf lið og þú velur svo að láta herdeildirnar berjast.")
                print("Herdeildirnar berjast þangað til enginn leikmaður er eftir í öðru hvoru liði")
                print("Þetta endurtekur þú ef þú vilt spila aftur")

            elif val == 5: # Hætta valmöguleikinn
                valmynd = False
            else:
                print("Villa")
    except ValueError:
        print("Innsláttarvilla")
print("Takk fyrir að spila leikinn minn")