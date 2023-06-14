# Hreiðar Pétursson
# 24 Apríl 2023
# Klasar æfingaverkefni 3
import random
on = True

while on == True:

    print("1. Setning")
    print("2. Meðlimir")
    print("3. Nemandi")
    print("4. Bankareikningur")
    print("5. Hætta")


    val = int(input("Hvað viltu gera?"))

    if val == 1:
        class setning:
            def __init__(self, strengur=""):
                self.strengur = strengur

            def fall1(self):
                self.strengur = input("Sláðu inn streng")

            def __str__(self):
                return "strengurinn er: " + self.strengur


        # Verð að kalla á klasann með breytu
        s = setning()
        # Sæki fallið innan klasans svo
        s.fall1()
        # Og prenta
        print(s)

    elif val == 2:

        class adili:
            def __init__(self, nafn, gsm, heimasimi, email):
                self.nafn = nafn
                self.gsm = gsm
                self.heimasimi = heimasimi
                self.email = email

            def breytanafn(self, nafn):
                self.nafn = nafn

            def breytagsm(self, gsm):
                self.gsm = gsm

            def breytaheimasimi(self, heimasimi):
                self.heimasimi = heimasimi

            def breytaemail(self, email):
                self.email = email

            def __str__(self):
                return f"Nafn: {self.nafn}\n" \
                       f"gsm: {self.gsm}\n" \
                       f"Heimasími: {self.heimasimi}\n" \
                       f"Email: {self.email}"


        listi = []
        adili1 = adili("Hreiðar", 7617603, 7617603, "hreidar1987@gmail.com")
        adili2 = adili("Gunnar", 5648976, 8976589, "blabla@blabla.com")
        adili3 = adili("Jónas", 1234567, 7654321, "jonas@island.is")
        listi.append(adili1)
        listi.append(adili2)
        listi.append(adili3)
        for adili in listi:
            print(adili)
            print("")

        adili1.breytaemail("nyttemail@email.com")
        adili2.breytagsm(8978976548)

        for adili in listi:
            print(adili)
            print("")


    elif val == 3:
        class nemandi:
            def __init__(self,nafn,aldur,braut):
                self.nafn = nafn
                self.aldur = aldur
                self.braut = braut

            def __str__(self):
                return f"Nafn: {self.nafn}\n" \
                       f"Aldur: {self.aldur}\n" \
                       f"Braut: {self.braut}\n"

            def elsti(listi):


                # Róbótinn gerði þessa útgáfu !!!
                haedstialdur = max(nemandi.aldur for nemandi in listi)
                for x in listi:
                    if haedstialdur == x.aldur:
                        return f"Elsti nemandinn er:\n" \
                               f"{x}"



                #  ÉG GERÐI ÞESSA ÚTGÁFU AF ÞESSU
                #aldurlisti = []
                #for x in listi:
                #    aldurlisti.append(x.aldur)
                #haedsti = max(aldurlisti)

                #for x in listi:
                #    if haedsti == x.aldur:
                #        return f"Elsti nemandinn er:\n" \
                #               f"{x}"

            def rada(listi):
                # Þetta er ein útgáfan af hvernig er hægt að gera þetta
                radadurlisti = sorted(listi, key=lambda nemandi: nemandi.nafn)
                return radadurlisti

                # Þetta er útgáfan sem ég gerði sjálfur
                #nyrlistinofn = []
                #for nemandi in listi:
                #    nafn = nemandi.nafn
                #    nyrlistinofn.append(nafn)
                #radadurlistinyrlistinofn = sorted(nyrlistinofn)
                #return radadurlistinyrlistinofn

            def fjoldibraut(listi):
                brautir = {}
                for nemandi in listi:
                    if nemandi.braut in brautir:
                        brautir[nemandi.braut] += 1
                    else:
                        brautir[nemandi.braut] = 1
                return brautir

        # GERI VALMYND TIL AÐ AUÐVELDA AÐ KEYRA FÖLLIN !
        valmynd = True
        while valmynd == True:
            print("1. Prenta út nemendur")
            print("2. Elsti nemandinn")
            print("3. Nemendur í stafrófsröð")
            print("4. Hversu margir á hverri braut")
            print("5. Hætta")
            val = int(input("Veldu nú"))
            # Bý til lista af 10 instances í klasanum
            listi = []
            nemandi1 = nemandi("Jón", 20, "Raunvísindadeild")
            nemandi2 = nemandi("Guðrún", 22, "Tölvunarfræðideild")
            nemandi3 = nemandi("Pétur", 21, "Læknadeild")
            nemandi4 = nemandi("Sigrún", 24, "Hagfræðideild")
            nemandi5 = nemandi("Anna", 30, "Lögfræðideild")
            nemandi6 = nemandi("Bjarni", 27, "Tölvunarfræðideild")
            nemandi7 = nemandi("Katrín", 21, "Tölvunarfræðideild")
            nemandi8 = nemandi("Jóhannes", 23, "Hagfræðideild")
            nemandi9 = nemandi("Sigurður", 18, "Læknadeild")
            nemandi10 = nemandi("Hafdís", 22, "Lögfræðideild")

            listi.append(nemandi1)
            listi.append(nemandi2)
            listi.append(nemandi3)
            listi.append(nemandi4)
            listi.append(nemandi5)
            listi.append(nemandi6)
            listi.append(nemandi7)
            listi.append(nemandi8)
            listi.append(nemandi9)
            listi.append(nemandi10)
            if val == 1:
                for nemandi in listi:
                    print(nemandi)
            elif val == 2:
                # Kalla á hæðsti fallið innan nemandi klasans
                haedsti2 = nemandi.elsti(listi)
                print(haedsti2)
            elif val == 3:
                # Raðaður listi af nöfnum nemenda
                print("Hérna kemur raðaður listi af nemendum")
                radadurlisti = nemandi.rada(listi)
                for x in radadurlisti:
                    print(x)

            elif val == 4:
                # Hérna er ég að keyra fallið sem segir hvað margir eru á hverri braut
                print("Hérna kemur hvað margir eru á hverri braut")
                brautir = nemandi.fjoldibraut(listi)
                for key, value in brautir.items():
                    print(key, ":", value)
            elif val == 5:
                valmynd = False

    elif val == 4:
        # Bý til klasann
        class bankareikningur:
            # Skilgreini eiginleika klasans
            def __init__(self,nafn,inneign,vextir):
                self.nafn = nafn
                self.inneign = inneign
                self.vextir = vextir
            # Skilgreini útprentun klasans
            def __str__(self):
                return f"Nafn: {self.nafn}\n" \
                       f"Inneign: {self.inneign}\n" \
                       f"Þínir vextir: {self.vextir}\n"
            # Bý til fall sem breytir vöxtum
            def breytavextir(self,vextir):
                self.vextir = vextir
            # Bý til fall sem reiknar út innistæðu eftir einn mánuð
            # og skilar nýju innistæðunni
            def inneigneftirhvernmanud(self):
                grodi = 0
                nyvaxtatala = self.vextir / 12
                grodi = self.inneign * nyvaxtatala
                nyinneign = self.inneign + grodi
                nyinneign = round(nyinneign,0)
                self.inneign = nyinneign
                return f"{self.inneign}"


        # Tilvik klasans - Instances - Sett í lista
        listi = []
        einstaklingur1 = bankareikningur("hreiðar",50000000 , 0.0565)
        einstaklingur2 = bankareikningur("Gunna", 3000, 0.04)
        einstaklingur3 = bankareikningur("Danni Galvez",5897678, 0.04)
        einstaklingur4 = bankareikningur("Bjarni",3456789,0.04)
        listi.append(einstaklingur1)
        listi.append(einstaklingur2)
        listi.append(einstaklingur3)
        listi.append(einstaklingur4)

        # Bý til lista yfir mánuði ársins
        manudir = ['janúar', 'febrúar', 'mars', 'apríl', 'maí', 'júní', 'júlí',
                   'ágúst', 'september', 'október', 'nóvember', 'desember']
        ar = []
        for x in range(100):
            artala = 2023 + x
            ar.append(artala)


        # Geri valmynd til að keyra klasann
        valmynd = True
        while valmynd == True:
            print("1. Reikna út inneign eftir hvern mánuð")
            print("2. Breyta ársvöxtum")
            print("3. Sýna nafn og inneign")
            print("4. Hætta")
            val = int(input("Veldu nú"))

            if val == 1: # Velja hvað marga mánuði skal reikna fram í tímann
                for x in range(len(listi)):
                    print(x+1,"\n",listi[x])
                valeinstak = int(input("Veldu hjá hverjum skal reikna út inneign eftir einn mánuð"))
                valeinstak -= 1
                for x in range(len(listi)):
                    if x == valeinstak:
                        hvadmargirmanudir = int(input("Veldu hvað marga mánuði skal reikna"))
                        for i in range(hvadmargirmanudir):
                            utreikningur = listi[x].inneigneftirhvernmanud()
                            print("Inneign í",manudir[i%12],ar[i//12],"er:",utreikningur)

            elif val == 2:
                for x in range(len(listi)):
                    print(str(x+1) + "\n" + str(listi[x]))
                valeinstak = int(input("Veldu hjá hverjum þú vilt breyta vöxtum"))
                valeinstak -= 1
                for x in range(len(listi)):
                    if x == valeinstak:
                        vextir = float(input("Sláðu inn nýja vaxtatölu (Dæmi: 0.04)"))
                        listi[x].breytavextir(vextir)

            elif val == 3:
                for x in listi:
                    print(x)
            elif val == 4:
                valmynd = False


    elif val == 5:
        on = False
    else:
        print("þú hefur ekki valið rétt")

print("Takk fyrir að nota forritið mitt")