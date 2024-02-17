########## Hreiðar Pétursson ###########
  ######### Skilaverkefni 4 ##########
 ########### Október 2023 ###########


import random



class spil:
    # Þar sem sum spil gefa stig geri ég dictionary utan um það innan í klasanum
    stig = {
        10: 10,
        11: 20,
        12: 30,
        13: 40,
        14: 50
    }
    
    def __init__(self, spilategund, spilanumer, spilanafn) -> None:
        self.spilategund = spilategund
        self.spilanumer = spilanumer
        self._spilanafn = spilanafn
    
    # Fékk smá hjálp frá netinu með þetta
    @property
    def spilanafn(self):
        """ Gerði þetta til að það prentist "(tromp spil)" fyrir aftan öll spil sem eru tromp spil """
        tromp_skilabod = " (tromp spil)" if self.spilategund == tromp_tegund else ""
        return f"{self._spilanafn}{tromp_skilabod}"
    
    # Fékk smá hjálp fyrir þetta
    def stig_fyrir_spil(self):
        return spil.stig.get(self.spilanumer, 0)
    
    def __str__(self) -> str:
        return f"\nSpilanafn: {self.spilanafn}\nSpilategund: {self.spilategund}\nSpilanúmer: {self.spilanumer}"
    
    
    

spilanofn = [
    # Hjarta (Hearts)
    "Hjarta Ás", "Hjarta Tvistur", "Hjarta Þristur", "Hjarta Fjarki", 
    "Hjarta Fimma", "Hjarta Sexa", "Hjarta Sjöa", "Hjarta Átta", 
    "Hjarta Nía", "Hjarta Tía", "Hjarta Gosi", "Hjarta Drottning", "Hjarta Kóngur",
    
    # Spaða (Spades)
    "Spaða Ás", "Spaða Tvistur", "Spaða Þristur", "Spaða Fjarki", 
    "Spaða Fimma", "Spaða Sexa", "Spaða Sjöa", "Spaða Átta", 
    "Spaða Nía", "Spaða Tía", "Spaða Gosi", "Spaða Drottning", "Spaða Kóngur",
    
    # Tígul (Diamonds)
    "Tígul Ás", "Tígul Tvistur", "Tígul Þristur", "Tígul Fjarki", 
    "Tígul Fimma", "Tígul Sexa", "Tígul Sjöa", "Tígul Átta", 
    "Tígul Nía", "Tígul Tía", "Tígul Gosi", "Tígul Drottning", "Tígul Kóngur",
    
    # Laufa (Clubs)
    "Laufa Ás", "Laufa Tvistur", "Laufa Þristur", "Laufa Fjarki", 
    "Laufa Fimma", "Laufa Sexa", "Laufa Sjöa", "Laufa Átta", 
    "Laufa Nía", "Laufa Tía", "Laufa Gosi", "Laufa Drottning", "Laufa Kóngur"
]
spilanumer = [14,2,3,4,5,6,7,8,9,10,11,12,13]

# Eitthvað svaka list comprehension til að splitta stóra nafna listanum í fjóra lista eftir sortum
hjarta, spadi, tigull, lauf = [spilanofn[i:i + 13] for i in range(0, len(spilanofn), 13)]

# Set nafn sortar sem key og lista af nöfnunum sem value
spilategundir_og_nofn = {
    "Hjarta": hjarta,
    "Spaði": spadi,
    "Tígull": tigull,
    "Lauf": lauf,
}


# Fallið sem býr til spilastokkinn
def bua_til_spil():
    spilastokkur = []

    for tegund, nofn in spilategundir_og_nofn.items():
        for i, nafn in enumerate(nofn):
            numer = spilanumer[i]
            spilastokkur.append(spil(tegund, numer, nafn))
    
    return spilastokkur

""" ----------------------------------------------------------------------------- """
""" ---------- Checka á sjö - Fallið gengur bæði fyrir tölvu og mann ------------ """
""" ----------------------------------------------------------------------------- """
def check_for_7(spilahendi, spilastokkur, valid_spil=None):
    global tromp_spil
    global tromp_tegund
    
    if valid_spil:
        if valid_spil.spilanumer == 7 and valid_spil.spilategund == tromp_tegund:
            # Tek spilið af hendinni
            spilahendi.remove(spil)
            # Tek upp spilið og set á hendi
            spilahendi.append(tromp_spil)
            # Set spilið aftur í stokkinn
            spilastokkur.append(spil)
            # Geri spilið að hinu nýja spili sem snýr upp (tromp spilið)
            tromp_spil = spil

            # Skila fallinu True þar sem skipt hefur verið um spil
            return True
        
    else:
        for spil in spilahendi:
            if spil.spilanumer == 7 and spil.spilategund == tromp_tegund:
                # Tek spilið af hendinni
                spilahendi.remove(spil)
                # Tek upp spilið og set á hendi
                spilahendi.append(tromp_spil)
                # Set spilið aftur í stokkinn
                spilastokkur.append(spil)
                # Geri spilið að hinu nýja spili sem snýr upp (tromp spilið)
                tromp_spil = spil

                # Skila fallinu True þar sem skipt hefur verið um spil
                return True
        
    # Skila fallinu false ef gekk ekki að skipta um spil
    return False
    
    
    
    
    
""" ----------------------------------------------------------------------------- """
""" ------- Checka hjón og tromp - Fallið gengur bæði fyrir tölvu og mann ------- """
""" ----------------------------------------------------------------------------- """       
def check_samsetningar(spilahendi, spilari):
    global syndar_samsetningar
    global skuld_madur
    global skuld_tolva
    
    stig = 0
    skilabod = []
    
    # Byrja á að athuga með hjónin
    for spil in spilahendi:
        if spil.spilanumer == 12: # Drottning
            for hitt_spil in spilahendi:
                if hitt_spil.spilanumer == 13: # Kóngur
                    # Hérna er ég búinn finna combo drollu og kóng og bý til lista af þeim
                    combo = [spil, hitt_spil]
                    if any([spil in samsetningar for samsetningar in syndar_samsetningar] for spil in combo):
                        skilabod.append(f"\n{spilari} reyndi að sýna hjón sem þegar hafa verið sýnd. Engin stig!")
                    else:
                        if spil.spilategund == tromp_tegund and hitt_spil.spilategund == tromp_tegund:
                            stig += 80
                            skilabod.append(f"\n{spilari} sýndi hjón í trompi og fékk 80 stig!")
                        else:
                            stig += 40
                            skilabod.append(f"\n{spilari} sýndi venjuleg hjón og fékk 40 stig!")
                        syndar_samsetningar.append(combo)
    
    # Athuga með röð - Ástæðan fyrir því að ég nota soldið mikið list comprehension og lambda er að ég er að æfa mig sérstaklega í því
    tolur_fyrir_rod = [10,11,12,13,14]
    tolur_a_hendi = sorted([spil for spil in spilahendi if 10 <= spil.spilanumer <= 14], key=lambda x: x.spilanumer)

    if tolur_fyrir_rod == tolur_a_hendi:
        combo = spilahendi
        if any(spil in samsetningar for samsetningar in syndar_samsetningar for spil in spilahendi):
            skilabod.append(f"\n{spilari} reyndi að sýna röð sem þegar hefur verið sýnd. Engin stig!")
        else:
            if all(spil.spilategund == tromp_tegund for spil in spilahendi):
                stig += 300
                skilabod.append(f"\n{spilari} sýndi röð í trompi og fékk 300 stig!")
            else:
                stig += 150
                skilabod.append(f"\n{spilari} sýndi venjulega röð og fékk 150 stig!")
            syndar_samsetningar.append(spilahendi)
    
    # Uppfæri skuld útfrá spilara
    if spilari == "Maður":
        skuld_tolva += stig
        # Ef engin stig þá voru þetta ekki rétt spil
        if stig == 0:
            skilabod.append(f"\nÞessi spil gefa engin stig. Því miður.")
    else:
        skuld_madur += stig

    return skilabod




# --------- Tölvan gerir fallið og logicið fyrir hvaða spil skal spila -------- #
def tolva_gerir(spilahendi_tolvu, spilastokkur, spil_uti=None):
    global tromp_spil
    global tromp_tegund
    # Byrja á að athuga hvort tölvan sé með sjöu af tromp sortinni
    success_skipta_sjöu = check_for_7(spilahendi_tolvu, spilastokkur)
    if success_skipta_sjöu:
        print(f"Tölvan skipti út {tromp_spil.spilanafn} fyrir {spilahendi_tolvu[-1].spilanafn}")
    else:
        # Held ég þurfi ekki tilkynna í hvert skipti sem tölvan getur ekki skipt út sjöu
        # og því vegna set ég bara pass hérna svo kóðinn haldi áfram keyra
        pass

    # Athuga hvort tölvan geti sýnt hjón eða röð
    skilabod = check_samsetningar(spilahendi_tolvu, "Tölva")
    for skilabod in skilabod:
        print(skilabod)
    
    # --------------------------------------------------------------------#
    ### ----------- EF TÖLVAN Á AÐ SVARA OG ÞAÐ ER SPIL ÚTI ----------- ###
    # --------------------------------------------------------------------# 
    if spil_uti is not None:

        # Þetta sækir öll spil tölvu sem eru af sömu sort
        moguleg_spil_tolvu = [spil for spil in spilahendi_tolvu if spil.spilategund == spil_uti.spilategund]
        
        # Ef það finnast möguleg spil af sömu sort
        if moguleg_spil_tolvu:
            # Nota list comprehension til að filtera út hærri spil en er úti
            hærri_spil = [spil for spil in moguleg_spil_tolvu if spil.spilanumer > spil_uti.spilanumer]
            
            # velja lægsta spilið af hærri spilunum ef hærri spil er TRUE, annars velja lægsta spilið af sömu sortinni
            spil_tolvu = min(hærri_spil, key=lambda x: x.spilanumer) if hærri_spil else min(moguleg_spil_tolvu, key=lambda x: x.spilanumer)
                
        # Ef tölvan á ekki spil af sömu sort
        else:
            # Skoða hvort tölvan eigi tromp spil til að trompa
            tromp_spil_tolvu = [spil for spil in spilahendi_tolvu if spil.spilategund == tromp_tegund]
            
            # Ef tölvan á tromp spil velja lægsta tromp spilið og trompa slaginn
            if tromp_spil_tolvu:
                spil_tolvu = min(tromp_spil_tolvu, key=lambda x: x.spilanumer)
                
            # Ef tölvan á ekki tromp spil til að trompa og ekki sömu sort þá spilar hún út lægsta spilinu sínu
            else:
                spil_tolvu = min(spilahendi_tolvu, key=lambda x: x.spilanumer)
    
    
    
    
    # --------------------------------------------------------------------#
    ### ------------ EF TÖLVAN Á AÐ SETJA FYRSTA SPILIÐ ÚT ------------ ###
    # --------------------------------------------------------------------# 
    else:
        print("\nTölvan á að setja út fyrst")
        # Reyni komast hjá því að setja út tromp spilin ef mögulegt er
        ekki_tromp_spil_tolvu = [spil for spil in spilahendi_tolvu if spil.spilategund != tromp_tegund]

        # Ef það eru spil á hendi sem eru ekki tromp spil þá spila út hæðsta spilinu af þeim
        if ekki_tromp_spil_tolvu:
            spil_tolvu = max(ekki_tromp_spil_tolvu, key=lambda x: x.spilanumer)
            
        # Ef tölvan á bara tromp spil þá spila út hæðsta spilinu
        else:
            spil_tolvu = max(spilahendi_tolvu, key=lambda x: x.spilanumer)
    
    
    # Skila völdu spili
    return spil_tolvu
    
    

# --------------------------------------------------------------------#
### ---------------------- Þegar maður gerir ---------------------- ###
# --------------------------------------------------------------------#   
def madur_gerir(spilahendi_manns, spilastokkur, spil_uti=None):
    
    if spil_uti is None:
        print(f"\nÞú átt að setja út fyrst.")
    
    
    while True:
        # Prenta út spilin sem eru á hendinni
        print("\nSpilin þín: \n")
        for i, spil in enumerate(spilahendi_manns):
            print(f"{i+1}. {spil.spilanafn}")
        
        print(f"\n6. Sýna samsetningu")
        print(f"7. Skipta út sjöunni")
        
        val = input("\nVeldu hvaða spil þú vilt spila út :")
    
        # Validate-a hvort það sé örugglega tala stimpluð inn
        if not val.isdigit():
            print("\nVilla. Verður að stimpla inn tölu.")
            continue

        val = int(val)
        
        # Ef leikmaður ákveður að sýna samsetningu (hjón eða röð)
        if val == 6:
            valin_spil_index = input("\nVeldu hvaða spil þú vilt sýna (t.d. '1 3' eða '1 2 3 4 5' )").split()
            valin_spil = [spilahendi_manns[int(index)-1] for index in valin_spil_index]
            
            skilabod = check_samsetningar(valin_spil, "Maður")
            for skilabod in skilabod:
                print(skilabod)
        
        # Ef leikmaður velur að skipta út tromp sjöunni
        elif val == 7:
            valid_spil_index = input("\nVeldu spilið sem þú ætlar að skipta út (verður að vera sjöa af trompi): ")
            if valid_spil_index.isdigit() and 1 <= int(valid_spil_index) <= len(spilahendi_manns):
                valid_spil = spilahendi_manns[int(valid_spil_index)-1]
                if check_for_7(spilahendi_manns, spilastokkur, valid_spil):
                    print("\nÞú hefur skipt út tromp sjöunni.")
                else:
                    print("\nÞað tókst ekki að skipta út spilinu. Gæti verið að þetta hafi ekki verið rétt spil?")
            else:
                print("\nVerður að velja spil sem er á hendinni.")
                continue
            
        
        elif 1 <= val <= len(spilahendi_manns):
            spil_manns = spilahendi_manns[val-1]
        
            # Ef það er spil úti
            if spil_uti is not None:
                # Athuga öll spil á hendi sem eru af sömu sort ef það eru einhver
                sama_sort = [spil for spil in spilahendi_manns if spil.spilategund == spil_uti.spilategund]
                
                # Ef spilari á sömu sort verður spilari að nota sömu sort. Ef hann á ekki sömu sort þá má trompa
                if sama_sort and spil_manns.spilategund != spil_uti.spilategund:
                    print(f"\nÞú verður að nota sömu sort. Möguleg spil þín eru :")
                    for spil in sama_sort:
                        print(spil.spilanafn)
                    continue
                
            return spil_manns
        else:
            print("\nVerður að velja spil sem er á hendinni eða veldu 6 eða 7.")
            
        
        

# Fall sem prentar út útsettu spilin
def prenta_ut_utsett_spil(spil_manns, spil_tolvu, setti_fyrst_ut):
        if setti_fyrst_ut == "Maður":
            print(f"\n-----------------\nÞú settir út : {spil_manns.spilanafn}\nTölvan setti út : {spil_tolvu.spilanafn}\n-----------------")
        else:
            print(f"\n-----------------\nTölvan setti út : {spil_tolvu.spilanafn}\nÞú settir út : {spil_manns.spilanafn}\n-----------------")
            

# Fall sem ákvarðar hver vinnur slaginn
def hver_vinnur_slaginn(spil_manns, spil_tolvu, setti_fyrst_ut):
    # Ef það er sama sort úti þá vinnur hærra spilið
    if spil_manns.spilategund == spil_tolvu.spilategund:
        prenta_ut_utsett_spil(spil_manns, spil_tolvu, setti_fyrst_ut)
        return "Maður" if spil_manns.spilanumer > spil_tolvu.spilanumer else "Tölva"
    
    # Ef spil manns er tromp en hitt ekki þá vinnur maður
    elif spil_manns.spilategund == tromp_tegund:
        prenta_ut_utsett_spil(spil_manns, spil_tolvu, setti_fyrst_ut)
        return "Maður"
    
    # Ef spil tölvu er tromp en hitt ekki þá vinnur tölva
    elif spil_tolvu.spilategund == tromp_tegund:
        prenta_ut_utsett_spil(spil_manns, spil_tolvu, setti_fyrst_ut)
        return "Tölva"
    
    # Ef hvorugt spil er tromp og samt mismunandi sortir úti þá vinnur sá sem setti út fyrst
    prenta_ut_utsett_spil(spil_manns, spil_tolvu, setti_fyrst_ut)
    return setti_fyrst_ut
    
    
    
    
# Fall sem spilar umferðir þangað til spilin eru búin
def spila_umferd(spilahendi_manns, spilahendi_tolvu, spilastokkur, sigurvegari, slagir_manns, slagir_tolvu):
    global tromp_spil
    # Sá sem vann síðasta slaginn setur fyrst út
    setur_fyrst_ut = sigurvegari
    
    print(f"\nTromp spilið sem snýr upp er: {tromp_spil.spilanafn}")
    
    if setur_fyrst_ut == "Tölva":
        spil_tolvu = tolva_gerir(spilahendi_tolvu, spilastokkur)
        print(f"\nTölva setur út: {spil_tolvu.spilanafn}")
        spil_manns = madur_gerir(spilahendi_manns, spilastokkur, spil_uti=spil_tolvu)
        print(f"\nNotandi setur út : {spil_manns.spilanafn}")

    else:
        spil_manns = madur_gerir(spilahendi_manns, spilastokkur)
        print(f"\nNotandi setur út : {spil_manns.spilanafn}")
        spil_tolvu = tolva_gerir(spilahendi_tolvu,spilastokkur, spil_uti=spil_manns)
        print(f"Tölva setur út: {spil_tolvu.spilanafn}")
    
    # Sjá hver vinnur umferðina
    sigurvegari = hver_vinnur_slaginn(spil_manns, spil_tolvu, setur_fyrst_ut)

    if sigurvegari == "Maður":
        print(f"\nÞú vannst þessa umferð!")
    elif sigurvegari == "Tölva":
        print(f"\nTölvan vann þessa umferð!")
    
    # Tek spilin af hendi tölvu og manns
    spilahendi_manns.remove(spil_manns)
    spilahendi_tolvu.remove(spil_tolvu)
    
    # Dreg ný spil og extenda spiluðum spilum sem slagi í slaga listann
    if sigurvegari == "Maður":
        slagir_manns.extend([spil_manns, spil_tolvu])
        draga_spil(spilastokkur, spilahendi_manns)
        draga_spil(spilastokkur, spilahendi_tolvu)
    elif sigurvegari == "Tölva":
        slagir_tolvu.extend([spil_tolvu, spil_manns])
        draga_spil(spilastokkur, spilahendi_tolvu)
        draga_spil(spilastokkur, spilahendi_manns)
            
    return sigurvegari

# Sér fall til að draga spil - síðasta spil dregið er tromp spilið
def draga_spil(spilastokkur, spilahendi):
    global tromp_spil
    if spilastokkur:
        spil = spilastokkur.pop(0)
        spilahendi.append(spil)
    else:
        print(f"Búnkinn er búinn.")

    




# Reikna stigin með því að nota fallið innan í klasanum
def reikna_stig(slagalisti):
    return sum(spil.stig_fyrir_spil() for spil in slagalisti)

def prenta_ut_spil_sem_gefa_stig(slagalisti):
    for spil in slagalisti:
        if spil.spilanumer > 9:
            print(f"{spil.spilanafn} gaf þér {spil.stig_fyrir_spil()} stig")


# Gerði eitt fall fyrir þetta til að einfalda set_up_game() fallið
def klara_spilid(slagir_manns, slagir_tolvu):
    global skuld_madur
    global skuld_tolva
    
    # Reikna stigin út frá spilunum í slaga listunum
    stig_manns = reikna_stig(slagir_manns)
    stig_tolvu = reikna_stig(slagir_tolvu)
    
    
    print(f"\nSpil tölvu sem gáfu stig :\n")
    prenta_ut_spil_sem_gefa_stig(slagir_tolvu)
    
    print(f"\nSpil þín sem gáfu stig :\n")
    prenta_ut_spil_sem_gefa_stig(slagir_manns)
    
    print(f"\nHeildarstig tölvu : {stig_tolvu}")
    print(f"\nÞín heildarstig : {stig_manns}")
    print(f"\nTölvan skuldar þér : {skuld_tolva}")
    print(f"\nÞú skuldar tölvunni : {skuld_madur}")
    
    stig_tolvu += skuld_madur
    stig_tolvu -= skuld_tolva
    
    stig_manns += skuld_tolva
    stig_manns -= skuld_madur
    
    print(f"\nHeildarstig tölvu eftir skuldareikning er : {stig_tolvu}")
    print(f"\nHeildarstig þín eftir skuldareikning er : {stig_manns}")
    
    if stig_manns > stig_tolvu:
        print(f"\nTil hamingju þú hefur unnið spilið ! :)")
    elif stig_manns < stig_tolvu:
        print(f"\nÞví miður tapaðir þú spilinu ! :(")
    elif stig_manns == stig_tolvu:
        print(f"\nÞað ólíklega kom fyrir og spilið endaði sem jafntefli í stigum !")
       
def set_up_game():
    global tromp_spil, tromp_tegund, syndar_samsetningar, skuld_tolva, skuld_madur
    tromp_spil = None
    tromp_tegund = None
    syndar_samsetningar = []
    skuld_tolva = 0
    skuld_madur = 0
    
    # Bý til spilastokk
    spilastokkur = bua_til_spil()
    
    # Nota list comprehension til að taka spil 2-6 úr umferð
    spilastokkur = [spil for spil in spilastokkur if not (2 <= spil.spilanumer <= 6)]
    
    # Stokka spilin
    random.shuffle(spilastokkur)
    
    # Bý til listana
    spilahendi_manns = []
    spilahendi_tolvu = []
    slagir_manns = []
    slagir_tolvu = []
    
    stig_manns = 0
    stig_tolvu = 0
    
    
    
    # Ákvarða eftir leiknúmeri hvor gefur
    for _ in range(5):
        if leiknumer % 2 == 1:
            spilahendi_manns.append(spilastokkur.pop(0))
            spilahendi_tolvu.append(spilastokkur.pop(0))
        else:
            spilahendi_tolvu.append(spilastokkur.pop(0))
            spilahendi_manns.append(spilastokkur.pop(0))
            
    # Sá sem fær þessa breytu er sá sem setur fyrst út
    sigurvegari = random.choice(["Tölva", "Maður"])
    
    # Tek efsta spilið og það er svokallaða tromp_spil
    tromp_spil = spilastokkur.pop(0)
    # Ákvarða tromp tegundina útfrá tromp_spil
    tromp_tegund = tromp_spil.spilategund 
    # Prenta út upplýsingar er þetta varðar
    print(f"\nTromp í þessum leik er: {tromp_spil.spilategund} - {tromp_spil.spilanafn} snýr upp.")
    # Set tromp_spil aftast í stokkinn til að vera dregið síðast
    spilastokkur.append(tromp_spil)
    
    # Spila þangað til báðar hendur eru tómar
    while spilahendi_manns and spilahendi_tolvu:
        # Assuming sigurvegari is the winner of the last round
        sigurvegari = spila_umferd(spilahendi_manns, spilahendi_tolvu, spilastokkur, sigurvegari, slagir_manns, slagir_tolvu)

        # Geymi hver fékk síðasta slaginn
        sidasti_slagur = sigurvegari
        
    print("\nTil hamingju! Þú kláraðir spilið og núna verða stigin þín og tölvunnar reiknuð.")

    # Extra 20 stig fyrir þann sem fékk síðasta slaginn
    if sidasti_slagur == "Maður":
        stig_manns += 20
        print(f"Þú fékkst auka 20 stig fyrir að vinna síðasta slaginn")
    elif sidasti_slagur == "Tölva":
        stig_tolvu += 20
        print(f"Tölvan fékk auka 20 stig fyrir að vinna síðasta slaginn")
        
    # Prenta út spilin sem gáfu stig og sýna heildarstig og sigurvegara
    klara_spilid(slagir_manns, slagir_tolvu)



leiknumer = 0




try:
        
    while True:

        print("\n1. Spila Marias")
        print("0. Hætta")

        val = input("\nHvað viltu gera?")

        if val == "1":
            set_up_game()

        elif val == "0":
            break
        
        else:
            print("\nþú hefur ekki valið rétt")

    print("\nTakk fyrir að nota forritið mitt")

except Exception as error:
    print(f"\nÞað hefur komið upp einhver villa. Gripin villa : \n{error}")
    