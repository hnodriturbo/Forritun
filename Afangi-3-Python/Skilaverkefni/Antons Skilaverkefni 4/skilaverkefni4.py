# Skilaverkefni 3 - Liður 2
# 22/09/2023 - 12/10/2023
# Anton Smári Gunnarsson

from spilastokkur import Spilastokkur
from spil import Spil
from random import randint

stigSpilari = 0
stigTolva = 0

# Hér er randomly valið hver byrjar að gefa, 0 þýðir að tölvan gefur en 1 þýðir að spilari gefur
hverGefur = randint(0, 1)

print("Þú ert að spila Marías á móti tölvunni!")
# Spil er keyrt í endalausri while lykkju þar til valið er sérstaklega að hætta að spila
while True:
    # Byrja nýtt spil / nýja lotu
    print("Ný umferð byrjar!")
    if hverGefur == 0:
        print("Tölvan gefur þessa umferð!")
    else:
        print("Þú gefur þessa umferð!")

    # Stigin fyrir hverja lotu eru núllsett í byrjun lotunnar
    stigLotaSpilari = 0
    stigLotaTolva = 0

    # Hér er spilastokkurinn búinn til með 52 spilum og síðan er fall notað til þess að fjarlægja ónothæf spil og í lok er stokkað
    spilastokkur = Spilastokkur([])
    spilastokkur.fjarlaegjaOnotudSpil()
    spilastokkur.stokkaSpil()

    # Allir spilabunkar eru stilltir sem None áður en þeir eru notaðir af viti
    # Ég athuga síðan neðar í kóðanum hvort það þarf að búa til nýtt tilvik af Spilastokkur fyrir hvern af þessum bunkum
    hendiSpilari = None
    hendiTolva = None
    slagirSpilari = None
    slagirTolva = None
    ruslbunki = None

    # Breytur fyrir hvort það sé hægt að draga, hver gerir fyrst, hvort það sé búið að skipta út trompi og hver vann núverandi slag
    haegtAdDraga = True
    hverGerirFyrst = 1 - hverGefur
    buidAdSkiptaUtTrompi = False
    hverVannSeinastaSlag = -1

    # Þessir listar halda utan um hvort einhver hefur fengið aukastig fyrir hjón eða röð eða alla gosana t.d. og kemur í veg fyrir að það sé tvíreiknað inn í stigin
    tolvaAukastig = []
    spilariAukastig = []

    # Þetta er upphafsgjöfin, listunum er síðan úthlutað í takt við hvor gaf
    upphafsgjof = [[], []]
    for x in range(5):
        upphafsgjof[0].append(spilastokkur.dragaSpilEfstUrSpilabunka())
        upphafsgjof[1].append(spilastokkur.dragaSpilEfstUrSpilabunka())

    if hverGefur == 0:
        hendiSpilari = Spilastokkur(upphafsgjof[0])
        hendiTolva = Spilastokkur(upphafsgjof[1])
    else:
        hendiTolva = Spilastokkur(upphafsgjof[0])
        hendiSpilari = Spilastokkur(upphafsgjof[1])

    """
    # TODO: REMOVE THIS LINE OF CODE BELOW
    hendiSpilari = Spilastokkur([Spil(11, Spil.HJARTA), Spil(10, Spil.HJARTA), Spil(12, Spil.HJARTA), Spil(13, Spil.HJARTA), Spil(14, Spil.HJARTA)])
    hendiTolva = Spilastokkur([Spil(11, Spil.SPADI), Spil(10, Spil.SPADI), Spil(12, Spil.SPADI), Spil(13, Spil.SPADI), Spil(14, Spil.SPADI)])

    hendiSpilari = Spilastokkur([Spil(7, Spil.HJARTA), Spil(7, Spil.SPADI), Spil(7, Spil.TIGULL), Spil(7, Spil.LAUF), Spil(14, Spil.HJARTA)])
    # TODO: REMOVE THIS LINE OF CODE ABOVE
    """

    # Hér er trompið dregið og sett undir bunkann "snúandi upp"
    spilastokkur.dragaTromp = spilastokkur.dragaSpilEfstUrSpilabunka()
    Spil.TROMP = spilastokkur.dragaTromp.spilaTegund

    # Önnur endalaus while lykkja sem brotnar ekki fyrr en ein lota er búin
    while True:
        # Prenta út hvað er tromp í hverri umferð til minnis og spil á hendi spilara
        print(f"Trompið er {Spil.SORTIR_2[Spil.TROMP]}")
        if not buidAdSkiptaUtTrompi and spilastokkur.dragaTromp.spilaTala != 7:
            print(f"Útskiptanlega trompið er {str(spilastokkur.dragaTromp)}")
        elif spilastokkur.dragaTromp.spilaTala == 7 and buidAdSkiptaUtTrompi:
            print("Það er ekkert útskiptanlegt tromp því það er búið að skipta því út nú þegar...")
        else:
            print("Það er ekkert útskiptanlegt tromp því trompið sem var dregið í upphafi leiks er sjöa...")
        print()

        # Tölvan skiptir sjálfkrafa út tromp 7 fyrir útskiptanlega trompið
        for spil in hendiTolva.spilaListi:
            if spil.spilaTegund == Spil.TROMP and spil.spilaTala == 7 and not buidAdSkiptaUtTrompi:
                print(f"Tölvan skiptir tromp 7 út fyrir neðsta sýnilega útskiptanlega trompinu: {spilastokkur.dragaTromp}")
                hendiTolva.baetaSpiliVidLista(spilastokkur.dragaTromp)
                hendiTolva.notaSpilAfHendi(spil)
                spilastokkur.dragaTromp = spil
                buidAdSkiptaUtTrompi = True

        # Hér sýnir tölvan sjálfkrafa röð, hjón eða alla gosana t.d.
        stig, thegarSynt, synt = hendiTolva.geturSyntSpilFyrirAukastig(hendiTolva.spilaListi)
        if len(stig) > 0:
            for x in range(len(stig)):
                if synt[x] == True:
                    print(f"Tölvan sýnir {thegarSynt[x]} og fær þannig {stig[x]} stig")
                    stigLotaTolva += stig[x]

        # Hér byrjar svo spilið fyrir alvöru...
        if hverGerirFyrst == 0:
            print("Tölvan á að setja út fyrst...")
            tolvanSeturUt = hendiTolva.spilaListi[randint(0, len(hendiTolva.spilaListi) - 1)]
            hendiTolva.notaSpilAfHendi(tolvanSeturUt)
            spilariSeturUt, stig, skiptiUtTromp7 = hendiSpilari.setjaUtSpil(tolvanSeturUt, spilastokkur)
            stigLotaSpilari += stig
            hendiSpilari.notaSpilAfHendi(spilariSeturUt)
            print(f"Þú setur út {spilariSeturUt}")

            hverVannSeinastaSlag = tolvanSeturUt.hverVinnur(spilariSeturUt)
        else:
            print("Þú á að setja út fyrst...")
            spilariSeturUt, stig, skiptiUtTromp7 = hendiSpilari.setjaUtSpil(None, spilastokkur)
            stigLotaSpilari += stig
            hendiSpilari.notaSpilAfHendi(spilariSeturUt)
            print(f"Þú setur út {spilariSeturUt}")

            # Hér er listi yfir spil sem tölvan má setja út búinn til
            spilSemTolvaMaSetjaUt = list(filter(lambda spil: spil.spilaTegund == spilariSeturUt.spilaTegund, hendiTolva.spilaListi))
            # Ef engin spil eru á listanum þá þarf tölvan ekki að svara í sömu mynt / bekinna
            if not spilSemTolvaMaSetjaUt:
                spilSemTolvaMaSetjaUt = hendiTolva.spilaListi
            # Annað filter fall notað til þess að finna hvaða spil myndu vinna slaginn og þau sett á nýjan lista
            spilSemVinnaSlaginn = list(filter(lambda spil: spilariSeturUt.hverVinnur(spil) == 1, spilSemTolvaMaSetjaUt))
            # Ef engin spil eru í þeim lista er breytan endurnotuð fyrir spilSemTolvanMaSetjaUt breytuna sem var skilgreind hér fyrir ofan
            if not spilSemVinnaSlaginn:
                spilSemVinnaSlaginn = spilSemTolvaMaSetjaUt
            # Að lokum er min fall notað með lambda expressioni til þess að finna minnsta mögulega spilið til þess að setja út á móti
            tolvanSeturUt = min(spilSemVinnaSlaginn, key=lambda x: x.spilaTala)
            hendiTolva.notaSpilAfHendi(tolvanSeturUt)
            print(f"Tölvan setur út {tolvanSeturUt}")

            hverVannSeinastaSlag = spilariSeturUt.hverVinnur(tolvanSeturUt)
            # Þetta(1 - hverVannSeinastaSlag) er vegna þess að fallið hverVinnur skilar bara hvor vann miðað við hver gerði fyrst
            # Hægt er að nota niðurstöðuna beint ef tölvan gerir fyrst en andstæðuna þarf að nota þegar spilari setur út fyrst
            hverVannSeinastaSlag = 1 - hverVannSeinastaSlag
        if hverVannSeinastaSlag == 0:
            print("Tölvan vann þennan slag")
        else:
            print("Þú vannst þennan slag")
        print()

        if skiptiUtTromp7:
            buidAdSkiptaUtTrompi = True

        slagur = []
        rusl = []
        # Ef stig eru 0 er spil sett í ruslakistuna annars í slag lista
        if int(tolvanSeturUt) == 0:
            rusl.append(tolvanSeturUt)
        else:
            slagur.append(tolvanSeturUt)
        if int(spilariSeturUt) == 0:
            rusl.append(spilariSeturUt)
        else:
            slagur.append(spilariSeturUt)

        if rusl and not ruslbunki:
            ruslbunki = Spilastokkur(rusl)
        elif rusl:
            ruslbunki.baetaSpiliVidLista(rusl)

        # Ef tölvan vann seinasta slag
        if hverVannSeinastaSlag == 0:
            if slagur and not slagirTolva:
                slagirTolva = Spilastokkur(slagur)
            elif slagur:
                slagirTolva.baetaSpiliVidLista(slagur)
        # Ef þú vannst seinasta slag
        else:
            if slagur and not slagirSpilari:
                slagirSpilari = Spilastokkur(slagur)
            elif slagur:
                slagirSpilari.baetaSpiliVidLista(slagur)
        hverGerirFyrst = hverVannSeinastaSlag

        # Í lok hverrar umferðar dregur sá sem vann seinasta slag fyrst úr spilabunkanum
        if haegtAdDraga:
            fyrstaDregidSpil = spilastokkur.dragaSpilEfstUrSpilabunka()
            annadDregidSpil = spilastokkur.dragaSpilEfstUrSpilabunka()
            # Ef annað dregið spil er None þýðir það að bunkinn sé búinn og þá þarf að draga trompið í borði
            if annadDregidSpil == None:
                haegtAdDraga = False
                annadDregidSpil = spilastokkur.dragaTromp

            if hverVannSeinastaSlag == 0:
                print("Tölvan dregur...")
                hendiTolva.baetaSpiliVidLista(fyrstaDregidSpil)
                hendiSpilari.baetaSpiliVidLista(annadDregidSpil)
                print(f"Þú dregur svo líka: {str(annadDregidSpil)}")
            else:
                hendiSpilari.baetaSpiliVidLista(fyrstaDregidSpil)
                hendiTolva.baetaSpiliVidLista(annadDregidSpil)
                print(f"Þú dregur: {str(fyrstaDregidSpil)}")
                print("Tölvan dregur svo líka...")
                if annadDregidSpil == spilastokkur.dragaTromp:
                    print(f"Tölvan dró seinasta spilið í bunkanum sem er útskiptanlega {str(spilastokkur.dragaTromp)}")
        else:
            print("Spilabunkinn er tómur og ekki er hægt að draga lengur...")
        print()

        # Ef allir spilastokkar/bunkar/söfn eru tóm er þessi lota á enda
        if int(spilastokkur) == 0 and int(hendiTolva) == 0 and int(hendiSpilari) == 0:
            print("Spilastokkurinn er tómur og öll spil af hendi eru búin, þessi lota er búin!")
            break

    # Hér er byrjað að reikna út stigin fyrir liðna lotu
    if hverVannSeinastaSlag == 0:
        stigLotaTolva += 20
    else:
        stigLotaSpilari += 20

    for spil in slagirTolva.spilaListi:
        stigLotaTolva += int(spil)

    for spil in slagirSpilari.spilaListi:
        stigLotaSpilari += int(spil)

    # Hér er skoðað hvor aðilinn er með hærri stig til að prenta út sigurvegara liðinnar lotu
    if stigLotaTolva > stigLotaSpilari:
        print("Tölvan vinnur þessa lotu!")
    elif stigLotaSpilari > stigLotaTolva:
        print("Þú vinnur þessa lotu!!!")
    else:
        print("Þessi lota endaði með jafntefli, eins ólíklegt og það er...")

    # Heildarstig lögð saman
    stigSpilari += stigLotaSpilari
    stigTolva += stigLotaTolva

    print("Uppýsingar um stig þessarar lotu og heildarstig:")
    # Prenta út samtals stig beggja aðila og stig þessarar lotu
    print("Aðili   | Stig Samtals | Stig þessarar lotu")
    print(f"Spilari | {str(stigSpilari)} | {str(stigLotaSpilari)}")
    print(f"Tölva   | {str(stigTolva)} | {str(stigLotaTolva)}")
    # Þetta snýr tölunni sem ákvarðar hver gefur við frá 0 yfir í 1 eða öfugt
    hverGefur = 1 - hverGefur

    # Gefa spilara færi á að hætta í spilinu ef hann kýs svo
    veljaAdHaetta = input("Veldu Q/E til þess að hætta að spila(eða skrifaðu hætta): ")
    if veljaAdHaetta.lower() == "q" or veljaAdHaetta.lower() == "e" or veljaAdHaetta.lower() == "hætta":
        print("Notandi velur að hætta!")
        break