########## Hreiðar Pétursson ###########
  ######### Skilaverkefni 1 ##########
############## Ágúst 2023 ##############

import random
import math

while True:
    print("----- Velkominn  í skilaverkefni 1 -----")
    print(" ----- 1. Hermannaverkefnið ----- ")
    print(" ----- 2. Landsliðshópaverkefnið ----- ")
    print(" ----- 3. Hin ýmsu föll ----- ")
    print(" ----- 4. Föll sem lesa streng ----- ")
    print(" ----- 5. Textaskráin tolur.txt ----- ")
    print(" ----- 6. HÆTTA ----- ")
    
    val = int(input(" ----- Veldu nú ! ----- "))
    
    if val == 1:
        # Herdeildarklasinn
        class herdeild:
            def __init__(self, deild, hermenn=[]):
                self.deild = deild
                self.hermenn = hermenn

            # Útprentun herdeildar
            def __str__(self):
                hermadur_string = ""
                
                # Lúppa í gegnum hermennina og bý til stóran streng
                for hermadur in self.hermenn:
                    hermadur_string += str(hermadur) 
                    
                # Returna útprentun deildar og stóra hermannastrengsins
                return f"{self.deild}: \n" \
                       f"{hermadur_string}"
                       
        
# Fann líka þessa leið á netinu sem á að vera minna problematic
#def __init__(self, deild, hermenn=None):
#    if hermenn is None:
#        hermenn = []
           
         
        # Hermanns klasinn minn
        class hermadur:
            def __init__(self, herdeild, nr, lif, vopn, afl):
                self.herdeild = herdeild
                self.lif = lif
                self.vopn = vopn
                self.afl = afl
                self.nr = nr
                
            # Útprentun hvers hermanns
            def __str__(self): 
                return f"Herdeild: {self.herdeild} - Leikmaður nr: {self.nr}\n"\
                       f"Vopn(afl): {self.vopn}({self.afl}) - Líf: {self.lif}\n"\
                       f"---------------------------------------------- \n"
        
     
        # Nota fall sem býr til hermennina inn í fallinu sem býr til herdeildina   
        def buaTilHerdeildir(teamList):
            
            listOfWeapons = ['Byssa', 'Exi', 'Hnífur'] # Weapon list
            
            # Fall sem býr til hermenn og addar þeim í lista
            def geraHer(deild):
                hermennListi = [] 
                for nr in range(1, 6): # Nota x sem númer
                    vopn = random.choice(listOfWeapons)
                    afl = random.randint(1, 5)
                    lif = random.randint(1, 3)
                    hermennListi.append(hermadur(deild, nr, lif, vopn, afl))
                return herdeild(deild, hermennListi)
            
            # Bý til herdeildirnar og adda þeim í teamList og returna honum
            herdeildBreiðhyltingar = geraHer('Breiðholt')
            herdeildÞessalóníumenn = geraHer('Þessalóníumenn')
            teamList.append(herdeildBreiðhyltingar)
            teamList.append(herdeildÞessalóníumenn)
            return teamList
        
        # Functionið til að leyfa user að velja sína herdeild
        def veljaHerdeild(teamList):
            
            # Prenta út herdeildirnar
            for nr, herdeild in enumerate(teamList):
                print(f"{nr+1}. Herdeild: {herdeild.deild}")
            
            while True:
                valHerdeildar = int(input("Veldu þína herdeild - Veldu 9 til að hætta"))
               
                # Mínusa einn frá valinu og næ í lengd teamList
                valHerdeildar -= 1
                lengd = len(teamList)
                
                # Hætta möguleikinn
                if valHerdeildar == 9:
                    return None
                # Ef valið er vitlaust
                if valHerdeildar < 0 or valHerdeildar >= lengd:
                    print("Innsláttarvilla - Verður að velja herdeild")
                    continue
                
                # valLeikmanns er væntanlega inputtið
                valLeikmanns = teamList[valHerdeildar]
                # 1 - valHerdeildar lætur tolvu alltaf velja hitt liðið
                valTolvu = teamList[1 - valHerdeildar]
                # Skilaboð og returna tuple sem inniheldur tvö objects
                print(f"Þú valdir herdeild: {valLeikmanns.deild}")
                return valLeikmanns, valTolvu
                
                
        # Fight fall sem tekur inn hermennina og lætur þá berjast og returnar annaðhvort hermennunum báðum, eða bara öðrum og hinum sem None value
        def bardagi(hermadurLeikmanns, hermadurTolvu):
            
            # Gott að útskýra hvað er að gerast hverju sinni þegar leikurinn er í gangi
            print(f"\nValinn var maður úr her {hermadurLeikmanns.herdeild} nr: {hermadurLeikmanns.nr} og her {hermadurTolvu.herdeild} nr: {hermadurTolvu.nr} til að berjast")
            print(f"Hermaður úr her {hermadurLeikmanns.herdeild} er með {hermadurLeikmanns.vopn}({hermadurLeikmanns.afl})")
            print(f"Hermaður úr her {hermadurTolvu.herdeild} er með {hermadurTolvu.vopn}({hermadurTolvu.afl})")
            
            
            # Ef hermaður leikmanns vinnur
            if hermadurLeikmanns.afl > hermadurTolvu.afl:
                print(f"Hermaður {hermadurLeikmanns.herdeild} nr: {hermadurLeikmanns.nr} vann bardagann því hann var með öflugra vopnið!")
                hermadurTolvu.lif -= 1
                print(f"Hermaður {hermadurTolvu.herdeild} nr: {hermadurTolvu.nr} missir eitt líf og á núna {hermadurTolvu.lif} líf eftir")
                
                # Ef hermadur tölvunnar á núll líf eftir þá deyr hann
                if hermadurTolvu.lif == 0:
                    print(f"Hermaður nr {hermadurTolvu.nr} í her {hermadurTolvu.herdeild} lét endanlega lífið í þessum bardaga!")
                    return hermadurLeikmanns, None
                
                    
            # Ef hermaður tölvu er með meira afl en hermaður leikmanns
            elif hermadurTolvu.afl > hermadurLeikmanns.afl:
                print(f"Hermaður {hermadurTolvu.herdeild} nr: {hermadurTolvu.nr} vann bardagann því hann var með öflugra vopnið!")
                hermadurLeikmanns.lif -= 1
                print(f"Hermaður {hermadurLeikmanns.herdeild} nr: {hermadurLeikmanns.nr} missir eitt líf og á núna {hermadurLeikmanns.lif} líf eftir")

                # Ef hermaður leikmanns á núll líf eftir deyr hann
                if hermadurLeikmanns.lif == 0:
                    print(f"Hermaður nr {hermadurLeikmanns.nr} í her {hermadurLeikmanns.herdeild} lét endanlega lífið í þessum bardaga")
                    return None, hermadurTolvu

            elif hermadurLeikmanns.afl == hermadurTolvu.afl:
                print(f"Báðir hermenn eru með jafn mikið afl og því vegna fara báðir þá aftast í sína röð hermanna")
                return hermadurLeikmanns, hermadurTolvu
            
            # Ef hvorugur dó í bardaganum þá returnast báðir
            if hermadurTolvu and hermadurLeikmanns:
                return hermadurLeikmanns, hermadurTolvu       


        def bardagiÞangaðTilAnnarHvorVinnur(valLeikmanns, valTolvu):
            # Ég fann smá glitch sem ég var lengi að leysa úr hérna. Ef 1 er eftir í hvoru liði og þeir eru
            # eru með jafnmikið afl þá lúppar leikurinn endalaust. Þannig ef sú pattstaða kemur upp þá bjó
            # ég til dictionary sem notar nr hermannanna sem key og counter sem value. ef sömu númer etjast
            # á móti hvor öðrum 20 sinnum þá þvinga ég random niðurstöðu milli leikmannanna tveggja.
            
            # Bý til dictionary og stilli hvað margir bardagar 
            teljari_leikir = {}
            hamarkSamaBardaga = 20

            # Á meðan það eru til hermenn í öðru hvoru liðinu
            while valLeikmanns.hermenn and valTolvu.hermenn:

                # Tek sitthvoran leikmanninn úr hermannahópnum
                hermadurLeikmanns = valLeikmanns.hermenn.pop(0)
                hermadurTolvu = valTolvu.hermenn.pop(0)
                
                # Sæki niðurstöðu bardagans
                hermadurLeikmanns, hermadurTolvu = bardagi(hermadurLeikmanns, hermadurTolvu)
                
                # Simple if else - niðurstaða objectanna er annaðhvort til eða objectið er None
                if hermadurLeikmanns and not hermadurTolvu:
                    valLeikmanns.hermenn.append(hermadurLeikmanns)
                elif hermadurTolvu and not hermadurLeikmanns:
                    valTolvu.hermenn.append(hermadurTolvu)
                
                # Þegar leikur fer jafntefli logga ég hann
                else: 
                    # Set einkenni bardagans sem nr vs nr -- tuple sem key
                    einkenni_bardaga = (hermadurLeikmanns.nr, hermadurTolvu.nr)
                    # adda einkenni bardagans inn í teljari_leikir ef hann er ekki þar
                    if einkenni_bardaga not in teljari_leikir:
                        # dict[key] = 0
                        teljari_leikir[einkenni_bardaga] = 0
                    # Hækka teljarann
                    teljari_leikir[einkenni_bardaga] += 1
                    
                    # Ef sami bardaginn er búinn að eiga sér stað 20 sinnum þá vel ég random sigurvegar
                    if teljari_leikir[einkenni_bardaga] >= hamarkSamaBardaga:
                        nidurstadaBardaga = random.choice([hermadurLeikmanns, hermadurTolvu])
                        if nidurstadaBardaga == hermadurLeikmanns:
                            hermadurTolvu.lif -= 1
                            continue
                        else:
                            hermadurLeikmanns.lif -= 1
                            continue
                        
                    # Adda leikmönnum aftur í sinn lista þegar það er jafntefli
                    valLeikmanns.hermenn.append(hermadurLeikmanns)
                    valTolvu.hermenn.append(hermadurTolvu)
                    
            # Athuga með sigurvegara þegar lúppan er búin að komast að niðurstöðu
            if not valLeikmanns.hermenn:
                print("Tölvan vann og þú tapaðir og þú færð ekki súkkulaði!")
            elif not valTolvu.hermenn:
                print("Til hamingju!! Þú vannst og mátt fá þér súkkulaði!")

    # Function sem núllstillir leikinn og leyfir user að velja sína herdeild þegar ég vel að gera það
        def setGame(skipVeljaHerdeild=False):
            teamList.clear()
            nyarHerdeildir = buaTilHerdeildir(teamList)
            if skipVeljaHerdeild == False:
                nidurstada = veljaHerdeild(nyarHerdeildir)
                if nidurstada == None:
                    print("Gekk ekki að velja lið")
                    return None, None
                else:
                    # Tuple returnast sem nidurstada
                    return nidurstada
                
                
        teamList = []
        # Geri valmynd fyrir leikinn
        bardagaleiksvalmynd = True
        while bardagaleiksvalmynd:
            print(" ----- Velkomin/n í bardagaleikinn minn ---- ")
            print("  ----- ----- 1. Velja herdeild ----- ----- ")
            print("  ----- ----- 2. Spila leikinn. ----- -----")
            print("  ---- ---- 3. Leikreglur leiksins ---- ----")
            print("  ---- ---- - 4. Hætta í leiknum - ---- ----")
            bardagaleiksval = input(" ----- Hvað viltu gera ? ----- ")

            # Velja Herdeild
            if bardagaleiksval == "1":
                # Byrja á að nönna bæði liðin just in case
                valLeikmanns, valTolvu = None, None
                # Keyri setGame og vel að ekki skippa að velja herdeild
                valLeikmanns, valTolvu = setGame(skipVeljaHerdeild=False)
                # Ef setGame gekk og lið eru valin prentast út hermennirnir
                if valLeikmanns and valTolvu is not None:
                    print(f"\nÞínir hermenn:\n")
                    for hermenn in valLeikmanns.hermenn:
                        print(hermenn)
                    
            # Spila Leikinn
            elif bardagaleiksval == "2":
                # Ef ekkert lið er valið kemur þetta
                if not valLeikmanns.hermenn or not valTolvu.hermenn:
                    print("Vinsamlegast veldu herdeild fyrst!")
                    continue
                
                # Keyri bardagann þangað til annað hvort liðið vinnur
                sigurvegari = bardagiÞangaðTilAnnarHvorVinnur(valLeikmanns, valTolvu)
                # Endurstilli leikinn en hér skippa ég að velja herdeild
                setGame(skipVeljaHerdeild=True)
                continue

            # Leikreglur     
            elif bardagaleiksval == "3":
                print(f"Leikreglur og leiðbeiningar: \nValinn er fremsti maður úr hvoru liði. Sá sem er með meira aflið vinnur.\n\
Sá sem tapar missir eitt líf og ef hann á 0 líf eftir deyr hann. \n\
Sá sem vinnur fer undantekningalaust aftast í sinni her. \n\
Ef sá sem tapar á eftir líf fer hann líka aftast í sinn her.\n\n\
Pattstaðan: \nTil þess að koma í veg fyrir endalausa lúppu þá skrái ég niður nr hermanna sem mætast en\n\
bara ef það er jafntefli. Þegar þeir hafa barist 20 sinnum þá þvinga ég random sigur milli þeirra.")
                
            # Hætta valmöguleikinn
            elif bardagaleiksval == "4":
                bardagaleiksvalmynd = False
            
            
            
    # Landsliðshópaverkefnið
    elif val == 2:
    

        
        while True:
            print("Veldu 1 til að nota tilbúinn strengjalista")
            print("Veldu 2 til að fá spurninguna hvað eru margir skráðir...")
            print("Veldu 3 til að hætta")
            velja = input("veldu nú")
            while velja not in ["1","2","3"]:
                velja = input("veldu annaðhvort 1,2 eða 3")
                
                
            # Gerði þetta til að hoppa yfir að alltaf stimpla inn nöfn þegar ég er stanslaust keyra kóðann minn þegar hann er í vinnslu
            if velja == "1":
                landslidshopurKarla = ["Gylfi Sigurðsson", "Alfreð Finnbogason", "Aron Gunnarsson", "Hannes Þór Halldórsson", "Birkir Bjarnason"]
                landslidshopurKvenna = ["Dagný Brynjarsdóttir", "Sara Björk Gunnarsdóttir", "Hólmfríður Magnúsdóttir", "Katrín Ómarsdóttir", "Fanndís Friðriksdóttir"]
            
            # Hér er hægt svo sannarlega að stimpla hvað margir eru skráðir og stimpla inn nafn landsliðsmanns
            elif velja == "2":

                landslidshopurKarla = []
                landslidshopurKvenna = []
                
                # Spyr hvað marga skal stimpla inn og keyri lúppu með spurningu jafn oft og stimplað er inn
                spurningKarlar = int(input("Hvað eru margir skráðir í landsliðshóp karla ?"))
                for nr in range(spurningKarlar):
                    nafn = input("Skráðu inn karla landsliðsnafn til að bæta við í strengjalistann")
                    landslidshopurKarla.append(nafn)
                spurningKonur = int(input("Hvað eru margar konur skráðar í landsliðshóp kvenna ?"))
                for x in range(spurningKonur):
                    nafn = input("Skráðu inn konu landsliðsnafn til að bæta í strengjalistann")
                    landslidshopurKvenna.append(nafn)
            print("")
            
            
            # Liður A - Raða listunum í stafrófsröð og prenta út með ; á milli
            print("Liður A - Raða listunum í stafrófsröð og prenta strengina út með ; á milli")
            
            landslidshopurKarla.sort() # Þetta raðar listanum (breytir original listanum)
            landslidshopurKvenna.sort()
            radadurNyrListiHopurkarla = sorted(landslidshopurKarla) # Nýr listi í stafrófsröð
            radadurNyrListiHopurKvenna = sorted(landslidshopurKvenna)
            
            # Ef x er síðasta gildið þá prenta ég nýja línu
            for x in range(len(landslidshopurKarla)):
                if x == len(landslidshopurKarla) -1:
                    print(landslidshopurKarla[x], end="\n")
                else:
                    print(landslidshopurKarla[x], end=";")
            
            # Geri sama fyrir kvenna hópinn
            for x in range(len(landslidshopurKvenna)):
                if x == len(landslidshopurKvenna) -1:
                    print(landslidshopurKvenna[x], end="\n")
                else:
                    print(landslidshopurKvenna[x], end=";")
            print("")
            
            # Liður B - Listi af listum - Strengur sem nafn og tala sem mörk    
            print("Liður B - Búa til lista af listum - Str sem nafn og int sem mörk")
            
            ListiAfListumKarlar = []
            ListiAfListumKonur = []
            
            for nafn in landslidshopurKarla:
                listiNafnOgMork = []
                skorudMork = random.randint(1,10)
                listiNafnOgMork.append(nafn)
                listiNafnOgMork.append(skorudMork)
                ListiAfListumKarlar.append(listiNafnOgMork)
            for nafn in landslidshopurKvenna:
                listiNafnOgMork = []
                skorudMork = random.randint(1,10)
                listiNafnOgMork.append(nafn)
                listiNafnOgMork.append(skorudMork)
                ListiAfListumKonur.append(listiNafnOgMork)
                
            print(ListiAfListumKarlar)
            print(ListiAfListumKonur)
            
            
            # Liður C - Skrifa út hvað mörg mörk skoruð
            print("\nLiður - C Skrifa út hvað mörg mörk skoruð")
            skorudMorkKarlar = 0
            for listi in ListiAfListumKarlar:
                for x in range(len(listi)):
                    if x == 1:
                        mark = listi[x]
                        skorudMorkKarlar += mark
            print("Skoruð mörk hjá körlum eru: ", skorudMorkKarlar)
            
            skorudMorkKonur = 0
            for listi in ListiAfListumKonur:
                for x in range(len(listi)):
                    if x == 1:
                        mark = listi[x]
                        skorudMorkKonur += mark
            print("Skoruð mörk hjá konum eru: ", skorudMorkKonur)
                 

            # Liður D - Finna alla karla sem eru með 2+ mörk
            print("\nLiður D - Finna alla karla sem hafa skorað 2 mörk eða fleiri")
            
            dictKarlarMork = {}
            for listi in ListiAfListumKarlar:
                for x in range(len(listi)):
                    if x == 1:
                        nafnKarls = listi[0]
                        mark = listi[x]
                        if mark >= 2:
                            dictKarlarMork[nafnKarls] = mark
            print("Dictionary með mörkin sem value og nafnið sem key: ", dictKarlarMork)   
            print("")
            break
        
        
    # Hin ýmsu föll
    elif val == 3:
        while True:
            print("A. Fall sem finnur flatarmál fimmhyrnings")
            print("B. Fall sem tekur inn óákveðin fjölda nafna(ekki í lista)")
            print("C. Finnur rúmmál sívalnings með því að taka inn radius og hæð sem færibreytur")
            valFall = input("Stimplaðu inn A, B eða C og veldu 9 til að hætta")
            while valFall not in ["A","B","C","9"]:
                valFall = input("Verður að stimpla inn A, B eða C og veldu 9 til að hætta")     
            
            # Fall sem finnur flatarmál fimmhyrnings
            if valFall == "A":
                def flatarFimm(radius):
                    # Hérna er leiðin frá síðunni sem er í skjalinu okkar
                    flatarmal = (5/2) * radius * math.sin(math.radians(72))
                    return flatarmal
                
                    # Fann þessa leið á netinu líka
                    # flatarmal = (5/4) * (radius**2) / math.tan(math.pi/5)
                
                # nota float því radíus getur allt eins verið kommutala
                radius = float(input("Sláðu inn radíus fimmhyrnings"))
                flatarmal = flatarFimm(radius)
                print(f"Flatarmál fimmhyrningsins með radíus {radius} er {flatarmal:.1f}")
            
            # Fall sem tekur inn óákveðin fjölda nafna
            elif valFall == "B":
                def listiNofn(*nofn):
                    listiNofnFramarEnH = []
                    for nafn in nofn:
                        if nafn[0].upper() < "H":
                            listiNofnFramarEnH.append(nafn)
                    return listiNofnFramarEnH
                
                    # Ef ég geri stafinn upper þá skiptir ekki máli
                    # hvort nafnið sé stimplað inn lower eða upper

                        #stafur = nafn[0]
                        #stafur = stafur.upper()
                        #if stafur < "H": ...

                # Dæmi um notkun:
                listiNofnFramarEnH = listiNofn("Anna", "Gunnar", "Jónas", "Hreiðar")
                
                print(f"Nöfn sem eru á undan H í stafrófinu eru: {listiNofnFramarEnH} - (ég bjó þetta til svo ég þyrfti ekki alltaf að stimpla inn mörg nöfn þegar ég var að prófa kóðann)")
                
                nafnaListi = []
                while True:
                    
                    valSiggu = input("Ef þú vilt slá inn óákveðinn fjölda nafna veldu 1 - annars veldu 2 til að breaka lúppuna")
                    if valSiggu == "1":
                        while True:
                            nafn = input("Sláðu inn óákveðinn fjölda nafna - veldu 2 til að breaka og keyra fallið")
                            if nafn == "2":
                                break
                            nafnaListi.append(nafn)

                        # Þegar valið er "2" þá breakar lúppan og ég dúndra listanum með * inn í fallið og prenta niðurstöðuna
                        listiNofnFramarEnH = listiNofn(*nafnaListi)
                        print(f"Nöfnin sem þú slóst inn og eru á undan H í stafrófinu eru: {listiNofnFramarEnH}")
                    elif valSiggu == "2":
                        break
                print("")

                
                
            # Fall sem tekur inn radíus og hæð og reiknar út rúmmál sívalnings
            elif valFall == "C":
                # Nota math.pi * radíus í öðru * hæð
                def rummalSivalnings(radius, hæð):
                    rummal = math.pi * radius**2 * hæð
                    return rummal
                
                # Nota float því radíus er mjög oft kommutala
                radius = float(input("Sláðu inn radíus sívalningsins: "))
                hæð = float(input("Sláðu inn hæð sívalningsins: "))
                
                # Niðurstaða
                flatarmal = rummalSivalnings(radius, hæð)
                print(f"Rúmmál sívalningsins með radíus {radius} og hæð {hæð} er {flatarmal:.1f}")
            
            elif valFall == "9":
                break

    
    
    
    # Föll sem lesa streng
    elif val == 4:
        while True:
            print("A. Lesa inn streng eða nafn til að víxla stöfum")
            print("B. - Lesa inn streng og snúa pörtum við")
            print("Sláðu inn bókstaf í upper eða veldu 9 til að hætta")
            valFall2 = input("Veldu nú: ")
            while valFall2 not in ["A","B","9"]:
                valFall2 = input("Verður að velja A eða B. Veldu 9 til að hætta - Ath uppercase : ")
            
            # Liður 4 - Fall A - Víxla hverjum 2 stöfum og setja í hástafi
            if valFall2 == "A":
                
                strengur = input("Sláðu inn textastreng eða nafn: ")
                strengurUpper = strengur.upper()
                nyrStrengur = ""
                
                # Lúppa í gegnum strenginn - start, stop, step (x=0,x=2,x=4...)
                for x in range(0, len(strengurUpper), 2):
                    tveirStafir = strengurUpper[x:x+2]
                    reversedTveirStafir = tveirStafir[::-1]
                    nyrStrengur += reversedTveirStafir
                
                # Útkoman
                print(f"\nÚtkoma : {nyrStrengur}\n")
                    
            elif valFall2 == "B":
                strengur = input("Sláðu inn textastreng eða nafn: ")
                
                # Skulum kalla lengd heiltölu deilt með 2, miðju
                midja = len(strengur) // 2
                
                # Index telur frá 0 en len telur frá 1.
                
                # Ef lengd strengsins er oddatala
                if len(strengur) % 2 == 1:
                    fyrriPartur = strengur[0:midja]
                    # Heiltöludeiling af td 7 er 3 - Þá er midja alltaf miðjustafurinn
                    midjuStafur = strengur[midja]
                    # Skippa yfir miðjustafinn svona
                    seinniPartur = strengur[midja+1:]
                    # Skeyti saman pörtunum í nýjan streng
                    utkoma =  fyrriPartur[::-1] + midjuStafur + seinniPartur[::-1]
                    
                    print(f"\nLengd orðsins er oddatala.\nÚtkoma víxlunar: {utkoma}\n")
                    
                else: # Geri mjög svipað fyrir orð sem er slétt tala
                    fyrriPartur = strengur[0:midja]
                    seinniPartur = strengur[midja:]
                    nyrStrengur = fyrriPartur[::-1] + seinniPartur[::-1]
                    
                    # Útkoman
                    print(f"\nLengd orðsins er slétt tala. \nÚtkoma víxlunar: {nyrStrengur}\n")
                    
                    # Þetta er fyrir mig til að sjá hvort ég gerði rétt
                    print(f"fyrripartur strengs = {fyrriPartur}")
                    print(f"Seinnipartur strengs = {seinniPartur}\n")
                    
            # Hætta valmöguleikinn
            elif valFall2 == "9":
                break
    
    
    # Partur 5 - Textaskráin og föll sem vinna með og úr henni
    elif val == 5: # Ég valdi að nota kommu sem seperator
        
        # Byrja á að skrifa tölurnar inn í skrá með kommu á milli
        listiTolur = [2**x for x in range(1,21)]
        
        def skrifa_i_skra(listiTolur):
            with open("pythonVerkefniFiles/tolur.txt", "w", encoding="utf-8") as file:
                file.write(",".join(map(str, listiTolur)))
                
        # Keyri fallið strax
        skrifa_i_skra(listiTolur)

        # Þegar valið er 5 úr menu keyrist þessi print lína
        print(f"\nTölur skrifaðar! tölur frá 2-20, allar í öðru veldi. Hér er listinn sem var skrifað frá : \n{listiTolur}\n")            

        # Liður A - Fall sem les skránna og setur í lista
        def lesa_ur_skra_i_lista():
            listiTolurUrSkra = []
            with open("pythonVerkefniFiles/tolur.txt", "r") as file:
                tolur = file.read().split(",")
                for tala in tolur:
                    # þetta strippar allt frá (þarf svosem ekki því talan er strengur og ég splittaði með ",")
                    strippudTala = tala.strip() # ég var með x = x.strip(",") en hitt virkar betur
                    listiTolurUrSkra.append(int(strippudTala))
            return listiTolurUrSkra             
        #Keyri fallið svo ég geti notað listann í verkefninu
        listiTolurUrSkra = lesa_ur_skra_i_lista()

        
        # Liður B - Fall sem tekur inn listann sem færibreytu. Prenta út 10 tölur í línu
        def listiSemFaeribreyta(listiTolurUrSkra):
            print("\nLiður B - 10 tölur í línu með bili á milli :")
            for x in range(len(listiTolurUrSkra)):
                # Hreinsa upp bilið í enda línunnar svona
                if x != 9 or x != 19:
                    print(listiTolur[x], end=" ")
                else:
                    print(listiTolur[x])
                # Geri nýja línu eftir 10 útprentanir
                if (x+1) % 10 == 0:
                    print()
  
        # Liður C - 1 - Föll og fleira sem tengist tölunni 6
        def finnaTolurSemEndaASex(listiTolurUrSkra):
            listiTalan6 = []
            for tala in listiTolurUrSkra:
                if tala % 10 == 6:
                    listiTalan6.append(tala)
            # Get líka notað list comprehension í þetta sem væri svona:
            # listiTalan6 = [tala for tala in listiTolurUrskra if tala % 10 == 6]
            return listiTalan6
        
        # Keyri þetta hér svo hægt sé að keyra þennan lið úr valmyndinni
        listiTalan6 = finnaTolurSemEndaASex(listiTolurUrSkra)
        
        # Liður C - 2 - Fall sem skrifar tölurnar sem enda á 6 frá listanum sínum í aðra skrá
        def skrifa_tolur_6_i_skra(listiTalan6):
            try:
                with open("pythonVerkefniFiles/tolurSemEndaA_6.txt", "w") as file:
                    file.write(",".join(map(str, listiTalan6)))
                return True
            
            # Er að kynna mér meira um villumeðhöndlun en er samt á byrjunarstigi þar
            except Exception as error:
                print(f"Það kom upp villa : {error}")
                return False
            
        # Liður C - 3 Fall sem eyðir tölunum sem enda á tölunni 6 úr upprunalegu skránni
        def delAllNumbersEndingOn6FromOriginalFile():
            geymsluListi = []
            try:
                with open("pythonVerkefniFiles/tolur.txt","r") as file:
                    tolurUrSkra = file.read().split(",")
                    for strTala in tolurUrSkra:
                        if not strTala.strip().endswith("6"):
                            geymsluListi.append(strTala)
                with open("pythonVerkefniFiles/tolur.txt", "w") as file:
                        file.write(",".join(map(str, geymsluListi)))
                return True        
            # Er að kynna mér meira um villumeðhöndlun en er samt á byrjunarstigi þar
            except Exception as error:
                print(f"Það kom upp villa : {error}")
                return False
                        
      
        # Geri valmynd                        
        while True:
            print("Skráarverkefnið mikla! - Stimplaðu inn bókstaf í upper til að velja")
            print("Liður A - Fall sem les skránna og setur í lista og prentar út listann")
            print("Liður B - Fall sem tekur inn lista sem færibreytur prentar hann út með bil milli talna og 10 tölur í línu")
            print("Liður C - Fall sem finnur tölur sem enda á 6 og fall sem eyðir þessum tölum úr upprunalegu skránni")
            print("Liður D - Lesa úr báðum skrám og prenta út hvora fyrir sig")
            print("Liður E - Dictionary úr annarri skránni sem key er 1-* og gildi er tölurnar í skránni")
            print(" --- Veldu 9 til að hætta --- ")
            valLidur5 = input("Veldu hvað þú vilt gera : ")
            while valLidur5 not in ["A","B","C","D","E","9"]:
                valLidur5 = input("Verður að velja (veldu 9 til að hætta) : ")
            
            # Liður A - Fall sem les skránna og setur í lista og prentar út listann
            if valLidur5 == "A":
                print(f"\nHér er int listi með tölunum úr skránni : \n{listiTolurUrSkra}\n")    
                listiTolurUrSkra = lesa_ur_skra_i_lista()
            
            # Liður B - Fall með listann úr skránni sem færibreytu
            elif valLidur5 == "B":
                listiSemFaeribreyta(listiTolurUrSkra)
                print()

            # Liður C - Föll og fleira sem tengist tölunni 6
            elif valLidur5 == "C":
                # Næ í fallið sem lætur allar tölur sem enda á 6 í lista
                listiTalan6 = finnaTolurSemEndaASex(listiTolurUrSkra)
                print(f"\nHér eru allar tölurnar sem enda á 6 prentaðar úr listanum sínum: \n{listiTalan6}\n")
                
                # Keyri fallið sem skrifar tölurnar sem enda á 6 í sér skrá
                skrifaTolur6 = skrifa_tolur_6_i_skra(listiTalan6)
                if skrifaTolur6: 
                    print("Það tókst að skrifa tölurnar sem enda á 6 í skránna\n")
                else:
                    print("Það tókst ekki að skrifa tölurnar 6 í sér skrá\n")
                
                # Keyri fallið sem eyðir tölunum sem enda á tölunni 6 úr upprunalegu skránni
                boolDel = delAllNumbersEndingOn6FromOriginalFile()
                if boolDel:
                    print("Það tókst að eyða tölunum sem enda á tölustafnum 6 úr upprunalegu skránni\n")
                else:
                    print("Það tókst ekki að eyða tölunum sem enda á tölunni 6 úr upprunalegu skránni\n")   
            
            # Liður D - Prenta út báðar skrárnar
            elif valLidur5 == "D":
                with open("pythonVerkefniFiles/tolur.txt", "r") as file:
                    tolur = file.read().split(",")
                    print("\nHérna koma tölurnar úr tolur.txt : ")
                    for tala in tolur:
                        print(tala, end=" ")
                    print()
                with open("pythonVerkefniFiles/tolurSemEndaA_6.txt", "r") as file:
                    tolurUr6Skranni = file.read().split(",")
                    print("\nHérna koma tölurnar úr tolurSemEndaA_6.txt")
                    for tala in tolurUr6Skranni:
                        print(tala, end=" ")
                    print()
                print()
            
            
            # Liður E - Búa til dictionary úr skránni og prenta það út línu fyrir línu
            elif valLidur5 == "E":
                
                def buaTilDictUrSkranni():
                    try:
                        dictUrSkranni = {}
                        with open("pythonVerkefniFiles/tolur.txt", "r") as file:
                            tolurListi = file.read().split(",")
                            # Með því að nota enumerate get ég notað indexið úr því sem key og töluna sem gildi
                            for x, tala in enumerate(tolurListi):
                                dictUrSkranni[x+1] = tala
                        return dictUrSkranni
                    # Er að kynna mér meira um villumeðhöndlun en er samt á byrjunarstigi þar
                    except Exception as error:
                        print(f"Það kom upp villa : {error}")
                        return False
                
                dictUrSkranni = buaTilDictUrSkranni()
                if dictUrSkranni:
                    print(f"\nÞað tókst að búa til dictionary úr skránni og hér er það línu fyrir línu : \n")
                else:
                    print(f"\nÞað tókst ekki að búa til dictionary úr skánni. Einhver villa kom upp!")
                
                # Þetta er góð leið til að iterate yfir dictionary
                for key, value in dictUrSkranni.items():
                    print(f"Key: {key} - Value: {value}")
                print()      

            # Hætta valmöguleikinn
            elif valLidur5 == "9":
                break

    # Hætta valmöguleikinn
    elif val == 6:
        break
    else:
        print("Þú valdir ekki rétt")
print("Takk fyrir nota forritið mitt ! :)")