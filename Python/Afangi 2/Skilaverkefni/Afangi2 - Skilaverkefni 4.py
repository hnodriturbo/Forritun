# Hreiðar Pétursson
# Apríl 2023 - Forritun
# Skilaverkefni 4 - Áfangi 2

import math
import random


# ----- Hérna eru allir klasar sem ég nota í þessu verkefni -----

# --- Klasinn hringur sem er liður 1 í verkefninu ---
class hringur:
    # Smiðurinn
    def __init__(self, radius):
        self.radius = radius
    # Skilgreini strenginn fyrir klasann
    def __str__(self):
        return f"Radíus er {self.radius}"
    # Fallið sem reiknar ummálið
    def ummal(self):
        ummal = 2 * math.pi * self.radius
        ummal2 = round(ummal,1)
        return f"Ummál hringsins með {self.radius} í radíus er = {ummal2}"
    # Fallið sem reiknar flatarmálið
    def flatarmal(self):
        annadveldi = self.radius ** 2
        flatarmal = math.pi * annadveldi
        flatarmal2 = round(flatarmal,1)
        return f"Flatarmál hringsins með {self.radius} í radíus er = {flatarmal2}"





# --- Klasi og föll sem eru notuð í lið 2 - bankareikningur verkefnið ---

# --- Klasinn eigandi ---
class eigandi:
    # Smiðurinn
    def __init__(self,nafn,innistaeda=0):
        self.nafn = nafn
        self.innistaeda = innistaeda
    # Strengurinn
    def __str__(self):
        return f"Nafn: {self.nafn} Innistæða: {self.innistaeda}"
    # Fallið sem tekur út af reikningnum
    def uttekt(self,upphaed):
        innistaeda = self.innistaeda
        if upphaed > innistaeda:
            return False
        else:
            nyinnistaeda = innistaeda - upphaed
            self.innistaeda = nyinnistaeda
            return True
    # Fallið sem leggur inn á reikninginn
    def innlogn(self,upphaed):
        innistaeda = self.innistaeda
        nyinnistaeda = innistaeda + upphaed
        self.innistaeda = nyinnistaeda
        return True

# Fallið sem eyðir nafni út úr listanum
def eyda(listi,nafn):
    for owner in listi:
        if owner.nafn == nafn:
            listi.remove(owner)
            return True
    return False

# Fallið sem prentar út öll nöfn og innistæður
def prenta_reikninga(listi):
    for numer, eigandi in enumerate(listi):
        print(numer+1,eigandi)

# Fallið sem finnur þann sem á hæðstu innistæðuna
def haesta(listi):
    inneignir = []
    for eigandi in listi:
        inneignir.append(eigandi.innistaeda)
    haedst = max(inneignir)
    for eigandi in listi:
        if eigandi.innistaeda == haedst:
            print("Sá sem er með mest í bankanum er:")
            print(eigandi)





# --- Klasi og föll sem er notað í lið 3 - Spilastokkur ---
class spil:
    def __init__(self,tegund,numer,nafn):
        self.tegund = tegund
        self.numer = numer
        self.nafn = nafn
    def __str__(self):
        return f"{self.tegund} {self.nafn} ({self.numer})"

# Fallið sem býr til spilastokkinn
def spilastokkurbuatil():
    listitegundir = ["Hjarta", "Spaði", "Tígull", "Lauf"]
    listispilanofn = ["Tvistur", "Þristur", "Fjarki", "Fimma", "Sexa", "Sjöa", "Átta", "Nía", "Tía", "Gosi",
                      "Drottning", "Kóngur", "Ás"]
    spilastokkur = []
    for x in range(len(listitegundir)):
        tegund = listitegundir[x]
        for i in range(len(listispilanofn)):
            nafn = listispilanofn[i]
            numer = i + 2
            spilinstance = spil(tegund, numer, nafn)
            spilastokkur.append(spilinstance)
    return spilastokkur

# Fallið sem gefur spilin
def gefaspil(spilastokkur):
    spilnotandi = []
    spiltolva = []
    for gjof in range(2):
        for spiligjof in range(26):
            spil = random.choice(spilastokkur)
            if gjof == 0:
                spilnotandi.append(spil)
                spilastokkur.remove(spil)
            elif gjof == 1:
                spiltolva.append(spil)
                spilastokkur.remove(spil)
    return spilnotandi, spiltolva

# Fallið sem segir hvor setur spilið út á undan
def hvorseturut(validspilnotandi,validspiltolva,teljari,tromp):
    # Breytur fyrir útprentun um hvor setur út
    utprentunnotandiaut = f"Notandi setti út {validspilnotandi.tegund} {validspilnotandi.nafn} og tölvan setti út {validspiltolva.tegund} {validspiltolva.nafn}"
    utprentuntolvaaut = f"Tölvan settu út {validspiltolva.tegund} {validspiltolva.nafn} og notandi setti út {validspilnotandi.tegund} {validspilnotandi.nafn}"
    if teljari % 2 == 1:
        print("Sá sem setur fyrst út er Notandi (tromp er:",tromp,")")
        print(utprentunnotandiaut)
        return True
    else:
        print("Sá sem setur fyrst út er Tölva (tromp er:",tromp,")")
        print(utprentuntolvaaut)
        return False

# Fallið sem velur spil úr stokknum
def veljaspil(spilnotandi,spiltolva):
    # Vel aftasta spilið úr stokknum
    for x in range(len(spilnotandi)):
        if x == len(spilnotandi) - 1:
            validspilnotandi = spilnotandi[x]
    for x in range(len(spiltolva)):
        if x == len(spiltolva) - 1:
            validspiltolva = spiltolva[x]
    return validspilnotandi, validspiltolva

# Fallið sem fjarlægir valin spil úr stokknum
def removespil(spilnotandi,spiltolva,validspilnotandi,validspiltolva):
    spilnotandi.remove(validspilnotandi)
    spiltolva.remove(validspiltolva)

# Fallið sem spilar spilið sjálft
def spilaspilið(spiltolva,spilnotandi,tromp,spilaslagfyrirsig):
    # Skilgreini teljara
    teljari = 0
    teljarinotandi = 0
    teljaritolva = 0
    # Keyri while lúppu þangað til spil tölvu eru búin en síðasta spilið sem sett er út er spil tölvunnar
    while len(spiltolva) > 0:
        if spilaslagfyrirsig == True:
            viltuspilanaestaslag = input("Veldu 1 til að spila slag - Veldu 2 til að hætta")
            if viltuspilanaestaslag == "1":
                print("")
                pass
            elif viltuspilanaestaslag == "2":
                return
            else:
                print("Verður að velja 1 eða 2")
                continue
        # Teljari til að greina hvor setur út á undan
        teljari += 1

        # Kalla á fallið sem velur spilin
        validspilnotandi, validspiltolva = veljaspil(spilnotandi,spiltolva)

        # Útprentun vinnings skilaboða
        notandivinnur = f"Notandi vinnur slaginn með trompi því {validspilnotandi.tegund} {validspilnotandi.nafn} vinnur {validspiltolva.tegund} {validspiltolva.nafn}"
        tolvanvinnur = f"Tölvan vinnur slaginn með trompi því {validspiltolva.tegund} {validspiltolva.nafn} vinnur {validspilnotandi.tegund} {validspilnotandi.nafn}"
        notandivinnur_ekkitromp = f"Notandi vinnur slaginn því {validspilnotandi.tegund} {validspilnotandi.nafn} vinnur {validspiltolva.tegund} {validspiltolva.nafn}"
        tolvanvinnur_ekkitromp = f"Tölvan vinnur slaginn því {validspiltolva.tegund} {validspiltolva.nafn} vinnur {validspilnotandi.tegund} {validspilnotandi.nafn}"
        notandivinnur_ekkitromp_fyrstaspil = f"Notandi vinnur slaginn því hann setti fyrst út {validspilnotandi.tegund} {validspilnotandi.nafn}"
        tolvanvinnur_ekkitromp_fyrstaspil = f"Tölvan vinnur slagin því hún setti fyrst út {validspiltolva.tegund} {validspiltolva.nafn}"

       # Prenta út hver setur út fyrsta spilið og set return statement í breytu
        athugahvorseturut = hvorseturut(validspilnotandi, validspiltolva, teljari, tromp)

        # Ef annaðhvort spilið er tromp spil
        if validspilnotandi.tegund == tromp or validspiltolva.tegund == tromp:
            # Ef notandi er með tromp og tölvan ekki
            if validspilnotandi.tegund == tromp and validspiltolva.tegund != tromp:
                # Vinningsprentun
                print(notandivinnur)
                print("")
                # Hætta teljaranotanda um einn því hann vann slaginn
                teljarinotandi += 1
                # Fjarlægi spilin frá hendi beggja
                removespil(spilnotandi,spiltolva,validspilnotandi,validspiltolva)

            # Ef tölvan er með tromp og notandi ekki
            elif validspiltolva.tegund == tromp and validspilnotandi.tegund != tromp:
                print(tolvanvinnur)
                print("")
                teljaritolva += 1
                removespil(spilnotandi,spiltolva,validspilnotandi,validspiltolva)

            # Ef báðir eru með tromp
            elif validspiltolva.tegund == tromp and validspilnotandi.tegund == tromp:
                if validspilnotandi.numer > validspiltolva.numer:
                    print(notandivinnur)
                    print("")
                    teljarinotandi += 1
                    removespil(spilnotandi,spiltolva,validspilnotandi,validspiltolva)
                elif validspiltolva.numer > validspilnotandi.numer:
                    print(tolvanvinnur)
                    print("")
                    teljaritolva += 1
                    removespil(spilnotandi,spiltolva,validspilnotandi,validspiltolva)

        # Hérna er kóðinn fyrir slag úti og hvorugt spilið er tromp
        elif validspilnotandi.tegund != tromp and validspiltolva.tegund != tromp:

            # Ef Notandi setur út fyrsta spilið
            if athugahvorseturut == True:
                # Ef tegund tölvunnar er ekki sama tegund og notanda þá vinnur notandi því
                # hann setti fyrsta spilið út
                if validspiltolva.tegund != validspilnotandi.tegund:
                    print(notandivinnur_ekkitromp_fyrstaspil)
                    print("")
                    teljarinotandi += 1
                    removespil(spilnotandi, spiltolva, validspilnotandi, validspiltolva)

                # Ef tölvan setur út sömu tegund þá er athugað hvor er með hærra spilið til að vinna
                elif validspiltolva.tegund == validspilnotandi.tegund:
                    # Notandi vinnur slaginn
                    if validspilnotandi.numer > validspiltolva.numer:
                        print(notandivinnur_ekkitromp)
                        print("")
                        teljarinotandi += 1
                        removespil(spilnotandi, spiltolva, validspilnotandi, validspiltolva)
                    # Tölva vinnur slaginn
                    elif validspilnotandi.numer < validspiltolva.numer:
                        print(tolvanvinnur_ekkitromp)
                        print("")
                        teljaritolva += 1
                        removespil(spilnotandi, spiltolva, validspilnotandi, validspiltolva)

            # Ef tölvan setur út fyrsta spilið:
            elif athugahvorseturut == False:
                # Ef notandi er ekki með sömu tegund og tölvan þá vinnur tölvan
                if validspilnotandi.tegund != validspiltolva.tegund:
                    print(tolvanvinnur_ekkitromp_fyrstaspil)
                    print("")
                    teljaritolva += 1
                    removespil(spilnotandi, spiltolva, validspilnotandi, validspiltolva)
                elif validspilnotandi.tegund == validspiltolva.tegund:
                    # Notandi vinnur slaginn
                    if validspilnotandi.numer > validspiltolva.numer:
                        print(notandivinnur_ekkitromp)
                        print("")
                        teljarinotandi += 1
                        removespil(spilnotandi, spiltolva, validspilnotandi, validspiltolva)
                    # Tölva vinnur slaginn
                    elif validspilnotandi.numer < validspiltolva.numer:
                        print(tolvanvinnur_ekkitromp)
                        print("")
                        teljaritolva += 1
                        removespil(spilnotandi, spiltolva, validspilnotandi, validspiltolva)


    print("Leikurinn fór þannig að tölvan var með",teljaritolva,"stig og þú varst með",teljarinotandi,"stig!")
    if teljaritolva > teljarinotandi:
        print(f"Þú tapaðir leiknum")
    elif teljarinotandi > teljaritolva:
        print(f"Til hamingju!!! ÞÚ VANNST SPILIÐ !!! ÞÚ FÆRÐ EINA MILLJÓN Í VERÐLAUN !!! HAHAHAHA!")
    elif teljarinotandi == teljaritolva:
        print(f"Leikurinn fór jafntefli.")




valmynd = True
while valmynd == True:

    print("1. Hringur")
    print("2. Bankareikningur")
    print("3. Spil")
    print("4. Hætta")

    val = input("Hvað viltu gera?")

    if val == "1":
        try:
            #  Bið notanda um radíus og geri svo valmynd sem keyrir föll inn í klasa eftir vali
            radius = int(input("Sláðu inn radíus hringsins"))
            hringur = hringur(radius)
            valmynd2 = True
            while valmynd2 == True:
                print("1. Reikna ummál hringsins")
                print("2. Reikna Flatarmál hringsins")
                print("3. Breyta radíus")
                print("4. Hætta")
                val = input("Veldu nú")
                if val == "1":
                    print(hringur.ummal())
                elif val == "2":
                    print(hringur.flatarmal())
                elif val == "3":
                    radius = int(input("Sláðu inn nýjan radíus"))
                    hringur.radius = radius
                elif val == "4":
                    valmynd2 = False
                else:
                    print("Ekki rétt valið")
        except ValueError:
            print("Innsláttarvilla")

    elif val == "2": # Bankareikningur

        # Fallið sem býr til instances fyrir klasann eigandi
        def buatileigendur():
            mannanofn = ['Adam', 'Benjamin', 'Caleb', 'Daniel', 'Ethan', 'Finn', 'Gavin', 'Henry', 'Isaac', 'Jack',
                         'Kai', 'Liam', 'Mason', 'Nathan']
            listi = []
            for x in range(len(mannanofn)):
                nafn = mannanofn[x]
                innistaeda = random.randint(1, 500000)
                owner = eigandi(nafn, innistaeda)
                listi.append(owner)
            return listi

        # Keyri fallið og bý til eigendur áður en valmynd keyrist
        listi = buatileigendur()

        # Hérna geri ég valmynd
        valmynd3 = True
        while valmynd3 == True:

            print("Velkominn í bankann minn - Í þessari valmynd eru svokallaðar yfirlits aðgerðir")
            print("1. Velja aðila")
            print("2. Eyða aðila útfrá nafni eða lista")
            print("3. Skoða alla reikninga")
            print("4. Finna hæðstu innistæðuna")
            print("5. Hætta")
            val = input("Veldu nú")

            # Velja aðila
            if val == "1":
                # Prenta út lista til að geta valið aðila útfrá
                for numer, eigandi in enumerate(listi):
                    print(numer+1,eigandi)
                try:
                    valadili = input("Veldu aðila")
                    valadili = int(valadili)
                    valadili -= 1
                    # Ef valið er rétt
                    if valadili >= 0 and valadili < len(listi):
                        # Skilgreini reikningseigandann
                        reikningseigandi = listi[valadili]

                        # Geri svo valmynd útfrá völdum aðila
                        valmynd4 = True
                        while valmynd4 == True:

                            print(reikningseigandi.nafn," - Einstaklingsaðgerðir")
                            print("1. Skoða reikninginn")
                            print("2. Úttekt")
                            print("3. Innlögn")
                            print("4. Eyða viðkomandi")
                            print("5. Hætta")
                            val = input("Veldu nú")

                            if val == "1": # Skoða reikninginn
                                print("")
                                print("Nafn:",reikningseigandi.nafn)
                                print("Innistæða:",reikningseigandi.innistaeda)
                                print("")
                            elif val == "2": # Úttekt
                                while True: # Keyri while lúppu ef ské kynni að úttekt sé meiri en innistæða
                                    # Prenta stöðu reiknings og spyr hvað eigi að taka mikið út
                                    print("Staðan á reikningnum er:",reikningseigandi.innistaeda)
                                    upphaed = input("Sláðu inn upphæð sem skal taka út")
                                    upphaed = int(upphaed)
                                    # Athuga hvort fallið komi True eða False
                                    athuga = reikningseigandi.uttekt(upphaed)
                                    if athuga == True: # Ef fallið er satt keyrist fallið
                                        reikningseigandi.uttekt(upphaed)
                                        print("Ný staða reikningsins er:",reikningseigandi.innistaeda)
                                        break
                                    else: # Annars kemur val um að reyna aftur eða hætta við
                                        val=input("Ekki næg innstæða. 1 = Reyna aftur - 2 = Hætta við")
                                        if val == "1":
                                            continue
                                        elif val == "2":
                                            break
                                        else:
                                            print("Veldu rétt")
                            elif val == "3": # Innlögn
                                    print("Staðan á reikningnum er:",reikningseigandi.innistaeda)
                                    upphaed = input("Sláðu inn upphæð sem skal leggja inn")
                                    upphaed = int(upphaed)
                                    reikningseigandi.innlogn(upphaed)
                                    print("Ný staða reikningsins er:",reikningseigandi.innistaeda)
                            elif val == "4": # Eyða viðkomandi
                                nafn = reikningseigandi.nafn
                                # Athuga hvort eyda sé True eða False
                                athugaeyda = eyda(listi,nafn)
                                # Keyri fallið
                                eyda(listi,nafn)
                                # Ef það kom satt klárast lúppan, annars koma villuskilaboð
                                if athugaeyda == True:
                                    print("Það tókst að eyða",nafn)
                                    break
                                else:
                                    print("Einhver villa kom upp - ekki tókst að eyða")
                            elif val == "5": # Hætta
                                valmynd4 = False
                            else:
                                print("Verður að velja rétt")
                    else:
                        print("Óvænt villa kom upp")
                except ValueError:
                    print("Villa")
            # Eyða aðila útfrá völdu nafni eða lista
            elif val == "2":
                # Geri valmynd
                while True:
                    print("1. Eyða útfrá nafni")
                    print("2. Eyða útfrá lista")
                    print("3. Hætta við")
                    val = input("Veldu nú")
                    if val == "1": # Eyða útfrá nafni
                        # Keyri while lúppu
                        while True:
                            nafn = input("Sláðu inn nafn þess sem skal eyða")
                            # Athuga hvort eyða fallið kemur True eða False
                            athugaeyda = eyda(listi, nafn)
                            # Keyri eyða fallið
                            eyda(listi,nafn)
                            # Ef fallið kemur True prentast staðfesting
                            if athugaeyda == True:
                                print("Það tókst að eyða",nafn)
                                break
                            # Ef nafnið finnst ekki kemur annar valgluggi
                            else:
                                val = input("Viðkomandi fannst ekki. 1 = Reyna aftur - 2 = Hætta við")
                                # Ef notandi vill reyna aftur keyrir while lúppan uppá nýtt
                                if val == "1":
                                    continue
                                # Ef valið er 2 er hætt við og while lúppan breaks
                                elif val == "2":
                                    break
                                # Ef eitthvað vitlaust er valið koma villuskilaboð
                                else:
                                    print("Veldu rétt")
                    elif val == "2": # Eyða útfrá lista
                        # Bý til listann
                        for numer, eigandi in enumerate(listi):
                            print(numer+1, eigandi)
                        adili = int(input("Veldu númer hvað þú vilt eyða"))
                        adili -= 1
                        # Skilgreini eigandann og set nafnið í breytu
                        reikningseigandi = listi[adili]
                        nafn = reikningseigandi.nafn
                        # Athuga hvort fallið er True eða False og set í breytu
                        athuga = eyda(listi,nafn)
                        # Keyri eyða fallið
                        eyda(listi,nafn)
                        # Ef fallið er satt prentast út staðfesting
                        if athuga == True:
                            print("Reikningnum hjá",nafn,"hefur verið lokað")
                        # Annars koma villuskilaboð
                        else:
                            print("Eitthvað hefur ekki verið rétt valið")
                    elif val == "3":
                        break
            # Skoða alla reikninga
            elif val == "3":
                prenta_reikninga(listi)
                print("")
            # Finna hæðstu innistæðuna
            elif val == "4":
                print(haesta(listi))
            elif val == "5": # Hætta
                listi.clear()
                valmynd3 = False

            else:
                print("Innsláttarvilla")
                continue

    elif val == "3": # Spilaleikurinn

        while True:
            # Geri tóman spilastokk og hreinsa hann til að koma í veg fyrir villur
            spilastokkur = []
            spilastokkur.clear()
            spilastokkur = spilastokkurbuatil()
            # Prenta út skilaboðin
            print("Velkominn í Spila leikinn minn")
            val = input("1. Spila - 2. Leikreglur - 3. Hætta")
            if val == "1": # Spila
                # Fallið sem stokkar spilin
                random.shuffle(spilastokkur)
                # Kalla á fallið sem gefur spilin
                spilnotandi, spiltolva = gefaspil(spilastokkur)
                # Vel tromp fyrir spilið
                tromp = random.choice(["Hjarta", "Spaði", "Tígull", "Lauf"])
                # Keyri lúppu og geri annað menu sem býður uppá að láta spilið spilast og spila hvern slag fyrir sig
                while True:
                    print("Það er búið að gefa spilin! Þú ert með",len(spilnotandi),"spil á hendi og trompið er:",tromp)
                    val2 = input("1. Láta spilið spilast - 2. Spila hvern slag fyrir sig - 3. Sjá spilin þín - 4. Hætta")
                    # Láta spilið spilast
                    if val2 == "1":
                        spilaslagfyrirsig = False
                        spilaspilið(spiltolva,spilnotandi,tromp,spilaslagfyrirsig)
                        # Býð uppá að spila aftur og keyri kóða í samræmi við það
                        valspilaaftur = input("Spilið er búið. Viltu spila aftur? 1. Já - 2. Nei")
                        if valspilaaftur == "1":
                            spilastokkur = spilastokkurbuatil()
                            spilnotandi, spiltolva = gefaspil(spilastokkur)
                            continue
                        else:
                            break
                    elif val2 == "2": # Spila hvern slag fyrir sig
                        spilaslagfyrirsig = True
                        spilaspilið(spiltolva,spilnotandi,tromp,spilaslagfyrirsig)
                        # Býð uppá að spila aftur og keyri kóða í samræmi við það
                        valspilaaftur = input("Spilið er búið. Viltu spila aftur? 1. Já - 2. Nei")
                        if valspilaaftur == "1":
                            spilastokkur = spilastokkurbuatil()
                            spilnotandi, spiltolva = gefaspil(spilastokkur)
                            continue
                        else:
                            break
                    elif val2 == "3": # Sjá spilin þín
                        for spil in spilnotandi:
                            print(spil)
                    elif val2 == "4": # Hætta valmöguleikinn
                        break

            elif val == "2": # Leikreglur
                print("Leikreglur eru þannig hljóðandi:")
                print("Hvor um sig fær helming spilastokks eða 26 spil á hendi")
                print("Notandi byrjar á að setja út fyrsta spilið og svo sitt á hvað")
                print("Sá sem setur fyrsta spilið út ræður sort. Sá sem setur seinna spil út þarf að vera með sömu sort")
                print("Ef sá sem setur seinna spilið út er ekki með sömu sort þá tapar sá aðili")
                print("Ef sá sem setur seinna spilið er með sömu sort þá vinnur hærra spilið")
                print("Tromp er random valið fyrir leikinn og ef tromp er úti vinnur það slaginn")
                print("Ef báðir aðilar eru með tromp úti vinnur hærra trompið")
                print("Takk fyrir að spila leikinn minn")
            elif val == "3":
                break
            else:
                print("Vitlaust valið")

    elif val == 4: # Hætta valmöguleikinn
        pass

    else:   # Villuskilaboðin
        print("þú hefur ekki valið rétt")



print("Takk fyrir að nota forritið mitt")