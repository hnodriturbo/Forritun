# Skilaverkefni 3 - Liður 2
# 22/09/2023 - 12/10/2023
# Anton Smári Gunnarsson

from spil import Spil, OgiltSpilException
import random

# Klasi fyrir Spilastokk
class Spilastokkur:
    thegarSynt = []

    # Hér er spilastokkur búinn til
    # Ef engin spil eru skilgreind þá er þetta stokkur og hann býr sjálfkrafa til 52 spil
    # Annars er þetta hendi eða ruslbunki og self.spilaListi er notaður í stað self.spilabunki
    def __init__(self, spilaListi):
        self.spilabunki = []
        self.spilaListi = []
        if len(spilaListi) == 0:
            for tegund in [Spil.HJARTA, Spil.SPADI, Spil.TIGULL, Spil.LAUF]:
                for tala in range(2, 15):
                    try:
                        self.spilabunki.append(Spil(tala, tegund))
                    except OgiltSpilException as e:
                        print(f"Gat ekki búið til spil: {e}")
        else:
            self.spilaListi = spilaListi

    # Svona er spilastokk convertað í streng
    def __str__(self):
        if self.spilaListi:
            return ', '.join(str(spil) for spil in self.spilaListi)
        elif self.spilabunki:
            return '\n'.join(str(spil) for spil in self.spilabunki)
        else:
            return "Engin spil í þessum bunka!"

    # Svona er spilastokk convertað í int (til að athuga hvort hann sé tómur til að ákvarða leikslok)
    def __int__(self):
        if self.spilaListi:
            return len(self.spilaListi)
        elif self.spilabunki:
            return len(self.spilabunki)
        else:
            return 0

    # Þetta fall tjékkar bara hvort sýnd spil eða hendi sé með öll þau spil sem að þarf til þess að fá einhver aukastig
    def erHendiIDictionary(self, hendiListi, aukastigDictionary):
        samsvarandi_lyklar = []
        for lykill, aukastigListi in aukastigDictionary.items():
            if set(hendiListi).issuperset(set(aukastigListi)):
                samsvarandi_lyklar.append(lykill)
        return samsvarandi_lyklar if samsvarandi_lyklar else None

    # Þetta fall heldur utan um nánast allt sem hefur að gera með aukastig og sýnd spil
    def geturSyntSpilFyrirAukastig(self, hendiListi):
        stig = []
        thegarBoridSaman = []
        synt = []

        aukastigSort = {
            "hjarta hjón": Spil.HJARTA,
            "spaða hjón": Spil.SPADI,
            "tígul hjón": Spil.TIGULL,
            "lauf hjón": Spil.LAUF,
            "hjarta röð": Spil.HJARTA,
            "spaða röð": Spil.SPADI,
            "tígul röð": Spil.TIGULL,
            "lauf röð": Spil.LAUF,
        }
        aukastigYfirskrifar = {
            "hjarta röð": "hjarta hjón",
            "spaða röð": "spaða hjón",
            "tígul röð": "tígul hjón",
            "lauf röð": "lauf hjón",
        }
        aukastigRadir = {
            "hjarta röð": [Spil(10, Spil.HJARTA), Spil(11, Spil.HJARTA), Spil(12, Spil.HJARTA), Spil(13, Spil.HJARTA), Spil(14, Spil.HJARTA)],
            "spaða röð": [Spil(10, Spil.SPADI), Spil(11, Spil.SPADI), Spil(12, Spil.SPADI), Spil(13, Spil.SPADI), Spil(14, Spil.SPADI)],
            "tígul röð": [Spil(10, Spil.TIGULL), Spil(11, Spil.TIGULL), Spil(12, Spil.TIGULL), Spil(13, Spil.TIGULL), Spil(14, Spil.TIGULL)],
            "lauf röð": [Spil(10, Spil.LAUF), Spil(11, Spil.LAUF), Spil(12, Spil.LAUF), Spil(13, Spil.LAUF), Spil(14, Spil.LAUF)],
        }
        aukastigHjon = {
            "hjarta hjón": [Spil(12, Spil.HJARTA), Spil(13, Spil.HJARTA)],
            "spaða hjón": [Spil(12, Spil.SPADI), Spil(13, Spil.SPADI)],
            "tígul hjón": [Spil(12, Spil.TIGULL), Spil(13, Spil.TIGULL)],
            "lauf hjón": [Spil(12, Spil.LAUF), Spil(13, Spil.LAUF)],
        }
        aukastigAllt = {
            "allar tíur": [Spil(10, Spil.HJARTA), Spil(10, Spil.SPADI), Spil(10, Spil.TIGULL), Spil(10, Spil.LAUF)],
            "allir gosar": [Spil(11, Spil.HJARTA), Spil(11, Spil.SPADI), Spil(11, Spil.TIGULL), Spil(11, Spil.LAUF)],
            "allar drottningar": [Spil(12, Spil.HJARTA), Spil(12, Spil.SPADI), Spil(12, Spil.TIGULL), Spil(12, Spil.LAUF)],
            "allir kóngar": [Spil(13, Spil.HJARTA), Spil(13, Spil.SPADI), Spil(13, Spil.TIGULL), Spil(13, Spil.LAUF)],
            "allir ásar": [Spil(14, Spil.HJARTA), Spil(14, Spil.SPADI), Spil(14, Spil.TIGULL), Spil(14, Spil.LAUF)],
        }

        aukastigIBodi = self.erHendiIDictionary(hendiListi, aukastigRadir)

        if aukastigIBodi is not None:
            for aukastig in aukastigIBodi:
                if aukastig in self.thegarSynt:
                    stig.append(0)
                    synt.append(False)
                else:
                    if aukastigSort[aukastig] == Spil.TROMP:
                        if aukastigYfirskrifar[aukastig] in self.thegarSynt:
                            stig.append(300 - 80)
                        else:
                            stig.append(300)
                    else:
                        if aukastigYfirskrifar[aukastig] in self.thegarSynt:
                            stig.append(150 - 40)
                        else:
                            stig.append(150)
                    synt.append(True)
                thegarBoridSaman.append(aukastig)

                # Koma í veg fyrir að stig teljist til bæði vegna raðar og hjóna
                thegarBoridSaman.append(aukastigYfirskrifar[aukastig])
                stig.append(0)
                synt.append(False)

        aukastigIBodi = self.erHendiIDictionary(hendiListi, aukastigHjon)

        if aukastigIBodi is not None:
            for aukastig in aukastigIBodi:
                if aukastig not in thegarBoridSaman:
                    if aukastig in self.thegarSynt:
                        stig.append(0)
                        synt.append(False)
                    else:
                        if aukastigSort[aukastig] == Spil.TROMP:
                            stig.append(80)
                        else:
                            stig.append(40)
                        synt.append(True)
                    thegarBoridSaman.append(aukastig)

        aukastigIBodi = self.erHendiIDictionary(hendiListi, aukastigAllt)

        if aukastigIBodi is not None:
            for aukastig in aukastigIBodi:
                if aukastig in self.thegarSynt:
                    stig.append(0)
                    synt.append(False)
                else:
                    stig.append(sum([int(spil) for spil in aukastigAllt[aukastig]]))
                    synt.append(True)
                thegarBoridSaman.append(aukastig)

        for x in range(len(stig)):
            if thegarBoridSaman[x] not in self.thegarSynt:
                self.thegarSynt.append(thegarBoridSaman[x])

        return stig, thegarBoridSaman, synt

    # Hér er fallið sem leyfir spilara að velja spil af hendi og ef það er tromp 7 þá skiptir það henni út fyrir trompspilið í borði
    def skiptaUtTromp7(self, spilastokkur):
        skila = False
        while True:
            gildarUtsetningar = []
            for x in range(0, len(self.spilaListi)):
                gildarUtsetningar.append(str(x + 1))
                spil = self.spilaListi[x]
                print(f"{str(x + 1)}) {str(spil)}")
            print(f"Trompið er {Spil.SORTIR_2[Spil.TROMP]}")
            skiptaUtVal = input("Veldu tromp 7 af hendi: ")

            if skiptaUtVal not in gildarUtsetningar:
                print("Veldu eitt af eftirfarandi: ")
                continue
            spil = self.spilaListi[int(skiptaUtVal) - 1]
            if spil.spilaTegund == Spil.TROMP and spil.spilaTala == 7:
                print(f"Þú skiptir tromp 7 út fyrir neðsta sýnilega útskiptanlega trompinu: {str(spilastokkur.dragaTromp)}")
                self.baetaSpiliVidLista(spilastokkur.dragaTromp)
                self.notaSpilAfHendi(spil)
                spilastokkur.dragaTromp = spil

                skila = True
            else:
                print("Valið spil er ekki tromp 7 og því var þessi aðgerð ekki leyfð...")

            break
        return skila

    # Þetta fall leyfir spilara að sýna spilin sýn og ef það eru hjón, röð eða allir gosar t.d. þá fær spilari stig fyrir það, annars ekkert...
    # Ekki er hægt að sýna sömu spilin tvisvar
    def synaSpil(self):
        hendiSyna = []
        while True:
            gildarUtsetningar = []
            print()
            for x in range(0, len(self.spilaListi)):
                spil = self.spilaListi[x]
                if spil not in hendiSyna:
                    gildarUtsetningar.append(str(x + 1))
                    print(f"{str(x + 1)}) {str(spil)}")
            print("s) Staðfesta val, sýna spil!")
            print()

            skiptaUtVal = input("Veldu eitt og eitt spil til þess að sýna og staðfestu síðan með því að velja s) : ")
            if skiptaUtVal in gildarUtsetningar:
                spil = self.spilaListi[int(skiptaUtVal) - 1]
                hendiSyna.append(spil)
            elif skiptaUtVal.lower() == "s":
                stig, thegarSynt, synt = self.geturSyntSpilFyrirAukastig(hendiSyna)
                samtalsstig = 0
                for x in range(len(stig)):
                    if synt[x] == True:
                        print(f"Þú sýnir {thegarSynt[x]} og færð þannig {stig[x]} stig")
                        samtalsstig += stig[x]
                    elif synt[x] == False and len(thegarSynt) == 1:
                        print(f"Þú hefur þegar sýnt {thegarSynt[x]} og færð því engin stig")
                if len(stig) == 0:
                    print("Þú valdir spil sem ekki hægt er að fá stig fyrir að sýna, en núna veit tölvan að þú ert með þessi spil, æjæjæj...")
                break
        return samtalsstig

    # Hérna er svo valmyndin til þess að leyfa spilara að velja hvaða spil hann vill setja út
    # Inní þessu falli er svo skoðað hvort spilari sé með sömu spilaTegund og sett var í borð
    # og má hann eingöngu velja spil af þeirri tegund ef hann hefur þá tegund á hendi...
    def setjaUtSpil(self, spilAndstaedings = None, spilastokkur = None):
        stig = 0
        skiptiUtTromp7 = False

        tharfAdSvaraISomuMynt = False
        if spilAndstaedings != None:
            for spil in self.spilaListi:
                if spil.spilaTegund == spilAndstaedings.spilaTegund:
                    tharfAdSvaraISomuMynt = True

        gildarUtsetningar = []
        if not tharfAdSvaraISomuMynt:
            for x in range(0, len(self.spilaListi)):
                gildarUtsetningar.append(str(x + 1))

        while True:
            if spilAndstaedings != None:
                print(f"Tölvan setur út {spilAndstaedings}")

            print(f"Trompið er {Spil.SORTIR_2[Spil.TROMP]}")
            for x in range(0, len(self.spilaListi)):
                spil = self.spilaListi[x]
                if tharfAdSvaraISomuMynt and spil.spilaTegund == spilAndstaedings.spilaTegund:
                    gildarUtsetningar.append(str(x + 1))
                print(f"{str(x + 1)}) {str(spil)}")
            print("a) Skipta tromp 7 út fyrir tromp í borði")
            print("b) Sýna spil")
            veljaSpil = input("Veldu hvaða spil þú vilt setja út: ")

            if veljaSpil in gildarUtsetningar:
                spilariVelurThettaSpil = self.spilaListi[int(veljaSpil) - 1]
                break
            elif veljaSpil.lower() == "a":
                if(self.skiptaUtTromp7(spilastokkur)):
                    skiptiUtTromp7 = True
            elif veljaSpil.lower() == "b":
                stig += self.synaSpil()
            else:
                if tharfAdSvaraISomuMynt:
                    print("Þú þarft að bekinna (svara í sömu mynt) / velja spil af hendi sem er af sömu sort og sett var í borð...")
                else:
                    print("Þú þarft að velja einn af eftirfarandi valkostum:")

        return spilariVelurThettaSpil, stig, skiptiUtTromp7

    # Eyðir spili af hendi
    def notaSpilAfHendi(self, spil):
        self.spilaListi.remove(spil)

    # Bætir spili við self.spilaListi
    def baetaSpiliVidLista(self, spil):
        if isinstance(spil, list):
            for spilILista in spil:
                self.spilaListi.append(spilILista)
        else:
            self.spilaListi.append(spil)

    # Dregur efsta spil úr self.spilabunki (list.pop(-1) dregur aftasta spilið með áherslu)
    def dragaSpilEfstUrSpilabunka(self):
        return self.spilabunki.pop(-1) if self.spilabunki else None

    # Þetta fall fjarlægir ónotuð spil í Marías úr spilabunkanum
    def fjarlaegjaOnotudSpil(self):
        self.spilabunki = [spil for spil in self.spilabunki if spil.spilaTala > 6]

    # Þetta fall stokkar spilabunkann
    def stokkaSpil(self):
        random.shuffle(self.spilabunki)
