########## Hreiðar Pétursson ###########
  ######### Skilaverkefni 1 ##########
 ########### September 2023 ###########

import json

# Þú veist hvernig ég er með skipulagningnu á kóða. Þannig ég ætla búa til tvö föll til að
# Lesa JSON skránna og setja hvert object í lista og annað fall til að skrifa í skránna.
# Til að spara línur gerði ég fall sem notar writeJSON til að skrifa gögnin aftur í skránna.

# Fallið sem les JSON skránna og skilar object lista frá skránni
def readJSON(skraarnafn):
    try:
        with open(skraarnafn, "r", encoding="utf-8") as file:
            data = json.load(file)
            medlimaskra = data["skra"]
    except FileNotFoundError:
        print("Skráin fannst ekki")
    except json.JSONDecodeError:
        print("Það kom upp villa við að decoda JSON gögnin")
    except Exception as error:
        print(f"Það kom upp óvænt villa við að lesa skránna. Gripin villa : \n{error}")
    # Skila lista með objectum úr JSON skránni
    return medlimaskra

# Fallið sem skrifar JSON
def writeJSON(medlimaskra, skraarnafn):
    """ Skrifa meðlimi í JSON skrá """
    data = {'skra': medlimaskra}
    
    # Reyni skrifa gögnin í skránna
    try:
        with open(skraarnafn, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        print(f"Það kom upp óvænt villa við að skrifa í skránna. Gripin villa : \n{error}")
        return False
    
# Skrifa gögnin í skránna (get keyrt þetta til að þurfa ekki skrifa allar þessar línur aftur og aftur)    
def skrifa(medlimaskra):
    success = writeJSON(medlimaskra, "Skilaverk3.json")
    if success:
        print("\nÞað tókst að skrifa gögnin aftur í skránna.")
        return True
    else:
        print("\nÞað gekk ekki að skrifa gögnin í skránna.")
        return False
    
# Fallið sem prentar alla sem eru í skránni út á skipulagðan hátt
def prentaUtAlla():
    # Byrja á að lesa skránna með flotta fallinu mínu
    medlimaskra = readJSON("Skilaverk3.json")
    print("\nÞað tókst að lesa gögnin úr skránni")
    
    # Renni í gegnum listann og prenta út alla á skipulagðan hátt
    print("\nNúna nota ég for lúppu til að prenta út alla frá skránni úr listanum")
    for medlimur in medlimaskra:
        print(f"\n{medlimur['fornafn']} {medlimur['eftirnafn']}, {medlimur['aldur']}, {medlimur['símanúmer']}, {medlimur['heimili']['heimilisfang']}, {medlimur['heimili']['póstfang']} {medlimur['heimili']['bær']}")
    print("\nTókst að prenta út alla. Núna reyni ég skrifa gögnin aftur í skránna")
    
    # Skrifa gögnin aftur í skránna
    skrifa(medlimaskra)
    
    return True
    
# Fallið sem finnur heildaraldur allra sem eru í skránni
def heildaraldur():
    heildaraldur = 0
    
    # Byrja á að lesa skránna með flotta fallinu mínu
    medlimaskra = readJSON("Skilaverk3.json")
    print("\nÞað tókst að lesa gögnin úr skránni")

    print("\nNúna reikna ég heildaraldur allra sem eru í skránni")
    
    for medlimur in medlimaskra:
        aldur = int(medlimur['aldur'])
        heildaraldur += aldur
    
    print("\nTókst að reikna heildaraldur")
    
    # Skrifa gögnin aftur í skránna
    skrifa(medlimaskra)
    
    if heildaraldur > 0:
        return heildaraldur
    else:
        return False

    
# -----------------------------------------------------------------------------
# ----- Hérna koma öll þau föll sem eru notuð við að búa til nýjan meðlim -----
# -----------------------------------------------------------------------------
def faValidInput(spurning, villuskilabod, validation):
    while True:
        try:
            data = input(spurning)
            if validation(data):
                return data
            else:
                raise ValueError(villuskilabod)
        except ValueError as error:
            print(f"Villa: {error}")
            
# Gerði nokkur validation functions til að validate innslegnar upplýsingar um meðlim
def check_alpha(data):
    return data.isalpha()
def check_aldur(data):
    return data.isdigit() and len(data) <= 2
def check_simanumer(data):
    return data.isdigit()
def check_lengd_amk_2(data):
    return len(data) >= 2
def check_postnumer(data):
    return data.isdigit() and len(data) == 3

# Svo kemur fallið hérna sem keyrir prógrammið til að bæta við nýjum meðlim 
def addMember():
    while True:
        print("\nVelkominn í að bæta við nýjum notanda í skránna !")
        print("\nVinsamlegast sláðu inn gildar upplýsingar í hverjum lið.")
        
        fornafn = faValidInput("\nSláðu inn fornafn : ", "Verður að slá inn eingöngu bókstafi.", check_alpha)
        eftirnafn = faValidInput("\nSláðu inn eftirnafn : ", "Verður að slá inn eingöngu bókstafi.", check_alpha)
        aldur = faValidInput("\nSláðu inn aldur : ", "Verður að slá inn eingöngu tölur og má mest vera tveir tölustafir.", check_aldur)
        simanumer = faValidInput("\nSláðu inn símanúmer : ", "Verður að slá inn eingöngu tölustafi.\nSláðu inn símanúmer : ", check_simanumer)
        heimilisfang = faValidInput("\nSláðu inn heimilisfang : ", "Lengd heimilisfangs verður að vera amk 2 stafir að lengd.", check_lengd_amk_2)
        baer = faValidInput("\nSláðu inn bæjarfélag : ", "Lengd bæjarfélags verður að vera amk 2 stafir að lengd.", check_lengd_amk_2)
        postnumer = faValidInput("\nSláðu inn póstnúmer : ", "Verður að slá inn 3 tölustafi.", check_postnumer)
        
        aldur = int(aldur)
        
        print("\nNúna hafa allar upplýsingar verið slegnar inn.")
        
        print(f"\nÞú slóst inn þessar upplýsingar: \nNafn: {fornafn} {eftirnafn}\nAldur: {aldur}\nSímanúmer: {simanumer}\nHeimili: {heimilisfang}\nBær: {baer}\nPóstnúmer: {postnumer}")
        
        stadfesting = input("\nVeldu 1 til að staðfesta og 2 til að byrja uppá nýtt")
        
        while stadfesting not in ["1","2","0"]:
            stadfesting = input("\nVerður að velja annaðhvort 1 til að staðfesta eða 2 til að byrja uppá nýtt")
        
        if stadfesting == "1":
            # Sæki svo gögnin úr skránni og set í lista
            medlimaskra = readJSON("Skilaverk3.json")
            print("\nÞað tókst að lesa gögnin úr skránni")
            
            # Geri nýtt dictionary fyrir nýja meðliminn
            nyr_notandi = {
                "fornafn": fornafn,
                "eftirnafn": eftirnafn,
                "aldur": aldur,
                "símanúmer": simanumer,
                "heimili": {
                    "heimilisfang": heimilisfang,
                    "bær": baer,
                    "póstfang": postnumer
                }
            }
            
            # Bæti svo nýja meðlims dictionary við listann með öllum hinum
            medlimaskra.append(nyr_notandi)
            print("\nTókst að bæta nýja notandanum við listann.")
            
            # Skrifa gögnin aftur í skránna
            success = skrifa(medlimaskra)
            if success:
                return True
            else:
                return False
            
        elif stadfesting == "2":
            continue
        elif stadfesting == "0":
            return False
# ----- Hérna endar að bæta við nýjum notanda ----- #

# ----- Hérna er fallið sem skilar lista af öllum sem eru yngri en 50 ára ----- #
def yngriEn50():
    listiYngriEn50 = []
    
    # Sæki gögnin úr skránni og set í lista
    medlimaskra = readJSON("Skilaverk3.json")
    print("\nÞað tókst að lesa gögnin úr skránni") 
    
    print("\nNúna keyri ég í gegnum listann og finn alla sem eru yngri en 50 ára og set þau í sér lista")
    for medlimur in medlimaskra:
        aldur = int(medlimur['aldur'])
        if aldur < 50:
            listiYngriEn50.append(medlimur)
    print("\nÞað tókst að keyra leit eftir þeim eru yngri en 50 ára")
    
    if len(listiYngriEn50) > 0:
        skrifa(medlimaskra) # Skrifa alltaf gögnin í skránna aftur eftir notkun
        # Return bæði listanum og boolean True
        return listiYngriEn50, True
    
    else:
        skrifa(medlimaskra) # Skrifa alltaf gögnin í skránna aftur eftir notkun
        # Return engum lista og boolean False
        return None, False
        
# ----- Fallið sem prentar út skilmerkilega alla sem eru yngri en 50 ára ----- #
def prentaYngriEn50():
    listiYngriEn50, success = yngriEn50()
    if not success:
        return False
    else:
        print(f"\nÞað fundust {len(listiYngriEn50)} leitarniðurstöður. Núna verða niðurstöðurnar prentaðar út.")
        for nr, medlimur in enumerate(listiYngriEn50):
            print(f"\nLeitarniðurstaða {nr}")
            print(f"{medlimur['fornafn']} {medlimur['eftirnafn']}, {medlimur['aldur']}, {medlimur['símanúmer']}, {medlimur['heimili']['heimilisfang']}, {medlimur['heimili']['póstfang']} {medlimur['heimili']['bær']}")
        print("\nBúið að prenta út alla sem eru yngri en 50 ára")
        return True

# ----- Fallið sem finnur alla sem hafa símanúmer sem byrjar á 8 og setur þau í lista og skilar honum ásamt boolean ----- #  
def simanumerSemByrjaA8():
    listiSimanumerSemByrjaA8 = []
    
    # Sæki gögnin úr skránni og set í lista
    medlimaskra = readJSON("Skilaverk3.json")
    print("\nÞað tókst að lesa gögnin úr skránni") 
    
    print("\nNúna renni ég í gegnum listann og finn alla þá sem eru með símanúmer sem byrja á 8 og adda þeim í listann")
    
    for medlimur in medlimaskra:
        simanumer = medlimur['símanúmer']
        fyrstistafur = simanumer[0]
        if fyrstistafur == "8":
            listiSimanumerSemByrjaA8.append(medlimur)
    
    print("\nTókst að renna í gegnum listann")
    
    if len(listiSimanumerSemByrjaA8) > 0:
        skrifa(medlimaskra) # Skrifa alltaf gögnin í skránna aftur eftir notkun
        # Return bæði listanum og boolean True
        return listiSimanumerSemByrjaA8, True
    
    else:
        skrifa(medlimaskra) # Skrifa alltaf gögnin í skránna aftur eftir notkun
        # Return engum lista og boolean False
        return None, False

# ----- Fallið sem prentar út skilmerkilega alla með símanúmer sem byrjar á tölustafnum 8 ----- #   
def prentaSimanumerSemByrjaA8():
    listiSimanumerSemByrjaA8, success = simanumerSemByrjaA8()
    if not success:
        return False
    else:
        print(f"\nÞað fundust {len(listiSimanumerSemByrjaA8)} niðurstöður. Núna verða niðurstöðurnar prentaðar út.")
        for medlimur in listiSimanumerSemByrjaA8:
            print(f"\nNafn: {medlimur['fornafn']} {medlimur['eftirnafn']}")
            print(f"Símanúmer: {medlimur['símanúmer']}")
        return True
        


# Hefjum valmyndina líka inn í try except blokk til að grípa mögulegar villur sem koma upp
try:
        
    while True:

        print("\n1. Prenta út alla í skránni")
        print("2. Bæta við notanda í skránna")
        print("3. Heildaraldur")
        print("4. Yngri en 50 ára")
        print("5. Símanúmer sem byrjar á 8")
        
        print("\n0. Hætta")

        val = input("Hvað viltu gera?")

        # Prenta út alla í skránni
        if val == "1":
            try:
                success = prentaUtAlla()
                if not success:
                    print("\nÞað gekk ekki að prenta út alla í skránni")
                else:
                    print("\nÞað tókst að prenta út alla í skránni, Núna verðuru send/ur í aðalvalmyndina")
            except Exception as error:
                print(f"\nÞað kom upp villa við að prenta út alla í skránni. Gripin villa er : \n{error}")

        # Bæta við nýjum notanda
        elif val == "2":
            try:
                success = addMember()
                if not success:
                    print("\nEitthvað kom uppá við að bæta við meðlim")
                else:
                    print("\nTakk fyrir að bæta við nýjum meðlim, Núna verðuru send/ur í aðalvalmyndina")
            except Exception as error:
                print(f"\nÞað kom upp villa við að bæta við nýjum meðlim. Gripin villa er : \n{error}")
        
        # Heildaraldur      
        elif val == "3":
            try:
                heildar_aldur = heildaraldur()
                if not heildar_aldur:
                    print("\nFallið skilaði sér false til baka. Eitthvað hefur komið uppá")
                else:    
                    print(f"\nHeildar aldur allra sem eru í skránni er: {heildar_aldur}")
            except Exception as error:
                print(f"\nÞað kom upp villa við að reikna út heildaraldur. Gripin villa er : \n{error}")
        
        # Yngri en 50 ára
        elif val == "4":
            try:
                success = prentaYngriEn50()
                if not success:
                    print("\nÞað fundust engar leitarniðurstöður af fólki sem er yngri en 50 ára")
                else:
                    print("\nAllt gekk upp. Nú verðuru send/ur aftur í aðalvalmyndina")
            except Exception as error:
                print(f"\nÞað kom upp villa við keyrslu prentaYngriEn50. Gripin villa er : \n{error}")
        
        # Símanúmer sem byrja á 8
        elif val == "5":
            try:
                success = prentaSimanumerSemByrjaA8()
                if not success:
                    print("\nÞað fundust engar leitarniðurstöður af fólki sem er með símanúmer sem byrjar á 8")
                else:
                    print("\nAllt gekk upp. Nú verðuru send/ur aftur í aðalvalmyndina")
            except Exception as error:
                print(f"\nÞað kom upp villa við keyrslu prentaSimanumerSemByrjaA8. Gripin villa er : \n{error}")

        elif val == "0":
            break
        else:
            print("þú hefur ekki valið rétt")

    print("Takk fyrir að nota forritið mitt")

except Exception as error:
    print(f"Það hefur komið upp einhver villa. Gripin villa : \n{error}")